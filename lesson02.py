price = 12000
quantity = 3
discount_rate = 0.1
product = "노트"
is_member = True
subtotal = price * quantity
print(product,subtotal)
# __ 2개 더블 언더바 = 던더
print(type(price).__name__,type(discount_rate).__name__)
print(subtotal >= 30000, is_member)
# 파이썬의 나눗셈은 실수 지원 자바처럼 정수만 나오게 할려면 // 2개
print(7/2 , 7//2 , 7%2)