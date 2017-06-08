ml = [5,9,3,6,8,11,4,3]

ml.sort()

ml


class MyList(list):
    def remove_min(self):
        self.remove(min(self))
    def remove_max(self):
        self.remove(max(self))




x = [5,2,9,11,10,2,7]
min(x)
max(x)
x.remove(10)
x

x = [10,3,5,1,2,7,6,4,8]
y = MyList(x)

dir(x)
dir(y)

y.remove_min()
y

y.remove_max()
y

class NewList(list):
   def remove_max(self):
     self.remove(max(self))
   def append_sum(self):
     self.append(sum(self))

x = NewList([1,2,3])
while max(x) < 10:
   x.remove_max()
   x.append_sum()
print(x)