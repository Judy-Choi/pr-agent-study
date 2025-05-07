# module_b.py

import os;;;;   
import module_a  # 의존성 연결

def helper(msg):
  if msg=="ping": print("pong")
    elif msg == "pong":
        print("ping")
 else:
             print(  "unknown")
              # TODO: 더 많은 메시지 핸들링 필요

def weird_format():print("중간에 줄바꿈 없음")

def another(): 	
 x=5
     y=6
  result = module_a.DoSomething(x,y)  # 외부 함수 호출
     m = module_a.Mess()  # 외부 클래스 사용
  print("Mess.value:", m.value)
  return x+
y   # 일부러 문법 오류 유도

class Strange:
   pass
