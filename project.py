import sys
import json
#코드 가독성 정리 해봤습니다
def quote(price, quantity,shipping=3000):
    total = price * quantity
    return total + shipping

def sum_values(*args):
    return sum(args)

def profile(**kwargs):
    return kwargs

items = [("book",12000),
         ("note",8000),
         ("pen",1500),
         ("bag",25000),
         ("cup",6000)]

owned_items = {"book","pen"}
wish_items = {"pen","bag"}
memos = []
orders = []
total_price = 0

print("[파이썬 콘솔 애플리케이션]", " [수업시간]:",60)
print("[실행기 정보]:",sys.executable)

while True:
    print("======= 파이썬 스마트 스토어 & 학습 매니저 =======")
    print("1. 상품 목록 보기")
    print("2. 주문 담기 및 견적 계산")
    print("3. 수량 일괄 정산 리포트")
    print("4. 보유 vs 관심 상품 비교")
    print("5. 주문 내역 JSON 저장 및 불러오기")
    print("6. 회원 프로필 / 추가 메모 등록") 
    print("0. 종료")
    print("=================================================")
    name = input("메뉴 선택:").strip()
    
    if name == "1":
        print("==================================================")
        print("가격이 비싼 순 정렬")
        print(sorted(items,key=lambda item:item[1], reverse= True))
        print("※ 최고가 상품※")
        print(items[3])
        print("※ 추천 TOP3※")
        print(items[:3])
        print("==================================================")
    
    elif name == "2":
        print("==================================================")        
        username = input("사용자이름:").strip()
        # is_member = input("회원 여부[y / n] : ").strip() =="y"==True 
        # 로 줄여봤으나 가격 3만원과 회원 y를 충족했으나 Ture가 아닌
        # false 구문인 배송비 3천원이 계속 나왔음
        # 따라서 롤백
        is_member = input("회원 여부[y / n] : ").strip() 

        if is_member == "y":
            is_member = True
        else :
            is_member = False 
        
        callitems = input("주문 할 상품들:").strip()
        raw_quantity = input("수량:").strip()
        
        try : 
            quantity = int(raw_quantity)
            if quantity <= 0:
                print("0보다 큰 값을 적으세요")
                continue
        except ValueError:
            print("정수를 입력하세요")
            continue
        
        price_map = {"book":12000,
                     "note":8000,
                     "pen":1500,
                     "bag":25000,
                     "cup":6000}
                
        pick = [n.strip() for n in callitems.split(",") if n.strip()]
        #공백방지
        if not pick:
            print("상품을 입력하세요")
            continue
        
        unit_price = 0

        for p in pick:
            if p in price_map:
                unit_price += price_map[p]
            else:
                print("없는 상품입니다")
                unit_price = 0
                break
        
        total = unit_price * quantity
        #아 없는 상품 넣어도 배송비가 나오는 이유를 모르겠다.
        #왜 브레이크가 작동 안하지
        if total >= 30000 and is_member :
            final_price = quote(unit_price,quantity,shipping=0)
            print(final_price)
            print("무료배송")
        else:
            final_price = quote(unit_price,quantity,shipping=3000)
            print(final_price)
            print("배송비 3000원")
        
        orders.append({"사용자":username,
                       "상품":pick,
                       "수량":quantity,
                       "결제금액":final_price})
        # order("결제금액") 오류 고침 리스트에서 가져오는거라 []써야되는데 ()썼었음
        amount = (order["결제금액"] for order in orders)
        total_price = sum_values(*amount)         

        print(f"주문상품:{callitems.split(",")},수량:{raw_quantity}")
        print(f"주문 금액:{total}원")
        print("==================================================")
    
    elif name == "3":
        print("==================================================")
        values = [2,3,0,-1,1]
        totals = [n * 8000 for n in values if n > 0]
        report = {str(i + 1):values for i, values in enumerate(totals)}
        print("수량 일괄 정산 리포트")
        print(report,sum(totals))       
        print("==================================================")
    
    elif name == "4":
        print("==================================================")
        print("보유하신 상품:",owned_items)
        print("관심있는 상품:",wish_items)
        print("※ 보유 상품vs 관심상품 비교※")
        print("교집합:",sorted(owned_items & wish_items))
        print("차집합:",sorted(owned_items - wish_items))
        print("합집합:",sorted(owned_items | wish_items))
        print("==================================================")
    
    elif name == "5":
        print("==================================================")
        list = {"주문건수":len(orders),"누적금액":total_price,"주문내역":orders}
        text = json.dumps(list,ensure_ascii=False)
        loaded = json.loads(text)
        print(text)
        print("==================================================")
    
    elif name == "6":
    # 추가된 메모가 마지막에서만 프린트 되는 것을 처음에 memo의 리스트 memos 나오게해서
    # 쓴 메모들 확인할 수 있게 추가
        print("==================================================")
        print("※ 회원정보 조회※")       
        print(profile(name = "형민" , level = "basic", member = "Bronze"))
        print(memos)
                
        x,y = (10,20) 
        print("※ 매장 좌표※")
        print(x,y)
        
        memo = input("추가 메모 등록:").strip()        
        if memo:
            memos.append(memo)
        print(memo,"가 추가되었습니다")
        print("==================================================")            
    
    elif name == "0":
        print("정상적으로 종료되었습니다")
        break
    
    else :
        print("잘못된 입력입니다")
        
        


