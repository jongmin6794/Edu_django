class Person():
    name = '사람의 고유한 속성'
    age = '출생 이후부터 삶을 마감할 때까지의 기간'

    def greeting(self):
        print(f'{self.name}이 인사합니다. 안녕하세요.')
    
    def eating(self):
        print(f'{self.name}은 밥을 먹습니다.')

    def aging(self):
        print(f'{self.name}은 {self.age}살이지만, 나이를 먹어가는 중입니다.')
    
# 클래스 - 사람(집단, 특성)
# 인스턴스 - 사람(개인)
# 메소드 - 사람(개인)이 가지고 있는 행위
# 클래스 변수 - 사람(집단, 특성)이 가지고 있는 공통 속성
# 인스턴스 변수 - 사람(개인)이 가지는 고유한 특성

jongmin = Person() # 인스턴스
print(jongmin.name) # 인스턴스 변수
print(jongmin.age)
jongmin.name = '종민'
jongmin.age = '31'
print(jongmin.name)
print(jongmin.age)
print(Person.name)
print(Person.age)
jongmin.eating()

justin = Person()
print(justin.name) #=> 사람의 고유한 속성
justin.name = '재석'
print(justin.name) #=> 재석
print(jongmin.name) #=> 종민
