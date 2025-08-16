def fizzbuzz(start, end):
    divisors = [(3, "fizz"), (4,"buzz")]

    for i in range(start, end):
        result = "".join(word for divisor, word in divisors if i % divisor == 0)
        print(result or i)

fizzbuzz(0,100)
