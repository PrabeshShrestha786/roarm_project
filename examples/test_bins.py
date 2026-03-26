from roarm import RoArm
from roarm.tasks import RoArmTasks

arm = RoArm("COM7")
tasks = RoArmTasks(arm)

arm.home()
tasks.pick_and_place_to_bin("bin1")
arm.disconnect()

print("Bin test complete.")