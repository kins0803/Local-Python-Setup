def hello():
    print("Hello, user!")

def pack(x, y, z):
    return[x, y, z]

def eat_lunch(rand_list):
    if len(rand_list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(rand_list)):
            if i == 0:
                print(f"First I eat {rand_list[0]}")
            else:
                print(f"Next I eat {rand_list[i]}")

hello()
print(pack("one", "two", "three"))
print(pack(1,2,3))
print(pack("one", 2, 3))
eat_lunch([])
eat_lunch(["banana", "sandwich", "carrots", "soda"])
eat_lunch(["apple"])