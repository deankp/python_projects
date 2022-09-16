def hello():
    print("Hello! user!")


def pack(water, apple, sandwich):
    return [water, apple, sandwich]


def eat_lunch(my_list):
    if len(my_list) == 0:
        print("my lunchbox is empty!")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat {my_list[0]}")
            else:
                print(f"Next I eat {my_list[i]}")


hello()
print(pack("water", "apple", "sandwich"))
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple", "water", "sandwich", "brownie"])
