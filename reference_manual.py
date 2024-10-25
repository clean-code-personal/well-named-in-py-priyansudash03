from color_utils import get_color_from_pair_number

def generate_reference_manual():
    manual = []
    for pair_number in range(1, 26):
        major_color, minor_color = get_color_from_pair_number(pair_number)
        manual.append(f'{pair_number}: {major_color} - {minor_color}')
    return manual

def print_reference_manual():
    manual = generate_reference_manual()
    print("Color Code Reference Manual")
    print("---------------------------")
    for line in manual:
        print(line)

