from roarm import RoArm
from roarm.tasks import RoArmTasks
from roarm.camera import Camera
from roarm.color_detect import detect_color
import time


delay = 1
# Base positions for each color bin
COLOR_BIN_BASE = {
    "red": -0.5,
    "blue": -0.8,
    "green": -1.1,
    "yellow": -1.4,
}


def pick_object(arm):
    # go to pickup position
    arm.move_shoulder(0.65)
    time.sleep(delay)

    arm.open_gripper()
    time.sleep(delay)

    arm.move_wrist_1(0.65)
    time.sleep(delay)

    arm.close_gripper()
    time.sleep(delay)

    arm.move_wrist_1(0.0)
    time.sleep(delay)

    arm.move_shoulder(0.0)
    time.sleep(delay)


def drop_object(arm, base_angle):
    # rotate to color bin
    arm.move_base(base_angle)
    time.sleep(delay)

    # move down to drop
    arm.move_shoulder(0.63)
    time.sleep(delay)

    arm.move_wrist_1(0.65)
    time.sleep(delay)

    arm.open_gripper()
    time.sleep(delay)

    # return back
    arm.move_wrist_1(0.0)
    time.sleep(delay)

    arm.close_gripper()
    time.sleep(delay)

    arm.move_shoulder(0.0)
    time.sleep(delay)

    arm.move_base(0.0)
    time.sleep(delay)


def main():
    image_path = "test_capture_usb.jpg"

    # Step 1: capture image
    camera = Camera(1)
    path = camera.take_picture(image_path)
    print(f"Saved image to: {path}")

    # Step 2: detect color
    detected_color = detect_color(path)
    print(f"Detected color: {detected_color}")

    if detected_color not in COLOR_BIN_BASE:
        print("Color not assigned to any bin. Stopping.")
        return

    base_angle = COLOR_BIN_BASE[detected_color]
    print(f"Moving object to {detected_color} bin at base angle {base_angle}")

    # Step 3: robot action
    arm = RoArm("COM7")
    tasks = RoArmTasks(arm)

    try:
        arm.home()
        time.sleep(delay)

        pick_object(arm)
        drop_object(arm, base_angle)

        arm.home()
        print("Pick and place complete.")

    finally:
        arm.disconnect()


if __name__ == "__main__":
    main()