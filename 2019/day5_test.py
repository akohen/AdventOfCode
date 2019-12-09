from unittest import TestCase, main
from day5 import intcode_computer

class TestDay(TestCase):
  def test_eq_position_mode(self):
    result = intcode_computer([3,9,8,9,10,9,4,9,99,-1,8],[6]).execute().output_values[0]
    self.assertEqual(result,0)

  def test_lt_position_mode(self):
    result = intcode_computer([3,9,7,9,10,9,4,9,99,-1,8],[6]).execute().output_values[0]
    self.assertEqual(result,1)

  def test_longer_program(self):
    result = intcode_computer([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],[6]).execute().output_values[0]
    self.assertEqual(result,999)

if __name__ == '__main__':
  main()