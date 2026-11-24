import json

a = {"english","french","china","japan"}
b = {"korean","spanish","china","japan"}
print(sorted(a & b))
print(sorted(a - b))

student = {"name": "형민","subject":sorted(a | b)}
student.get("random","미입력")
text = json.dumps(student,ensure_ascii=False)
print(json.loads(text))