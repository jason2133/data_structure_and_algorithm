# 가변 매개변수 - Tuple

def grade(name, number=1, *points):
    avg = sum(points) / len(points)
    print(f'{name}은 학번 {number}이며 평균은 {avg:.2f}')
    return avg

if __name__ == '__main__':
    average = grade('홍길동', 20, 90, 95, 100)
    if average >= 90:
        print('등급은 A')
    elif average >= 80:
        print('등급은 B')
    elif average >= 70:
        print('등급은 C')
    else:
        print('등급은 F')


    