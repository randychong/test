### Exercise #1 - List Practice

ogAvengers = ["Captain America", "Thor", "Iron Man", "Black Widow", "Hulk"]

# Add the missing Avenger(s)
# Delete Iron Man from the Avengers #RIPTony
# Insert a new member of the Avengers (whoever you want -Bob Ross, yourself etc.-) between Captain America and Thor

# ogAvengers.append("Hawkeye")
# del ogAvengers[2]
# print(ogAvengers)


### Exercise #2 - FizzBuzz Part 2

# In your terminal, print the range of numbers from 1 to 100
# For every number that is divisible by 3, you want to replace it with the word "Fizz"
# For every number that is divisible by 5, you want to replace it with the word "Buzz"
# For every number that is divisible by 3 and 5, you want to replace it with the word "FizzBuzz"
# Example: it'll read like "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz" and so on
# Use what has been covered plus some research (don't google FizzBuzz lol)

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

### Exercise #3 - Moving Zeroes

#Given an array of numbers, write a function to move all zeroes to the end of it while maintaining the relative order of 
#the non-zero elements.

# array1 = [0,1,0,3,12]
# array2 = [1,7,0,0,8,0,10,12,0,4]

# def solution(nums):
#     for i in nums:
#         if 0 in nums:
#             nums.remove(0)
#             nums.append(0)
#     return nums

# print(solution(array1))
# print(solution(array2))

# Output:
# [1, 3, 12, 0, 0]
# [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]