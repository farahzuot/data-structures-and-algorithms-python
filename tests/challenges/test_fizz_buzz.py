from data_structures_and_algorithms.challenges.fizz_buzz_tree.fizz_buzz_tree import FizzBuzzTree

def test_fizz_buzz():
    actual = FizzBuzzTree([1,2,4,5,3,4,9,5,2,3,15])
    expected = ['1', '2', '4', 'Buzz', 'Fizz', '4', 'Fizz', 'Buzz', '2', 'Fizz', 'FizzBuzz']

    assert actual == expected