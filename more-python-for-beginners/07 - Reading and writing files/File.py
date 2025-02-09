import random
import time
num = 0
while True:
  num += 1
  stream = open("test"+str(num)+'.txt', 'wt')
  listtest = []
  for i in range(random.randint(1,99)):
    var = random.randint(0,9)
    listtest.append(str(var))
  if stream.writable():
    stream.write('\n')
    stream.writelines(['test','','','test'])
    stream.write('\n')
    stream.writelines(listtest)
    time.sleep(0.1)
    pass
  if num == 10:
    break
  stream.close