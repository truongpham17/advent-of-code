import hashlib
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from util.file import read_file, write_file

exclusive_string = ['ab', 'cd', 'pq', 'xy']
vowel_string = 'aeiou'
def is_contain_bad_string(string: str):
  for not_allow in exclusive_string:
    if not_allow in string:
      return True
  return False

def has_more_three_vowel(string: str):
  vowel = []
  for char in string:
    if(char in vowel_string):
      vowel.append(char)   
      if(len(vowel)>=3):
        return True
  return False

def has_double_letter(string: str):
  for i in range(1, len(string)):
    if(string[i] == string[i-1]):
      return True
  return False

def is_nice_string(string: str):
  return (not is_contain_bad_string(string)) and has_double_letter(string) and has_more_three_vowel(string)
  
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
  
# print(is_nice_string("ugknbfddgicrmopn"))
# print(is_nice_string("aaa"))
# print(is_nice_string("jchzalrnumimnmhp"))
# print(is_nice_string("haegwjzuvuyypxyu"))
# print(is_nice_string("dvszwmarrgswjxmb"))