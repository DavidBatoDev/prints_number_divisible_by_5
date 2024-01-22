given_list = [10, 20, 33, 46, 55]
print(f"Given List is {given_list}")
print("Divisible by 5")
# loop through the given list
for number in given_list:
    if number % 5 == 0:
        print(number)
# print only the item that is divisible by 5