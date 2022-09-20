# 가변 매개변수 - Dictionary

def grade(name, number=1, **points):
    avg = sum(points.values()) / len(points)
    print(f'{name}은 학번 {number}이며 평균은 {avg:.2f}')
    return avg

if __name__ == '__main__':
    # average = grade('홍길동', 국어=90, 영어=89, 수학=77)
    average = grade('홍길동', 20, 국어=90, 영어=89, 수학=77)
    # average = grade('홍길동', number=20, 국어=90, 영어=89, 수학=77)
    if average >= 90:
        print('등급은 A')
    elif average >= 80:
        print('등급은 B')
    elif average >= 70:
        print('등급은 C')
    else:
        print('등급은 F')
    
    