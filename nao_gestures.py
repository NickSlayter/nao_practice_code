
def neutral_pose():
    return{
        # Reset all motor poisitions to the neutral position

        "RPhalanx1_position" : 0.0,
        "RPhalanx2_position" : 0.0,
        "RPhalanx3_position" : 0.0,
        "RPhalanx4_position" : 0.0,
        "RPhalanx5_position" : 0.0,
        "RPhalanx6_position" : 0.0,
        "RPhalanx7_position" : 0.0,
        "RPhalanx8_position" : 0.0,
        "RShoulderPitch" : 1.8,
        "RShoulderRoll" : 0.0, 
        "HeadYaw" : 0.0,
        "HeadPitch" : 0.0
    }


def point_up_right():

    return{
        # Set finger gesture    
        "RPhalanx1_position" : 0.0,
        "RPhalanx2_position" : 0.0,
        "RPhalanx3_position" : 0.0,
        "RPhalanx4_position" : 1.0,
        "RPhalanx5_position" : 1.0,
        "RPhalanx6_position" : 1.0,
        "RPhalanx7_position" : 1.0,
        "RPhalanx8_position" : 0.0,

        # Set Shoulder Posistion
        "RShoulderPitch" : -0.21,
        "RShoulderRoll" : -0.43,
        
        # Set Head Position 
        "HeadYaw" : -0.58,
        "HeadPitch" : -0.13
    }