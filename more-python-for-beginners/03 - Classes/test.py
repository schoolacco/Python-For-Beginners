
class test():
    def input(var1, var2):
        var1 = int(input("Num1: "))
        return var1
    def __innit__(self, var1, var2):
        self.var1 = var1
        if int(var2) == var2:
           self.var1 = var2/var1
        return var2
    def idk(self, var2):
        self = self + var2
        print(self)
class Class(test):
   def __innit__(self, var1, var2):
      self.var1 = var1
      self.var2 = var2
   def Function(self):
      print(test.var1)

      
a = None
b = None
class Code():
  def code():
    global a
    global b
    a = test.input2(a,b)
    while True:
      try:
        test.var1 = int(input("Num2: "))
        break
      except:
        print("Input was not an integer")
        pass
    b = test.var1
    test.idk(a,b)
    print(issubclass(Class, test))
