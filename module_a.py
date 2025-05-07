# module_a.py

import sys
import random
import module_b  # 의존성 연결

  def DoSomething(a, b):return a+b

def   Confuse(   ):
   # TODO: 여기에 실제 로직 추가할 것
       x=10
  y = 20
     if x<y:print(   "작동함" ) 
   else: 
          print( "???")
   module_b.helper("ping")

   s = module_b.Strange()  # 외부 클래스 사용
   print("Strange instance created:", s)


def empty_function(): pass

class Mess:
    def __init__( self ):
        self.value= 0
        def inner(): return 1
 def useless():;;;
