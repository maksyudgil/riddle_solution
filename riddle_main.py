# This task is to introduce arrays/strings/conditions in Python. Also some logical thinking.

# Each of the ? must be replaced with a char, that is unique (so can't be same as on left or right).

def solve_riddle(str):
  # Please enter your solution here
  # ...
  return str


def run_tests():
  is_correct_solution(solve_riddle("abc?def"))
  is_correct_solution(solve_riddle("abc?de?????"))
  is_correct_solution(solve_riddle("??????"))

def is_correct_solution(solved_str):
  if "?" in solved_str:
    raise RuntimeError("Solution can't contain ?, but was '" + solved_str + "'")
  
  for i in range(len(solved_str)-1):
    if solved_str[i] == solved_str[i+1]:
      raise RuntimeError("Solution can't contain 2 same chars next to eachother, but was '" + solved_str + "'")

run_tests()      