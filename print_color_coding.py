from constants import MAJOR_COLORS, MINOR_COLORS

def print_color_coding_reference():
    print("Color Coding Reference Manual:")
    print("------------------------------")
    print("Pair Number | Major Color | Minor Color")
    print("---------------------------------------")
    pair_number = 1
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            print(f"{pair_number:>11} | {major_color:<11} | {minor_color}")
            pair_number += 1
