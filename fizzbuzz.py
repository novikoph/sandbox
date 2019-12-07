for i in range(1, 101):
    if i % 15 == 0:
        print('{0} FizzBuzz'.format(i))
    elif i % 5 == 0:
        print('{0} Buzz'.format(i))
    elif i % 3 == 0:
        print('{0} Fizz'.format(i))
    else:
        print(i)