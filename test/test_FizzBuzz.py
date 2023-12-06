from FizzBuzz import FizzBuzz

def test_1_gives_1():
    assert FizzBuzz().answer(1) == 1

def test_2_gives_2():
    assert FizzBuzz().answer(2) == 2

def test_3_gives_Fizz():
    assert FizzBuzz().answer(3) == 'Fizz'

def test_5_gives_Buzz():
    assert FizzBuzz().answer(5) == 'Buzz'

def test_15_gives_FizzBuzz():
    assert FizzBuzz().answer(15) == 'FizzBuzz'

def test_mutiple_of_3_gives_Fizz():
    assert FizzBuzz().answer(99) == 'Fizz'

def test_mutiple_of_5_gives_Buzz():
    assert FizzBuzz().answer(95) == 'Buzz'

def test_mutiple_of_15_gives_FizzBuzz():
    assert FizzBuzz().answer(60) == 'FizzBuzz'

