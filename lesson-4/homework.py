# list1 = [1, 1, 2]
# list2 = [2, 3, 4]
# result = []
# for x in list1:
  #  if x not in list2:
   #     result.append(x)
# for x in list2:
  #  if x not in list1:
   #     result.append(x)
# print(result)
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = []
# for x in list1:
  #  if x not in list2:
   #     result.append(x)
# for x in list2:
  #  if x not in list1:
   #     result.append(x)
# print(result)
# list1 = [1, 1, 2, 3, 4, 2]
# list2 = [1, 3, 4, 5]
# result = []
# for x in list1:
 #   if x not in list2:
  #      result.append(x)
# for x in list2:
  #  if x not in list1:
   #     result.append(x)
# print(result)
# n = 5
# for i in range(1, n):
#    print(i ** 2)
import random
while True:
    number = random.randint(1, 100)
    for attempt in range(10):
        guess = int(input("Enter your guess: "))
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("You guessed it right!")
            break
    else:
        answer = input("Do you want to play again?  ")
        if answer in ["Y", "Yes", "y", "yes", "ok"]:
            continue
        else:
            break