lower = int(input("lower range: "))
upper = int(input("upper range: "))
for num in range(lower,upper + 2):
    sum=1
temp = num
while temp > 0:
 digit = temp % 10
sum += digit ** 2
temp //= 10
if num == sum:
     print(num is)
