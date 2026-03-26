from typing import Dict

from .poses import DEFAULT_POSES
from .bins import DEFAULT_BINS
from .robot import RoArm


class RoArmTasks:
    def __init__(
        self,
        robot: RoArm,
        poses: Dict[str, Dict[str, float]] | None = None,
        bins: Dict[str, Dict[str, str]] | None = None,
    ):
        self.robot = robot
        self.poses = poses if poses is not None else DEFAULT_POSES
        self.bins = bins if bins is not None else DEFAULT_BINS

    def go_to_named_pose(self, pose_name: str):
        if pose_name not in self.poses:
            raise ValueError(f"Unknown pose: {pose_name}")
        self.robot.go_to_pose(self.poses[pose_name])

    def pick_up(
        self,
        approach_pose: str = "pickup_approach",
        grab_pose: str = "pickup_grab",
        retract_pose: str = "pickup_retract",
    ):
        print("Starting pick_up()...")
        self.robot.open_gripper()
        self.go_to_named_pose(approach_pose)
        self.go_to_named_pose(grab_pose)
        self.robot.close_gripper()
        self.go_to_named_pose(retract_pose)
        print("pick_up() complete.")

    def put_down(
        self,
        approach_pose: str,
        place_pose: str,
        retract_pose: str,
    ):
        print("Starting put_down()...")
        self.go_to_named_pose(approach_pose)
        self.go_to_named_pose(place_pose)
        self.robot.open_gripper()
        self.go_to_named_pose(retract_pose)
        print("put_down() complete.")

    def move_to_bin(self, bin_name: str):
        if bin_name not in self.bins:
            raise ValueError(f"Unknown bin: {bin_name}")

        bin_info = self.bins[bin_name]
        self.go_to_named_pose(bin_info["approach_pose"])
        self.go_to_named_pose(bin_info["drop_pose"])

    def drop_in_bin(self, bin_name: str):
        if bin_name not in self.bins:
            raise ValueError(f"Unknown bin: {bin_name}")

        bin_info = self.bins[bin_name]
        approach_pose = bin_info["approach_pose"]
        drop_pose = bin_info["drop_pose"]

        print(f"Dropping object in {bin_name}...")
        self.go_to_named_pose(approach_pose)
        self.go_to_named_pose(drop_pose)
        self.robot.open_gripper()
        self.go_to_named_pose(approach_pose)
        print(f"drop_in_bin({bin_name}) complete.")

    def pick_and_place_to_bin(self, bin_name: str):
        print(f"Starting pick_and_place_to_bin({bin_name})...")
        self.pick_up()
        self.drop_in_bin(bin_name)
        self.robot.home()
        print("pick_and_place_to_bin() complete.")