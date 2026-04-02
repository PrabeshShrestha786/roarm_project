from roarm import RoArm
from roarm.camera import Camera
from roarm.color_detect import detect_color
import time


delay = 1.5

# Base positions for bins
COLOR_BIN_BASE = {
    "red": -0.5,
    "blue": -0.8,
    "green": -1.1,
    "yellow": -1.4,
    "pink": -0.5,
}


# 🔍 Move robot to position where camera can see object
def move_to_scan_position(arm):
    print("Moving to scan position...")

    arm.move_base(0.0)
    time.sleep(delay)

    arm.move_wrist_1(-0.25)
    time.sleep(delay)
    
    arm.move_elbow(2.25)
    time.sleep(delay)

    arm.move_shoulder(0.5)
    time.sleep(delay)

    

# 🤖 Move to pick pose (lower down)
def pick_object(arm):
    print("Picking object...")
    
    arm.open_gripper()
    time.sleep(delay)
    
    arm.move_elbow(1.5)
    time.sleep(delay)
    
    arm.move_shoulder(0.67)
    time.sleep(delay)

    arm.move_wrist_1(0.65)
    time.sleep(delay)

    arm.close_gripper()
    time.sleep(delay)

    # lift object
    arm.move_wrist_1(0.0)
    time.sleep(delay)

    arm.move_shoulder(0.0)
    time.sleep(delay)


# 📦 Drop in correct bin
def drop_object(arm, base_angle):
    print("Dropping object...")

    arm.move_base(base_angle)
    time.sleep(delay)

    arm.move_shoulder(0.65)
    time.sleep(delay)
    

    arm.move_wrist_1(0.65)
    time.sleep(delay)

    arm.open_gripper()
    time.sleep(delay)

    # reset
    arm.move_wrist_1(0.0)
    time.sleep(delay)

    arm.close_gripper()
    time.sleep(delay)

    arm.move_shoulder(0.0)
    time.sleep(delay)

    arm.move_base(0.0)
    time.sleep(delay)


def main():
    camera = Camera(0)
    arm = RoArm("COM7")

    try:
        arm.home()
        time.sleep(delay)

        # STEP 1: Move to scan position
        move_to_scan_position(arm)

        # STEP 2: Capture image
        arm.move_wrist_2(1.4)
        time.sleep(2)
        arm.light_on(59)
        time.sleep(1)
        image_path = camera.take_picture("test_capture_usb.jpg")
        print(f"Image captured: {image_path}")
        arm.light_off()
        arm.move_wrist_2(0.0)
        time.sleep(2)

        # STEP 3: Detect color
        detected_color = detect_color(image_path)
        print(f"Detected color: {detected_color}")

        if detected_color not in COLOR_BIN_BASE:
            print("Unknown color. Stopping.")
            return

        base_angle = COLOR_BIN_BASE[detected_color]

        # STEP 4: Pick object
        pick_object(arm)

        # STEP 5: Drop object
        drop_object(arm, base_angle)

        arm.home()
        print("Task complete.")

    finally:
        arm.disconnect()


if __name__ == "__main__":
    main()