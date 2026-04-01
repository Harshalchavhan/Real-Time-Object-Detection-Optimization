import cv2
from ultralytics import YOLO
import time

# Optimized YOLO Detection with Performance Enhancements
model = YOLO("yolov8n.pt")  # lightweight model for speed

# Try to use GPU if available
try:
    model.to('cuda')
    print("Using GPU acceleration")
except:
    print("Using CPU")

cap = cv2.VideoCapture(0)

# Performance tracking variables
frame_count = 0
total_fps = 0
total_latency = 0
processed_frames = 0

print("=== Optimized YOLO Detection Started ===")
print("Press 'ESC' to exit, 'P' to pause/resume")

paused = False

while True:
    if not paused:
        start = time.time()

        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # Optimization 1: Frame skipping (process every 2nd frame)
        if frame_count % 2 != 0:
            continue

        # Optimization 2: Resolution scaling
        frame = cv2.resize(frame, (640, 480))

        # Run detection
        results = model(frame)

        # Get detection results
        boxes = results[0].boxes
        object_count = len(boxes)

        end = time.time()
        latency = (end - start) * 1000  # in milliseconds
        fps = 1 / (end - start)

        # Update performance metrics
        processed_frames += 1
        total_fps += fps
        total_latency += latency

        # Create annotated frame
        annotated_frame = results[0].plot()

        # Display FPS and latency
        cv2.putText(annotated_frame, f"FPS: {fps:.1f}",
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

        cv2.putText(annotated_frame, f"Latency: {latency:.1f}ms",
                    (20, 80), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2)

        # Extra Feature 1: Object Counter
        cv2.putText(annotated_frame, f"Objects: {object_count}",
                    (20, 120), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 0), 2)

        # Extra Feature 2: Class Name Display (show top detection)
        if object_count > 0:
            # Get the first detected object
            cls = int(boxes[0].cls[0])
            conf = float(boxes[0].conf[0])
            class_name = model.names[cls]

            cv2.putText(annotated_frame, f"Top: {class_name} ({conf:.2f})",
                        (20, 160), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0, 255, 255), 2)

        # Display frame count
        cv2.putText(annotated_frame, f"Frame: {processed_frames}",
                    (annotated_frame.shape[1] - 150, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow("Optimized YOLO Detection", annotated_frame)

    # Handle keyboard input
    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break
    elif key == ord('p') or key == ord('P'):  # Pause/Resume
        paused = not paused
        status = "PAUSED" if paused else "RESUMED"
        print(f"Detection {status}")

# Print final performance summary
if processed_frames > 0:
    avg_fps = total_fps / processed_frames
    avg_latency = total_latency / processed_frames

    print("\n=== Performance Summary ===")
    print(f"Total frames processed: {processed_frames}")
    print(f"Average FPS: {avg_fps:.2f}")
    print(f"Average Latency: {avg_latency:.1f}ms")
    print("\n=== Optimizations Applied ===")
    print("✓ Resolution scaling: 640x480")
    print("✓ Frame skipping: every 2nd frame")
    print("✓ Lightweight model: yolov8n.pt")
    print("✓ GPU acceleration (if available)")
    print("✓ Object counting and class display")

cap.release()
cv2.destroyAllWindows()