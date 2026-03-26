from roarm import RoArm
import time

arm = RoArm("COM7")

# Start safe
arm.home()
time.sleep(3)

# Gripper
arm.open_gripper()
time.sleep(2)
arm.close_gripper()
time.sleep(2)

# Base
arm.move_base(0.3)
time.sleep(2)
arm.move_base(0.0)
time.sleep(2)

# Shoulder
arm.move_shoulder(-0.3)
time.sleep(2)
arm.move_shoulder(0.0)
time.sleep(2)

# Elbow
arm.move_elbow(1.8)
time.sleep(2)
arm.move_elbow(1.57)
time.sleep(2)

# Wrist 1
arm.move_wrist_1(0.3)
time.sleep(2)
arm.move_wrist_1(0.0)
time.sleep(2)

# Wrist 2
arm.move_wrist_2(0.3)
time.sleep(2)
arm.move_wrist_2(0.0)
time.sleep(2)

# End safe
arm.home()
time.sleep(2)
arm.disconnect()

print("All joint movement test complete.")