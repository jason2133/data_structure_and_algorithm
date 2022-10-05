import re


# 리스트 비교 활용 펠린드롬
# 앞뒤가 똑같은 단어 또는 문장을 회문 (Palindrome, 펠린드롬)

def palindrome(data:str) -> bool:
    string_list = []
    for char in data:
        if char.isalpha():
            string_list.append(char.lower())
    print(string_list)
    while len(string_list) > 1:
        if string_list.pop(0) != string_list.pop():
            return False
    return True

if __name__ == '__main__':
    data = input('Input String:: ')
    print(f'Is the entered sentence or word a palindrome? >> {palindrome(data)}')

