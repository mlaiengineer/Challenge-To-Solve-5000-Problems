def fizz_buzz(n):
    arr_1_to_n = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            arr_1_to_n.append("FizzBuzz")
        elif i % 3 == 0:
            arr_1_to_n.append("Fizz")
        elif i % 5 == 0:
            arr_1_to_n.append("Buzz")
        else:
            arr_1_to_n.append(i)
    return arr_1_to_n

#test cases
print(fizz_buzz(2)) #1. fizz_buzz(2) should return [1, 2].
print(fizz_buzz(4)) #2. fizz_buzz(4) should return [1, 2, "Fizz", 4].
print(fizz_buzz(8)) #3. fizz_buzz(8) should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8]

#:4. fizz_buzz(20) should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz",
#"Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz"].
print(fizz_buzz(20))