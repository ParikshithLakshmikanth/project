num = input("Enter a number: ")
sum = 0
n = len(num)

for i in num:
    no = int(i)
    sum += no**n

if sum == int(num):
    print("Armstrong Number")
elif sum != int(num):
    print("Not an Armstrong Number")