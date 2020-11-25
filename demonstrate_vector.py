from random import randint
from Vector.Vector import Vector

if __name__ == "__main__":
    list_v1 = []
    list_v2 = []
    for val in range(10):
        v1 = Vector(randint(0, 100), randint(0, 100), randint(0, 100))
        list_v1.append(v1)
        v2 = Vector(randint(0, 100), randint(0, 100), randint(0, 100))
        list_v2.append(v2)
    print(list_v1)
    print(list_v2)
    for v_add, v_sub in zip(map(lambda x, y: x + y, list_v1, list_v2), map(lambda x, y: x - y, list_v1, list_v2)):
        print(f'Add = {v_add}, Subtract = {v_sub}')
