def water_purchase(mt_person, water_per_person):
    all = mt_person * water_per_person
    all_package = all // 12
    all_etc = all % 12
    money = all_package * 10000 + all_etc * 800
    return all_package, all_etc, money

if __name__ == '__main__':
    mt_person = int(input('MT Person : '))
    water_per_person = int(input('water_per_person : '))
    result = water_purchase(mt_person, water_per_person)
    print(f'생수 패키지 개수 : {result[0]}개, 생수 낱개 개수 : {result[1]}개, 전체 구매액 : {result[2]}원')

