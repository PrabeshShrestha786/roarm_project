from pathlib import Path
import cv2


class Camera:
    def __init__(self, camera_index: int = 0):
        self.camera_index = camera_index

    def take_picture(self, output_path: str = "capture.jpg") -> str:
        # Try default backend first
        cap = cv2.VideoCapture(self.camera_index, cv2.CAP_DSHOW)

        if not cap.isOpened():
            raise RuntimeError(f"Could not open camera at index {self.camera_index}.")

        ok, frame = cap.read()
        cap.release()

        if not ok:
            raise RuntimeError(f"Could not capture image from camera at index {self.camera_index}.")

        output = Path(output_path)
        cv2.imwrite(str(output), frame)
        return str(output)