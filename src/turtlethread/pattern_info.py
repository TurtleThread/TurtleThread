import math

from pyembroidery import JUMP, STITCH, TRIM


def get_pattern_info(pattern):
    """Construct a dictionary with information about an embroidery pattern

    Parameters
    ----------
    pattern : pyembroidery.EmbPattern

    Returns
    -------
    dict
        Dict with information
    """
    info = {
        "num_jumps": 0,
        "num_stitches": 0,
        "num_trims": 0,
        "x_min": float("inf"),
        "x_max": -float("inf"),
        "y_min": float("inf"),
        "y_max": -float("inf"),
        "closest_subsequent_stitches": float("inf"),
    }
    min_squared_distance = float("inf")
    prev_x, prev_y, prev_command = None, None, None
    for x, y, command in pattern.stitches:
        if command == JUMP:
            info["num_jumps"] += 1
        if command == STITCH:
            info["num_stitches"] += 1
        if command == TRIM:
            info["num_trims"] += 1

        if x < info["x_min"]:
            info["x_min"] = x
        if x > info["x_max"]:
            info["x_max"] = x

        if y < info["y_min"]:
            info["y_min"] = y
        if y > info["y_max"]:
            info["y_max"] = y

        if prev_command is None or command != prev_command or command != STITCH:
            prev_x, prev_y, prev_command = x, y, command
            continue

        squared_distance = (x - prev_x) ** 2 + (y - prev_y) ** 2
        min_squared_distance = min(min_squared_distance, squared_distance)
        prev_x, prev_y, prev_command = x, y, command
    info["closest_subsequent_stitches"] = math.sqrt(min_squared_distance)
    return info


def show_info(pattern, scale=1):
    """Display information about an embroidery pattern

    Parameters
    ----------
    pattern : pyembroidery.EmbPattern
    """
    pattern_info = get_pattern_info(pattern)
    width = abs(pattern_info["x_max"] - pattern_info["x_min"])
    height = abs(pattern_info["y_max"] - pattern_info["y_min"])

    info_fields = (
        width + 1,
        height + 1,
        pattern_info["num_stitches"] + 1,
        pattern_info["num_jumps"] + 1,
        pattern_info["num_trims"] + 1,
    )
    num_digits = int(max(map(math.log, info_fields)))
    closest_stitches = pattern_info["closest_subsequent_stitches"] / 10
    print(f"{'Pattern info':>{25 + num_digits}}")
    print("-" * (25 + num_digits + 3))
    print(f"{'Width [steps]':>25} | {width/scale:{num_digits}.0f}")
    print(f"{'Height [steps]':>25} | {height/scale:{num_digits}.0f}")
    print(f"{'Width [mm]':>25} | {width/10:{num_digits}.0f}")
    print(f"{'Height [mm]':>25} | {height/10:{num_digits}.0f}")
    print(f"{'Min distance between':>25} |")
    print(f"{'subsequent stitches [mm]':>25} | {closest_stitches:{num_digits}.0f}")
    print(f"{'Number of stitches':>25} | {pattern_info['num_stitches']:{num_digits}.0f}")
    print(f"{'Number of jumps':>25} | {pattern_info['num_jumps']:{num_digits}.0f}")
    print(f"{'Number of trims':>25} | {pattern_info['num_trims']:{num_digits}.0f}")
