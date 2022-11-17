import collections

def palindrome_deq(data):
    string_list = collections.deque()
    
    for char in data:
        if char.isalpha():
            string_list.append(char.lower())
    
    while len(string_list) > 1:
        if string_list.popleft() != string_list.pop():
            return False
    return True

if __name__ == '__main__':
    data = input('Input String:: ')
    print(f'Is the entered sentence or word a palindrome? >> {palindrome_deq(data)}')