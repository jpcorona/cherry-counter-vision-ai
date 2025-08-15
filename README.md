# 🍒 Vision AI for Automatic Cherry Counting

## 📄 Project Description
This project implements a **computer vision system** for **automatic cherry counting** on a **simulated production line**.  

The base video was **generated with Artificial Intelligence**, simulating a conveyor belt with cherries moving at industrial speed. This synthetic scenario allows controlled experimentation without relying on sensitive industrial data.  

The first approach uses **color segmentation in HSV space** to detect and count cherries. On top of this baseline, more advanced AI models such as **YOLOv8/YOLO11** are integrated and compared for **real-time object detection**.  

Key metrics evaluated include:
- **Counting accuracy**  
- **Frame rate (FPS)**  
- **Occupancy of the conveyor belt**  
- **Stability of detections**  

This project is part of the **Master in Information Technology at Universidad Técnica Federico Santa María (UTFSM, Chile)**, showcasing AI applications in the agro-industrial sector.  

---

## 🎯 Objectives
- Automate the counting of cherries on a conveyor belt.  
- Compare classical computer vision (HSV segmentation) with modern deep learning (YOLO).  
- Provide **real-time metrics and logging** for industrial monitoring.  
- Contribute to **digital transformation and quality control optimization** in agro-industry.  

---

## 🛠️ Technologies Used
- **Python 3.9+**  
- **OpenCV** (color segmentation, video processing, visualization)  
- **NumPy** (image operations and metrics)  
- **Ultralytics YOLO** (real-time object detection models)  
- **AI-generated synthetic video** simulating cherries on a conveyor belt  

---

## 🚀 Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/cherry-counter-vision-ai.git
cd cherry-counter-vision-ai
pip install -r requirements.txt
```

Dependencies (`requirements.txt`):
```
opencv-python
numpy
ultralytics
```

---

## ▶️ Usage

### 1. Run cherry counting with HSV segmentation:
```bash
python cherry_counter_hsv.py
```

### 2. Run cherry counting with YOLO:
```bash
python cherry_counter_yolo.py
```

### 3. Outputs generated:
- `cerezas_contadas_mejorado.mp4` → video with bounding boxes, line crossing and metrics overlay  
- `conteo_cerezas.txt` → log file with frame-by-frame counts  

---

## 📊 Example Metrics on Screen
- **Total Count**: accumulated cherries detected  
- **Detections (per frame)**: objects detected in the current frame  
- **Occupancy %**: percentage of the conveyor belt occupied by cherries  
- **FPS**: processing speed in frames per second  
- **Time**: elapsed time in video  
- **Estimated Precision %**: confidence/consistency of detections  

---

## ✅ Results & Expected Impact
- Accuracy > **95%** compared to manual counting  
- Real-time performance at **15–25 FPS**  
- Reduction of manual counting time by **80%**  
- Potential scalability to other fruits (grapes, blueberries)  

---

## 👤 Author
**Juan Pablo Corona Navarro**  
Master in Information Technology (MTI)  
**Universidad Técnica Federico Santa María (UTFSM, Chile)**  
2025  

---

## 📜 License
This project is released under the MIT License. You are free to use, modify and distribute it with proper attribution.  
