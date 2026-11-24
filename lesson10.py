values = [2,0,3]
totals = [n * 8000 for n in values if n > 0]
report = {str(i + 1): values for i, value in enumerate(totals)}

print(totals)
print(report)

try:
    quantity = int("ABC")
except ValueError:
    print("정수를 입력하세요")