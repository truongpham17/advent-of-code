import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from util.file import read_file, write_file

def move(position, direction):
  directions = {
    '<': -1,
    '>': 1,
    '^': -1000,
    'v': 1000
  }
  return position + directions[direction]
    
def who_is_lucky():
  input_text = read_file(__file__)
  cur_pos = 0
  lucky_boy = {cur_pos}
  
  for char in input_text:
    cur_pos = move(cur_pos, char)
    lucky_boy.add(cur_pos)
    
  write_file(__file__, len(lucky_boy))
  return len(lucky_boy)

print(who_is_lucky())