items = ["book","pen","bag"]
#자바와 다르게 음수 인데스 가능함
print(items[0],items[-1])
print(items[1:3])

#.append 리스트 저장공간에 값 추가
# 자바와 다르게 공간 추가 가능 
items.append("cup")
items[0] = "note"
print(items)

point = (10,20)
x,y = point
print(point)