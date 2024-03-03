


def get_nums():
    return int(input("Enter a num: "))


for i in range(10):
    if get_nums() < 18:
        raise Exception("You are under aged to vote")
