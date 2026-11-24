#파이썬은 배열이 없고 리스트 존재
total = 0
for quantity in [1,0,3]:
    if quantity == 0:
        continue
    total += quantity
print(total)

attemps = 0
while attemps <3:
    attemps += 1
    if attemps == 2:
        break
print(attemps)

#range는 초기값은 포함하고 끝값은 제외 ex) range(a,d) = [a,b,c]
total1 = 0
for number in range(1,5):
    if number % 2 != 0:
        continue
    total1 += number
print(total1)