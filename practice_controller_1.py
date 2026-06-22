from controller import Robot, Keyboard, DistanceSensor
from nao_gestures import point_up_right
from nao_gestures import neutral_pose
import math
from nao_helpers import apply_pose
import nao_constants as const
from nao_sound_localization_practice import get_sound_direction, look_toward_sound



robot = Robot()
timestep = int(robot.getBasicTimeStep())

# 1 Get motors and sensors here
"""
head_yaw = robot.getDevice("HeadYaw")
head_pitch = robot.getDevice("HeadPitch")

RShoulder_Pitch = robot.getDevice("RShoulderPitch")
RShoulder_Roll = robot.getDevice("RShoulderRoll")

R_Phalanx1 = robot.getDevice("RPhalanx1")
R_Phalanx2 = robot.getDevice("RPhalanx2")
R_Phalanx3 = robot.getDevice("RPhalanx3")
R_Phalanx4 = robot.getDevice("RPhalanx4")
R_Phalanx5 = robot.getDevice("RPhalanx5")
R_Phalanx6 = robot.getDevice("RPhalanx6")
R_Phalanx7 = robot.getDevice("RPhalanx7")
R_Phalanx8 = robot.getDevice("RPhalanx8")
distance_sensor_left = robot.getDevice("Sonar/Left")
"""

# 2. Configure devices here

motors = {
    "HeadYaw": robot.getDevice("HeadYaw"),
    "HeadPitch": robot.getDevice("HeadPitch"),
    "RShoulderPitch": robot.getDevice("RShoulderPitch"),
    "RShoulderRoll": robot.getDevice("RShoulderRoll"),
    "RPhalanx1_position" : robot.getDevice("RPhalanx1"),
    "RPhalanx2_position" : robot.getDevice("RPhalanx2"),
    "RPhalanx3_position" : robot.getDevice("RPhalanx3"),
    "RPhalanx4_position" : robot.getDevice("RPhalanx4"),
    "RPhalanx5_position" : robot.getDevice("RPhalanx5"),
    "RPhalanx6_position" : robot.getDevice("RPhalanx6"),
    "RPhalanx7_position" : robot.getDevice("RPhalanx7"),
    "RPhalanx8_position" : robot.getDevice("RPhalanx8")
}

for motor in motors.values():
    motor.setVelocity(1.0)

# Predetermined Finger Positions
"""

head_yaw_position = 0.0
head_pitch_position = 0.0

shoulder_pitch_position = 0.0
shoulder_roll_position = 0.0

RPhalanx1_position = 0.0
RPhalanx2_position = 0.0
RPhalanx3_position = 0.0
RPhalanx4_position = 0.0
RPhalanx5_position = 0.0
RPhalanx6_position = 0.0
RPhalanx7_position = 0.0
RPhalanx8_position = 0.0

R_Phalanx1.setPosition(RPhalanx1_position)
R_Phalanx2.setPosition(RPhalanx2_position)
R_Phalanx3.setPosition(RPhalanx3_position)
R_Phalanx4.setPosition(RPhalanx4_position)
R_Phalanx5.setPosition(RPhalanx5_position)
R_Phalanx6.setPosition(RPhalanx6_position)
R_Phalanx7.setPosition(RPhalanx7_position)
R_Phalanx8.setPosition(RPhalanx8_position)
"""

# Dictionary to hold positions


target_positions = {
    "HeadYaw": 0.0,
    "HeadPitch": 0.0,
    "RShoulderPitch": 1.8,
    "RShoulderRoll": 0.0,
    "RPhalanx1_position" : 0.0,
    "RPhalanx2_position" : 0.0,
    "RPhalanx3_position" : 0.0,
    "RPhalanx4_position" : 0.0,
    "RPhalanx5_position" : 0.0,
    "RPhalanx6_position" : 0.0,
    "RPhalanx7_position" : 0.0,
    "RPhalanx8_position" : 0.0
}

# Set up Keyboard
keyboard = Keyboard()
keyboard.enable(timestep)

# Set movement steps
YAW_STEP = 0.01
PITCH_STEP = 0.01


# Limits on ROM
HEAD_YAW_MAX = 1.0
HEAD_YAW_MIN = -1.0

HEAD_PITCH_MAX = 0.5
HEAD_PITCH_MIN = -0.5

RSHOULDER_PITCH_MAX = 2.0
RSHOULDER_PITCH_MIN = -2.0

RSHOULDER_ROLL_MAX = 0.31
RSHOULDER_ROLL_MIN = -1.2



# Main control loop
while robot.step(timestep) != -1:
    # Read sensors
    # Decide what to do
    key = keyboard.getKey()

    if key == ord("R"):
        pose = point_up_right()
        apply_pose(target_positions, pose)
    
    if key == ord("N"):
        pose = neutral_pose()
        apply_pose(target_positions, pose)

    if key == ord("P"):
        print(target_positions)

    for joint_name, position in target_positions.items():
        motors[joint_name].setPosition(position)


    """
    if key == ord("A"):
        head_yaw_position += YAW_STEP       # look left
        
    elif key == ord("D"):
        head_yaw_position -= YAW_STEP       # look right
        
    elif key == ord("W"):
        head_pitch_position -= PITCH_STEP   # look up
    
    elif key == ord("S"):
        head_pitch_position += PITCH_STEP   # Look down
    
    elif key == ord("C"):
        head_yaw_position = 0.0
        head_pitch_position = 0.0
        
    elif key == ord("P"):
        print("Head Yaw", head_yaw_position, "Head Pitch", head_pitch_position,
        "Shoulder Roll", shoulder_roll_position, "Shoulder Pitch", shoulder_pitch_position)
        
    elif key == ord("H"):
        shoulder_roll_position -= YAW_STEP       # 
        
    elif key == ord("U"):
        shoulder_pitch_position -= PITCH_STEP   # 
    
    elif key == ord("J"):
        shoulder_pitch_position += PITCH_STEP   # 
    
    elif key == ord("K"):
        shoulder_roll_position += YAW_STEP
        
    elif key == ord("R"):
        point_up_right()
       
    # Command Motors
    head_yaw_position = clamp(head_yaw_position, HEAD_YAW_MIN, HEAD_YAW_MAX)
    head_pitch_position = clamp(head_pitch_position, HEAD_PITCH_MIN, HEAD_PITCH_MAX)
    shoulder_roll_position = clamp(shoulder_roll_position, RSHOULDER_ROLL_MIN, RSHOULDER_ROLL_MAX)
    shoulder_pitch_position = clamp(shoulder_pitch_position, RSHOULDER_PITCH_MIN , RSHOULDER_PITCH_MAX)
    
    
    head_yaw.setPosition(head_yaw_position)
    head_pitch.setPosition(head_pitch_position)
    
    RShoulder_Pitch.setPosition(shoulder_pitch_position)
    RShoulder_Roll.setPosition(shoulder_roll_position)
"""
    
    # Print distancce sensor values
    """value = distance_sensor_left.getValue()
    print("Left sensor value is: ", value)"""
    
    
    # Temporary Storage for Premade Functions
    

    

















