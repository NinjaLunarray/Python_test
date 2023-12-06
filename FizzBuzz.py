
class FizzBuzz:
    def isFizz(self, n):
        return n % 3 == 0
    
    def isBuzz(self, n):
        return n % 5 == 0
    
    def isFizzBuzz(self, n):
        return n % 15 == 0
    
    def answer(self,n):
        if self.isFizzBuzz(n):
            return 'FizzBuzz'

        elif self.isFizz(n):
            return 'Fizz'

        elif self.isBuzz(n):
            return 'Buzz'

        return n
    
for x in range (1, 101):
    print(FizzBuzz().answer(x))