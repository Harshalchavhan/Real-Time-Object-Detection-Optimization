import time
import cv2
from ultralytics import YOLO


def run_optimized(video_source=0, model_name='yolov8n.pt'):
    cap = cv2.VideoCapture(video_source)
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open video source {video_source}")

    model = YOLO(model_name)
    try:
        model.to('cuda')
        use_cuda = True
        print('Optimized model moved to GPU')
    except Exception:
        use_cuda = False
        print('Optimized running on CPU')

    frame_count = 0
    processed = 0
    t_start = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # Frame skipping: process every 2nd frame
        if frame_count % 2 != 0:
            continue

        # Resolution optimization
        frame_resized = cv2.resize(frame, (640, 480))

        t0 = time.time()
        results = model(frame_resized)
        t1 = time.time()

        latency_ms = (t1 - t0) * 1000.0
        processed += 1

        count = len(results[0].boxes)
        cv2.putText(frame_resized, f"Latency: {latency_ms:.1f} ms", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame_resized, f"Objects: {count}", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow('Optimized', frame_resized)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    t_end = time.time()
    cap.release()
    cv2.destroyAllWindows()

    total_time = t_end - t_start
    fps = processed / total_time if total_time > 0 else 0
    print(f"Optimized frames processed: {processed}")
    print(f"Optimized average FPS: {fps:.2f}")
    print(f"Optimized average latency: {1000.0/fps:.1f} ms" if fps > 0 else "")


if __name__ == '__main__':
    run_optimized()