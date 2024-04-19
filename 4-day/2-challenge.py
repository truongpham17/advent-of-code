import hashlib
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from util.file import read_file, write_file

def find_hash():
  input_text = read_file(__file__)
  cur_number = 0
  while(True):
    str2hash = input_text + str(cur_number)
    if(hashlib.md5(str2hash.encode()).hexdigest().startswith('000000')):
      write_file(__file__, str(cur_number))
      return cur_number
    cur_number += 1
  
find_hash()