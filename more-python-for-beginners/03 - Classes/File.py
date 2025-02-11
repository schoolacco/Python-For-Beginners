import random
import time
class File():
  def intlist():
    num = 0
    while True:
      num += 1
      stream = open("test"+str(num)+'.txt', 'w')
      listtest = []
      for i in range(random.randint(1,99)):
        var = random.randint(0,9)
        listtest.append(str(var))
      if stream.writable():
        stream.write('\n')
        stream.writelines(['test','','','test'])
        stream.write('\n')
        stream.writelines(listtest)
        if stream.readable():
          stream.read()
        time.sleep(0.1)
        pass
      if num == 10:
        break
    stream.close
  def read():
    stream = open("demo.txt", "r")
    if stream.readable():
      print(stream.read())
    stream.close
  def create():
    num = 0
    while True:
      try:
        stream = open("Output"+str(num)+".py", "x")
        while True:
         if stream.writable():
          stream.write(input("Test: "))
          stream.write("\n")
         if input("End?: ").lower() == "true":
          stream.close()
          break
        break
      except:
        if num == None:
          num = 0
        num += 1
  