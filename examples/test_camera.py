from roarm.camera import Camera


def test_camera():
    camera = Camera(0)  # 1 = USB camera
    path = camera.take_picture("test_capture_usb.jpg")
    print(f"Saved image to: {path}")
    return path


if __name__ == "__main__":
    test_camera()