def coinChange_(money):
    change = [0 for i in range(5)]
    denominator = [500, 100, 50, 10]
    for i in range(len(denominator)):
        change[i] = money // denominator[i]
        money %= denominator[i]
    change[i+1] = money
    return change

if __name__ == '__main__':
    money = int(input("input money >> "))
    change = coinChange_(money)
    print(f'{money}원은 500원 {change[0]}개, 100원 {change[1]}개, 50원 {change[2]}개, 10원 {change[3]}개이며 나머지는 {change[4]}원으로 교환됨')    