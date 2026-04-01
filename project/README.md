# YOLO Object Detection Optimization Project

## 🚀 Project Overview
This project demonstrates real-time object detection using YOLOv8 with performance optimizations for better FPS and reduced latency.

## 📊 Performance Results

### Baseline vs Optimized Comparison

| Metric          | Baseline | Optimized | Improvement |
|-----------------|----------|-----------|-------------|
| FPS            | 12      | 22       | +83%       |
| Latency (ms)   | 80      | 40       | -50%       |
| Resolution     | 1280p   | 480p     | -62% pixels |
| Frame Skip     | No      | Yes      | 50% frames |
| Model          | yolov8m | yolov8n  | -50% params |

## ⚡ Optimizations Applied

### 1. **Resolution Scaling**
```python
frame = cv2.resize(frame, (640, 480))  # From 1280x720 to 640x480
```
- **Impact**: 20-40% speed increase
- **Trade-off**: Slight accuracy reduction

### 2. **Frame Skipping**
```python
if frame_count % 2 != 0:
    continue  # Skip every other frame
```
- **Impact**: 30-50% FPS boost
- **Trade-off**: Potential motion blur for fast objects

### 3. **Lightweight Model**
```python
model = YOLO("yolov8n.pt")  # Instead of yolov8m.pt
```
- **Impact**: Faster inference
- **Trade-off**: Slightly lower accuracy

### 4. **GPU Acceleration**
```python
model.to('cuda')  # If GPU available
```
- **Impact**: Significant speed boost on GPU systems

## 🎯 Extra Features

### Object Counter
- Displays total number of detected objects
- Real-time count overlay

### Class Name Display
- Shows the most confident detection class
- Includes confidence score

### Performance Metrics
- Real-time FPS display
- Latency measurement in milliseconds
- Frame counter

## 🛠️ Installation & Usage

### Prerequisites
```bash
pip install opencv-python ultralytics matplotlib
```

### Running the Optimized Detection
```bash
python optimization.py
```

### Generating Performance Graphs
```bash
python project/performance_graph.py
```

### Running Baseline Comparison
```bash
python project/baseline.py
```

### Running Optimized Version
```bash
python project/optimized.py
```

## 🎮 Controls
- **ESC**: Exit the application
- **P**: Pause/Resume detection

## 📈 Viva Preparation Points

### Key Talking Points:
1. **"We improved FPS from 12 to 22 (~80% improvement)"**
2. **"Used resolution scaling, frame skipping, and lightweight model"**
3. **"Trade-off: slight accuracy reduction but real-time performance improved"**
4. **"Added object counting and class name display for enhanced UX"**

### Technical Details:
- YOLOv8 nano model for edge deployment
- OpenCV for real-time video processing
- Performance metrics collection and visualization
- GPU acceleration support

## 📁 Project Structure
```
project/
├── baseline.py          # Unoptimized version
├── optimized.py         # Optimized version
├── graph.py            # Performance visualization
├── performance_graph.py # Enhanced comparison graphs
└── README.md           # This file
```

## 🔧 Customization

### Adjust Frame Skipping
```python
if frame_count % 3 != 0:  # Process every 3rd frame
    continue
```

### Change Resolution
```python
frame = cv2.resize(frame, (320, 240))  # Even smaller for more speed
```

### Different Model
```python
model = YOLO("yolov8s.pt")  # Small model
```

## 📊 Expected Viva Questions & Answers

**Q: What optimizations did you implement?**
A: Resolution scaling (640x480), frame skipping (every 2nd frame), lightweight model (yolov8n), and GPU acceleration.

**Q: What was the performance improvement?**
A: 83% FPS increase (12→22) and 50% latency reduction (80ms→40ms).

**Q: What trade-offs did you make?**
A: Slight accuracy reduction for significantly better real-time performance.

**Q: What extra features did you add?**
A: Object counting, class name display with confidence scores, and real-time performance metrics.