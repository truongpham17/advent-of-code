from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))

from enum import Enum
from util.file import read_file, write_file

def square_feet_of_wrapping_paper():
  input_text = read_file(__file__)
  presents = input_text.split('\n')
  min_wrap = 0
  for present in presents:
    [l, w, h] = list(map(int,present.split('x')))
    require_area = l*w*h + (l+w+h - max(l,w,h))*2
    min_wrap = min_wrap + require_area
  write_file(__file__, min_wrap)
  return min_wrap

print(square_feet_of_wrapping_paper())
