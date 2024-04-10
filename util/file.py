import os

fileDir = os.path.dirname(__file__)

def read_file(path):
  path = os.path.join(os.path.dirname(path), 'input')
  input_file = open(os.path.join(os.path.dirname(path), 'input'))
  input_text = input_file.read()
  return input_text
  
def write_file(path, output):
  output_file = open(os.path.join(os.path.dirname(path), 'output'),'w')
  output_file.write(str(output))
  output_file.close()
 