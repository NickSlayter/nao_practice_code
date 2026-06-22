from nao_helpers import clamp
import nao_constants as const
def get_sound_direction(key):
    """
    Returns:
        azimuth: left/right direction in radians
        elevation: up/down direction in radians
        confidence: reliability from 0.0 to 1.0
    """

    test_directions = {
        "Left" : (0.5, 0.0, 0.9),
        "Right" : (-0.5, 0.0, 0.9),
        "Up" : (0.0, 0.5, 0.9),
        "Down" : (0.5, -0.5, 0.9),
        "Up Left" : (0.5, 0.5, 0.9),
        "Up Right" : (-0.5, 0.5, 0.9),
        "Down Left" : (0.5, -0.5, 0.9),
        "Down Right" : (-0.5, -0.5, 0.9),
        "Unconfident" : (0.5, 0.5, 0.2),
        "Excessive" : (1.0, 1.0, 0.9)
    }

    return test_directions[key]
    pass


def look_toward_sound(azimuth, elevation, current_yaw, current_pitch):
    """
    Move NAO's head toward the sound.
    """
    raw_target_yaw = azimuth + current_yaw
    raw_target_pitch = current_pitch - elevation

    safe_target_yaw = clamp(
        raw_target_yaw,
        const.HEAD_YAW_MIN,
        const.HEAD_YAW_MAX
    )
    safe_target_pitch = clamp(
        raw_target_pitch, 
        const.HEAD_PITCH_MIN, 
        const.HEAD_PITCH_MAX
    )

    return safe_target_yaw, safe_target_pitch



    pass


def main_loop():
    azimuth, elevation, confidence = get_sound_direction()

    if confidence > 0.6:
        look_toward_sound(azimuth, elevation)