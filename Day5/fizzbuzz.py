for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        number = print("Fizzbuzz")
    elif number % 3 == 0:
        number = print("Fizz")
    elif number % 5 == 0: 
        number = print("Buzz")
    else:
        print(number)