class MaxStack:
  def __init__(self):
      self.__max=-9999
      self.__stack=[]

  def push(self, val):
      if val>self.__max:
          self.__max=val
      self.__stack.append(val)
  def pop(self):
      self.__stack.pop()

  def max(self):
    return self.__max

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2