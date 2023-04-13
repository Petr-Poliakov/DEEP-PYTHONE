import math
import random
import csv

def quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return None


def generate_csv_file(filename, num_rows):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for i in range(num_rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            csv_writer.writerow(row)




def quadratic_decorator(func):
    def wrapper(filename):
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                result = func(*map(int, row))
                print(f"Roots of {row}: {result}")
    return wrapper


def save_to_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        filename = f"{func.__name__}.json"
        with open(filename, 'a+') as json_file:
            data = {"input": (args, kwargs), "output": result}
            json.dump(data, json_file, indent=4)
            json_file.write('\n')
        return result
    return wrapper


generate_csv_file("test.csv", 100)

decorated_func = quadratic_decorator(quadratic_equation)

decorated_func("test.csv")

quadratic_equation = save_to_json(quadratic_equation)

quadratic_equation(1, 2, 1)
quadratic_equation(1, 5, 6)