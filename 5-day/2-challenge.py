import hashlib
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from util.file import read_file, write_file


def is_appear_twice(string: str):
  for i in range(0, len(string)-2):
    for j in range(i+2, len(string)-1):
      if(string[i] + string[i+1] == string[j] + string[j+1]):
        return True
  return False

def is_zig_zag(string: str):
  for i in range(0, len(string) - 2):
    if(string[i] == string[i+2]):
      return True
  return False

def is_nice_string(string: str):
  return is_appear_twice(string)and is_zig_zag(string)
  
def nice_string_count():
  input_text = read_file(__file__)
  inputs = input_text.split("\n")
  nice_count = 0
  for string in inputs:
    if is_nice_string(string):
      nice_count += 1
  write_file(__file__, str(nice_count))
  return nice_count

nice_string_count()

# print(is_nice_string("qjhvhtzxzqqjkmpb"))
# print(is_nice_string("xxyxx"))
# print(is_nice_string("uurcxstgmygtbstg"))
# print(is_nice_string("ieodomkazucvgmuy"))