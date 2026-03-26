import cv2
import numpy as np


def detect_color(image_path, debug=False):
    img = cv2.imread(image_path)
    if img is None:
        raise RuntimeError(f"Could not read image: {image_path}")

    # Resize for consistency
    img = cv2.resize(img, (640, 480))

    # Focus only on center area
    h, w = img.shape[:2]
    x1 = int(w * 0.25)
    y1 = int(h * 0.25)
    x2 = int(w * 0.75)
    y2 = int(h * 0.75)
    roi = img[y1:y2, x1:x2]

    # Slight blur to reduce noise
    roi = cv2.GaussianBlur(roi, (5, 5), 0)

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    h_channel, s_channel, v_channel = cv2.split(hsv)

    # Keep only strong colored pixels
    colored_mask = (s_channel > 70) & (v_channel > 50)

    # If not enough colored pixels, then fallback to neutral colors
    colored_pixels = np.count_nonzero(colored_mask)

    if debug:
        print(f"Colored pixels: {colored_pixels}")

    if colored_pixels > 500:
        hue_values = h_channel[colored_mask]

        # Hue bins
        counts = {
            "red": int(np.sum((hue_values >= 0) & (hue_values <= 10)) +
                       np.sum((hue_values >= 170) & (hue_values <= 179))),
            "orange": int(np.sum((hue_values >= 11) & (hue_values <= 20))),
            "yellow": int(np.sum((hue_values >= 21) & (hue_values <= 34))),
            "green": int(np.sum((hue_values >= 35) & (hue_values <= 85))),
            "blue": int(np.sum((hue_values >= 86) & (hue_values <= 130))),
            "purple": int(np.sum((hue_values >= 131) & (hue_values <= 155))),
            "pink": int(np.sum((hue_values >= 156) & (hue_values <= 169))),
        }

        if debug:
            print("Hue counts:")
            for name, count in counts.items():
                print(f"{name}: {count}")

        best_color = max(counts, key=counts.get)
        best_count = counts[best_color]

        if best_count > 200:
            if debug:
                print(f"Detected dominant color: {best_color}")
            return best_color

    # Fallback for black / white / gray only if strong color was not found
    black_mask = (v_channel < 50)
    white_mask = (s_channel < 40) & (v_channel > 180)
    gray_mask = (s_channel < 40) & (v_channel >= 50) & (v_channel <= 180)

    neutral_counts = {
        "black": int(np.count_nonzero(black_mask)),
        "white": int(np.count_nonzero(white_mask)),
        "gray": int(np.count_nonzero(gray_mask)),
    }

    if debug:
        print("Neutral counts:")
        for name, count in neutral_counts.items():
            print(f"{name}: {count}")

    best_neutral = max(neutral_counts, key=neutral_counts.get)
    if neutral_counts[best_neutral] > 500:
        if debug:
            print(f"Detected neutral color: {best_neutral}")
        return best_neutral

    return "unknown"