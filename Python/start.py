
def hello_world():
    print('Hello World')

add = lambda x, y : x + y

nums = [1,2,3,4,5]
square = list(map(lambda x: x*x, nums))

even = list(filter(lambda x: x%2 == 0, nums))

students = [('Alice', 88),  ('Bob', 74), ('David', 89)]
sorted_students = sorted(students, key=lambda student: student[1])


def switch_case(option):
    return {
        'a': "Apple",
        'b': "Banana",
        'c': "Cherry"
    }.get(option, 'Invalid Option')

flatten = lambda l : [item for sublist in l for item in sublist]


if __name__ == "__main__":
    hello_world()
    print(add(3,4))
    print(square)
    print(even)
    print(sorted_students)
    print(switch_case('b'))
    print(flatten([[1], [2,3,4], [6,7], [8,9]]))
    x = [1,2,3]
    x.append({4})
    print(x)
    x.extend([6,7])
    print(x)

    