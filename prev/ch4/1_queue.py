# 큐
# Queue

# Circle Queue Basic Algorithm

def enqueue(q, v):
    global rear
    global MAX

    if full(q):
        q.append(v)
        rear = (rear + 1) % MAX

def dequeue(q):
    global front
    global MAX

    if empty(q):
        q.pop(0)
        front = (front + 1) % MAX

def empty(q):
    global rear
    global front

    if rear != front:
        return True
    else:
        print('Queue is Empty')
        return False

def full(q):
    global rear
    global front

    if front % MAX != (rear + 1) % MAX:
        return True
    else:
        print('Queue is Full')
        return False

if __name__ == '__main__':
    # Queue Create
    main_q = []

    MAX = 5
    rear = 0
    front = 0

    enqueue(main_q, 'A')
    enqueue(main_q, 'B')
    enqueue(main_q, 'C')
    enqueue(main_q, 'D')
    print(main_q)
    dequeue(main_q)

