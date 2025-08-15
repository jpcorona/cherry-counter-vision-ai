# 🍒 Visión Artificial para Conteo Automático de Cerezas en Línea de Producción

## 🎯 Objetivo
Implementar un sistema de **visión artificial** en la línea de producción de cerezas, capaz de detectar y contar automáticamente los frutos que pasan por la cinta transportadora, con el fin de:
- Garantizar un conteo más **preciso y consistente** que el realizado manualmente.
- **Reducir costos y tiempos operativos** asociados al control de producción.
- Proveer datos en tiempo real para la **trazabilidad y toma de decisiones** en la planta.

---

## 📝 Hipótesis
> La implementación de un sistema de conteo automático de cerezas basado en técnicas de visión artificial (segmentación por color y/o modelos YOLO de detección de objetos) permitirá alcanzar una **precisión superior al 95%** respecto al conteo manual de referencia, procesando en tiempo real (≥15 FPS) y reduciendo significativamente los errores humanos en la línea de producción.

### Hipótesis secundarias:
1. El sistema presentará una **variabilidad menor al 2%** en conteos repetidos sobre el mismo lote.
2. El conteo automático permitirá reducir al menos en un **80% el tiempo operativo** dedicado al control manual.
3. El modelo podrá adaptarse con reentrenamiento a otros productos similares (ej. uvas, arándanos).

---

## 🔬 Metodología de validación

### 3.1 Diseño experimental
- Se seleccionará un lote de producción de cerezas.
- Se grabará en video el paso de las cerezas por la cinta transportadora durante distintos turnos.
- El conteo se realizará de manera **paralela**:
  - **Método A**: Conteo manual por un operario especializado.
  - **Método B**: Conteo automático con el sistema de visión artificial.

### 3.2 Métricas a evaluar
- **Precisión (accuracy):**
  ```
  Precisión = |Conteo_automático - Conteo_real| / Conteo_real * 100
  ```
- **Tasa de procesamiento (FPS):** imágenes procesadas por segundo.
- **Consistencia:** variación en conteos sobre el mismo video.
- **Tiempo operativo:** minutos requeridos para obtener resultados con y sin el sistema.

### 3.3 Herramientas tecnológicas
- Librerías: **OpenCV, Ultralytics YOLO**.
- Hardware: cámara industrial (≥30 FPS, resolución ≥720p).
- Procesamiento: GPU/CPU estándar en la planta.

### 3.4 Criterios de éxito
- Precisión ≥ 95%.
- FPS ≥ 15 (tiempo real).
- Reducción de ≥ 80% en tiempo de conteo manual.

---

## 📊 Resultados Esperados
1. **Precisión del conteo:** >95% respecto al conteo manual.
2. **Rendimiento (FPS):** promedio de 15–25 FPS.
3. **Consistencia:** variabilidad <2% en conteos repetidos.
4. **Reducción de tiempos:** al menos 80% menos tiempo en comparación al conteo manual.
5. **Escalabilidad:** adaptable a otros frutos pequeños con reentrenamiento.

---

## ✅ Conclusión Preliminar
La aplicación de un sistema de **visión artificial para conteo de cerezas en la línea de producción** demuestra un alto potencial para mejorar la **eficiencia operativa**, reducir **errores humanos** y entregar información en tiempo real para la gestión productiva.

El piloto permitirá confirmar la hipótesis de que la visión artificial puede alcanzar niveles de precisión superiores al 95%, procesar en tiempo real y disminuir significativamente la carga operativa del personal.

De comprobarse los resultados esperados, la solución podrá **escalar a otras líneas y productos** dentro de la planta, contribuyendo a la **transformación digital de los procesos de control de calidad y productividad** en la industria agroalimentaria.
