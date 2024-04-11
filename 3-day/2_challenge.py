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
  santa_pos = 0
  bot_pos = 0
  lucky_boy = {santa_pos}
  
  for i in range(len(input_text)):
    if(i % 2 == 0):
      santa_pos = move(santa_pos, input_text[i])
      lucky_boy.add(santa_pos)
    else:
      bot_pos = move(bot_pos, input_text[i])
      lucky_boy.add(bot_pos)
    
  write_file(__file__, len(lucky_boy))
  return len(lucky_boy)

print(who_is_lucky())