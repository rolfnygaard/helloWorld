import argparse

def multiply_by_two(x:float):

    return x*2

def get_args():
    parser = argparse.ArgumentParser(description="doesn't matter")
    parser.add_argument('number', type=float, default=0)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_args()
    a_number = args.number
    result = multiply_by_two(a_number)
    print(f"{a_number} * 2 = {result}")
    