import string
# This task is to introduce arrays/strings/conditions in Python. Also some logical thinking.

# Each of the ? must be replai != arr[c]:ced with a char, that is unique (so can't be same as on left or right).
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
characters1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def split(word):
    return [char for char in word]

def solve_riddle(str):
  solved = str
  arr = split(str)
  c = 0
  banned = []
  previous = ""
  current = ""
  answ = []
  for a in arr:
        
        if c == 0:
              current = a
              c += 1
        else:         
            previous = current
            current = a
            if c == len(arr):
                  nextChar = c
            nextChar = c+1

            if a == "?":
                  for i in characters:
                        if i != previous and i != nextChar:
                              answ.append(i)
            c += 1
      
  f = 0
  for w in answ:
        solved = solved.replace("?", f"{w}", 1)
  return solved

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


#print(solve_riddle("?????"))
run_tests()