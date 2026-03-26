import serial
import time

GRIPPER_CMD = 106
HOME_CMD = 100
JOINT_MOVE_CMD = 101

GRIPPER_OPEN = 1.57
GRIPPER_CLOSE = 3.14

JOINT_BASE = 1
JOINT_SHOULDER = 2
JOINT_ELBOW = 3
JOINT_WRIST_1 = 4
JOINT_WRIST_2 = 5


class RoArm:
    def __init__(self, port="COM7", baudrate=115200):
        print(f"Connecting to robot on {port}...")
        self.ser = serial.Serial(port, baudrate=baudrate, timeout=1, dsrdtr=None)
        self.ser.setRTS(False)
        self.ser.setDTR(False)
        time.sleep(2)
        print("Connected.")

    def send(self, cmd: str, delay: float = 0.1):
        self.ser.write((cmd + "\n").encode())
        time.sleep(delay)

    def home(self, delay: float = 0.1):
        print("Moving to home position...")
        self.send(f'{{"T":{HOME_CMD}}}', delay=delay)

    def set_gripper(self, angle: float, spd: int = 0, acc: int = 0, delay: float = 0.1):
        print(f"Setting gripper angle to {angle}...")
        self.send(
            f'{{"T":{GRIPPER_CMD},"cmd":{angle},"spd":{spd},"acc":{acc}}}',
            delay=delay,
        )

    def open_gripper(self, delay: float = 0.1):
        print("Opening gripper...")
        self.set_gripper(GRIPPER_OPEN, delay=delay)

    def close_gripper(self, delay: float = 0.1):
        print("Closing gripper...")
        self.set_gripper(GRIPPER_CLOSE, delay=delay)

    def move_joint(self, joint: int, rad: float, spd: int = 0, acc: int = 10, delay: float = 0.1):
        print(f"Moving joint {joint} to {rad} rad...")
        self.send(
            f'{{"T":{JOINT_MOVE_CMD},"joint":{joint},"rad":{rad},"spd":{spd},"acc":{acc}}}',
            delay=delay,
        )

    def move_base(self, rad: float, spd: int = 0, acc: int = 10, delay: float = 0.1):
        self.move_joint(JOINT_BASE, rad, spd, acc, delay)

    def move_shoulder(self, rad: float, spd: int = 0, acc: int = 10, delay: float = 0.1):
        self.move_joint(JOINT_SHOULDER, rad, spd, acc, delay)

    def move_elbow(self, rad: float, spd: int = 0, acc: int = 10, delay: float = 0.1):
        self.move_joint(JOINT_ELBOW, rad, spd, acc, delay)

    def move_wrist_1(self, rad: float, spd: int = 0, acc: int = 10, delay: float = 0.1):
        self.move_joint(JOINT_WRIST_1, rad, spd, acc, delay)

    def move_wrist_2(self, rad: float, spd: int = 0, acc: int = 10, delay: float = 0.1):
        self.move_joint(JOINT_WRIST_2, rad, spd, acc, delay)

    def disconnect(self):
        print("Disconnecting...")
        self.ser.close()
        print("Disconnected.")