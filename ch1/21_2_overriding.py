# 클래스 예시, 상속, 오버라이딩, 스페셜 메소드

class KoreaUniv:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    def entrance(self):
        self.ent_year = self.number[:4]
    
    def graduation(self, year):
        pass

class College(KoreaUniv):
    def __init__(self, name, number, department):
        super().__init__(name, number)
        self.department = department
    
    def graduation(self, year):
        self.entrance()
        print(f'졸업까지 총 {year - int(self.ent_year)}년 걸렸음')

    def __repr__(self):
        return f'{self.name}은 {self.department} 입니다'

if __name__ == '__main__':
    student1 = College('Yuna', '20181236', 'Industrial Eng')
    student1.graduation(2022)
    print(student1)
