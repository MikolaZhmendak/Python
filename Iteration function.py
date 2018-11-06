# iterator example that uses iter and next methods to print numbers from 1 to 10.

class Numbers:
   def _iter_(self):
      self.a = 1
      return self


   def _next_(self):
       x = self.a
       self.a  += 1
       retrun x



       myclass = Numbers()
       myiter = iter(myclass)



       print(next(myiter))
       print(next(myiter))
       print(next(myiter))
       print(next(myiter))
       print(next(myiter))
       print(next(myiter))
       print(next(myiter))
       print(next(myiter))
       print(next(myiter))
       print(next(myiter))