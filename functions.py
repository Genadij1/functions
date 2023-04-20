import random
def most_frequent(numbers):
    count = {}
    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    max_count = max(count.values())
    most_frequent_nums = [k for k, v in count.items() if v == max_count]
    return min(most_frequent_nums)
numbers = [random.randint(1, 100) for _ in range(100)]
print(numbers)
most_frequent(numbers)
print(most_frequent(numbers))
