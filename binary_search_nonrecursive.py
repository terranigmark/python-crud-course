import random


def binary_search(data, target, lower_limit, higher_limit):
    if lower_limit > higher_limit:
        return False

    while lower_limit <= higher_limit:
        mid = (lower_limit + higher_limit) // 2

        if data[mid] < target:
            low = mid + 1
        elif data[mid] > target:
            higher_limit = mid - 1
        else:
            return mid

    return -1


if __name__ == "__main__":
    data = [random.randint(0, 100) for i in range(10)]
    data.sort()
    print(data)

    target = int(input("What number would you like to find?: "))
    found = binary_search(data, target, 0, len(data) - 1)

    if found != -1:
        print(f"Element {target} is present")
    else:
        print(f"Element is NOT present")