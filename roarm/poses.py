"""
These are starter poses.
You MUST calibrate them on your real robot/table setup.
All values are joint angles in radians.
"""

DEFAULT_POSES = {
    "home": {
        "base": 0.0,
        "shoulder": 0.0,
    },

    # Example pickup sequence
    "pickup_approach": {
        "base": 0.0,
        "shoulder": -0.20,
    },
    "pickup_grab": {
        "base": 0.0,
        "shoulder": -0.35,
    },
    "pickup_retract": {
        "base": 0.0,
        "shoulder": -0.10,
    },

    # Example camera pose
    "camera_view": {
        "base": 0.0,
        "shoulder": -0.15,
    },

    # Example bin poses (starter values only)
    "bin1_approach": {"base": -0.80, "shoulder": -0.10},
    "bin1_drop":     {"base": -0.80, "shoulder": -0.28},

    "bin2_approach": {"base": -0.40, "shoulder": -0.10},
    "bin2_drop":     {"base": -0.40, "shoulder": -0.28},

    "bin3_approach": {"base":  0.00, "shoulder": -0.10},
    "bin3_drop":     {"base":  0.00, "shoulder": -0.28},

    "bin4_approach": {"base":  0.40, "shoulder": -0.10},
    "bin4_drop":     {"base":  0.40, "shoulder": -0.28},

    "bin5_approach": {"base":  0.80, "shoulder": -0.10},
    "bin5_drop":     {"base":  0.80, "shoulder": -0.28},
}