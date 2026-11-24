total = 0
for number in range(1,11):
    if number % 2 !=0:
        continue
    total += number
print(total)
print("--------------------------------------")

total1 = 0
for number in range(1,11):
    if number % 2 !=1:
        continue
    total1 += number
print(total1)
print("--------------------------------------")

evennum = 0
while evennum < 11:
    evennum += 1
    if evennum % 2 == 0:
        print(evennum)
        

print("--------------------------------------")

oddnum = 0
while oddnum < 11:
    oddnum += 1
    if oddnum % 2 == 1:
        print(oddnum)
        
