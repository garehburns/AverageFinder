"""
nums = float(input("Enter numbers you want averaged: "))
result = str((sum(nums)) / len(nums))
print("The average is " + result)
"""

'''
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
average = str((num1 + num2) / 2)
print ("The average is " + average)
'''


nums = (input("Enter numbers you want averaged, separated by a comma: "))
average = int(sum(nums) / len(nums))
print (average)