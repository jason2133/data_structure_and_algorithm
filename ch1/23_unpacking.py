# Unpacking

def test(name, class_id, points):
    print(name, class_id, points)

test('gildong', 1234, 4.5)
test(*['gildong', 1234, 4.5])

def avg(*data):
    return sum(data) / len(data)

if __name__ == '__main__':
    result = avg(90, 90, 88, 100, 95)
    print(f'{result:.2f}')

