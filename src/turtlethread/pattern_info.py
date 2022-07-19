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
    }
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
    print(f"{'Pattern info':>{20 + num_digits}}")
    print("-" * 30)
    print(f"{'Width [steps]':>20} | {width/scale:{num_digits}.0f}")
    print(f"{'Height [steps]':>20} | {height/scale:{num_digits}.0f}")
    print(f"{'Width [mm]':>20} | {width/10:{num_digits}.0f}")
    print(f"{'Height [mm]':>20} | {height/10:{num_digits}.0f}")
    # TODO: print(f"{'Minimum distance between stitches':>40} | {pattern_info[mind_distance]}")
    print(f"{'Number of stitches':>20} | {pattern_info['num_stitches']:{num_digits}.0f}")
    print(f"{'Number of jumps':>20} | {pattern_info['num_jumps']:{num_digits}.0f}")
    print(f"{'Number of trims':>20} | {pattern_info['num_trims']:{num_digits}.0f}")
