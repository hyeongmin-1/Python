raw_score = input("성적 입력:").strip()
score = int(raw_score)


if score > 100 or score < 0:
    message = "알맞은 성적을 넣어주세요"
elif score >= 90:
    message = "성적 : A"
elif score >= 80:
    message = "성적 : B"
else :
    message = "성적 : C"

print(message)