# .strip()은 문자열 양끝 공백 제거 메서드
# 자바의 trim()
#input은 자바의 scanner.nextLine()
name = (input("이름:")).strip()
raw_quantity = input("수랑:")
quantity = int(raw_quantity)
total = quantity * 8000

print(f"{name}님, 총액:{total:,}원")
print("book,pen".split(","))