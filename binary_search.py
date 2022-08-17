def binary_search(numbers, item):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        half = int((low + high) / 2)
        guess = numbers[half]
        if guess == item:
            return half
        if guess > item:
            high = half - 1
        else:
            low = half + 1
    return None


my_numbers = [14, 45, 66, 98, 114, 115, 170, 201, 256, 301, 332, 350, 402, 405]

print(binary_search(my_numbers, 170))

print(binary_search(my_numbers, 400))
