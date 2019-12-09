from unittest import TestCase, main
from intcode_computer import intcode_computer
import day7

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

  def test_day7(self):
    result = intcode_computer([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0],[4, 5432]).execute().output_values[0]
    self.assertEqual(result,54321)

  def test_day7_phase1(self):
    with open('./input/day7') as f:
      result = day7.find_max([int(i) for i in next(f).split(',')], [0, 1, 2, 3, 4])
      self.assertEqual(result, 225056)

  def test_day7_phase2(self):
    with open('./input/day7') as f:
      result = day7.find_max([int(i) for i in next(f).split(',')], [5, 6, 7, 8, 9])
      self.assertEqual(result, 14260332)

if __name__ == '__main__':
  main()