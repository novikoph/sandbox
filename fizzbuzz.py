for i in range(1, 101):
    if i % 15 == 0:
        print('{} FizzBuzz'.format(i))
    elif i % 5 == 0:
        print('{} Buzz'.format(i))
    elif i % 3 == 0:
        print('{} Fizz'.format(i))
    else:
        print(i)