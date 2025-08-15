"""
------------------------------------------------------------
Sistema de visión artificial para el conteo de cerezas
en una línea de producción simulada.

Método: Segmentación por color rojo en espacio HSV.
Autor: Juan pablo corona navarro
Fecha: 2025
------------------------------------------------------------
"""

import cv2
import numpy as np
import time


# ------------------------------------------------------------
# CONFIGURACIÓN GENERAL
# ------------------------------------------------------------

VIDEO_PATH = "cerezas_linea_realista.mp4"   # Video de entrada
OUTPUT_PATH = "cerezas_contadas_mejorado.mp4"  # Video de salida
LOG_FILE = "conteo_cerezas.txt"                # Archivo de log

# Umbrales de detección en HSV para el color rojo
LOWER_RED1 = np.array([0, 120, 70])
UPPER_RED1 = np.array([10, 255, 255])
LOWER_RED2 = np.array([170, 120, 70])
UPPER_RED2 = np.array([180, 255, 255])

MIN_AREA = 200   # Área mínima para considerar una cereza válida
BELT_HEIGHT = 200  # Altura aproximada de la franja de la cinta

# ------------------------------------------------------------
# FUNCIONES AUXILIARES
# ------------------------------------------------------------

def inicializar_video(path_video: str, path_salida: str):
    """
    Inicializa el video de entrada y el escritor de salida.
    Retorna:
        cap: objeto de captura de OpenCV
        out: objeto de escritura de OpenCV
        w, h, fps: ancho, alto y FPS del video
    """
    cap = cv2.VideoCapture(path_video)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter(path_salida,
                          cv2.VideoWriter_fourcc(*"mp4v"),
                          fps, (w, h))
    return cap, out, w, h, fps


def segmentar_rojo(frame: np.ndarray) -> np.ndarray:
    """
    Segmenta el color rojo en una imagen usando HSV.
    Retorna una máscara binaria.
    """
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv, LOWER_RED1, UPPER_RED1)
    mask2 = cv2.inRange(hsv, LOWER_RED2, UPPER_RED2)
    return mask1 | mask2


def calcular_precision_estimada(areas: list) -> float:
    """
    Calcula una métrica de precisión estimada en base a la
    consistencia del tamaño de las detecciones.
    Retorna un porcentaje.
    """
    if len(areas) == 0:
        return 0.0
    avg_area = np.mean(areas)
    std_area = np.std(areas)
    # cuanto menor sea la desviación relativa, más “preciso”
    precision = max(0, 100 - (std_area / avg_area * 100))
    return precision


# ------------------------------------------------------------
# PROCESAMIENTO PRINCIPAL
# ------------------------------------------------------------

def procesar_video():
    # Inicializar video y salida
    cap, out, w, h, fps = inicializar_video(VIDEO_PATH, OUTPUT_PATH)

    # Línea de conteo en la mitad vertical
    line_y = h // 2
    count = 0

    # Abrir archivo de log
    log_file = open(LOG_FILE, "w")

    prev_time = time.time()  # para cálculo de FPS

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Tiempo transcurrido en segundos
        current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0

        # Segmentación por color rojo
        mask = segmentar_rojo(frame)

        # Encontrar contornos (cerezas detectadas)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        detections_in_frame = 0
        occupied_area = 0
        areas = []

        # Procesar cada contorno detectado
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > MIN_AREA:
                x, y, w_box, h_box = cv2.boundingRect(cnt)
                cx = x + w_box // 2
                cy = y + h_box // 2

                # Dibujar bounding box y centro
                cv2.rectangle(frame, (x, y), (x+w_box, y+h_box), (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 4, (255, 0, 0), -1)

                detections_in_frame += 1
                occupied_area += area
                areas.append(area)

                # Verificar cruce de la línea
                if line_y-5 <= cy <= line_y+5:
                    count += 1
                    log_file.write(f"Frame {int(cap.get(cv2.CAP_PROP_POS_FRAMES))}: Count={count}\n")

        # Calcular métricas adicionales
        belt_area = w * BELT_HEIGHT
        occupancy_pct = (occupied_area / belt_area) * 100
        precision_est = calcular_precision_estimada(areas)

        new_time = time.time()
        fps_real = 1 / (new_time - prev_time)
        prev_time = new_time

        # Dibujar línea de conteo
        cv2.line(frame, (0, line_y), (w, line_y), (255, 0, 0), 2)

        # Panel informativo (fondo semi-transparente)
        overlay = frame.copy()
        cv2.rectangle(overlay, (10, 10), (400, 200), (0, 0, 0), -1)
        frame = cv2.addWeighted(overlay, 0.4, frame, 0.6, 0)

        # Mostrar datos en pantalla
        cv2.putText(frame, f"Contador Total: {count}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        cv2.putText(frame, f"Detecciones (frame): {detections_in_frame}", (20, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f"Ocupación: {occupancy_pct:.1f}%", (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 150, 0), 2)
        cv2.putText(frame, f"FPS: {fps_real:.1f}", (20, 130),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 255), 2)
        cv2.putText(frame, f"Tiempo: {current_time:.1f}s", (200, 130),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, f"Precision est.: {precision_est:.1f}%", (20, 160),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 255), 2)

        # Mostrar ventana
        cv2.imshow("Conteo de Cerezas Mejorado", frame)
        out.write(frame)

        # Salir con 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Liberar recursos
    cap.release()
    out.release()
    log_file.close()
    cv2.destroyAllWindows()


# ------------------------------------------------------------
# EJECUCIÓN
# ------------------------------------------------------------
if __name__ == "__main__":
    procesar_video()
