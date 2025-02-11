from test import test
from test import Code
from File import File
a = b = None
while True:
  var = input("Command: ").lower()
  if var == "test":
    test.input(a,b)
    Code.code()
    break
  elif var == "random":
    File.intlist()
  elif var == "read":
   File.read()
  elif var == "create":
    File.create()
  elif var == "end":
    break