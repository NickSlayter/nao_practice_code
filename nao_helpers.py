




# Function to bound the amount you can change position
def clamp(value, minimum, maximum):
    return max(minimum, min(maximum, value))

def apply_pose(target_positions, pose):
    """
    Copy the pose values into the active target_positions dictionary.

    target_positions is the controller's current desired robot state.
    pose is a dictionary returned by a gesture function.
    """

    for joint_name, position in pose.items():
        if joint_name not in target_positions:
            print(f'Warning: "{joint_name}" is not in target_positions.')
            continue

        target_positions[joint_name] = position
    return None