from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))

from enum import Enum
from util.file import read_file, write_file

class Direction(str, Enum):
  UP = '('
  DOWN = ')'

def not_quite_lisp():
  input_text = read_file(__file__)
  floor = 0
  for char in input_text:
    if char == Direction.UP:
      floor = floor + 1
    elif char == Direction.DOWN:
      floor = floor - 1
  write_file(__file__, floor)
  print(floor)

not_quite_lisp()