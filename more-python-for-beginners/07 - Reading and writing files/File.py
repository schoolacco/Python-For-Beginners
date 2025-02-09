import random
import time
num = 0
while True:
  num += 1
  stream = open("test"+str(num)+'.txt', 'wt')
  listtest = []
  for i in range(5):
    var = random.randint(1,9)
    listtest.append(str(var))
  if stream.writable():
    stream.write('\n')
    stream.writelines(['test','','','test2'])
    stream.writelines(listtest)
    time.sleep(1)
    pass
  if num == 100:
    break
  stream.close