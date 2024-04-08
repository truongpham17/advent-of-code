from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))

from enum import Enum
from util.file import read_file, write_file

class Direction(str, Enum):
  UP = '('
  DOWN = ')'
BASEMENT = -1
def not_quite_lisp():
  input_text = read_file(__file__)
  floor = 0
  for i in range(0, len(input_text)):
    char = input_text[i]
    if char == Direction.UP:
      floor = floor + 1
    elif char == Direction.DOWN:
      floor = floor - 1
    if floor == BASEMENT:
      write_file(__file__, i + 1)
      print(i + 1)
      return

not_quite_lisp()