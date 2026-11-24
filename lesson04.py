# 파이썬 bool형은 조건식때 무조건 대문자
# 자바와 달리 경계값은 :(콜론으로) 종속은 {}를 쓰지 않고 들여쓰기(tap)
total = 30000
is_member = False

if total <0:
    message = "금액 오류"
elif total >= 30000 or is_member:
    message = "무료배송"
else :
    message = "배송비 3000원"

print(message)