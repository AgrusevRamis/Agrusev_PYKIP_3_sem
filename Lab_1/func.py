import sys
import math

calc_discriminant = lambda a, b, c: b**2 - 4*a*c

def get_y_roots(a, b, d):
    if d < 0:
        return []
    sqrt_d = math.sqrt(d)
    return [(-b + sqrt_d) / (2*a), (-b - sqrt_d) / (2*a)]

def process_y_roots(y_roots):
    result = []
    for y in set(y_roots):
        match y:
            case y if y > 0:
                result.extend([math.sqrt(y), -math.sqrt(y)])
            case 0:
                result.append(0.0)
            case _:
                pass
    return sorted(result)

def input_coefficient(name, cmd_val=None):
    if cmd_val is not None:
        try:
            return float(cmd_val)
        except ValueError:
            print(f"Ошибка в аргументе {name}. Ручной ввод.")

    while True:
        try:
            return float(input(f"Коэффициент {name}: "))
        except ValueError:
            print("Некорректно. Введите число.")

def main():
    args = sys.argv[1:]

    a = input_coefficient('A', args[0] if len(args) > 0 else None)
    if a == 0:
        print("A не может быть 0.")
        sys.exit(1)

    b = input_coefficient('B', args[1] if len(args) > 1 else None)
    c = input_coefficient('C', args[2] if len(args) > 2 else None)

    print(f"\nУравнение: {a}x^4 + {b}x^2 + {c} = 0")

    d = calc_discriminant(a, b, c)
    print(f"D = {d}")

    y_vals = get_y_roots(a, b, d)
    x_vals = process_y_roots(y_vals)

    if x_vals:
        print("Корни:")
        for x in x_vals:
            print(f"x = {x:.4f}")
    else:
        print("Корней нет.")

if __name__ == "__main__":
    main()
