from constants import MAJOR_COLORS, MINOR_COLORS
from color_utils import get_color_from_pair_number, get_pair_number_from_color
from test_color_code import test_number_to_pair, test_pair_to_number
from print_color_coding import print_color_coding_reference

if __name__ == '__main__':
  test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number('Red', 'Orange', 7)
  print('Done :)')

print_color_coding_reference()
