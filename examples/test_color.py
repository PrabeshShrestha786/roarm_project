from roarm.color_detect import detect_color


def test_color():
    image_path = "test_capture_usb.jpg"
    color = detect_color(image_path, debug=True)
    print("Detected color:", color)
    return color


if __name__ == "__main__":
    test_color()