import sys
import math

def get_coefficient(name, value_from_cmd=None):
    if value_from_cmd is not None:
        try:
            return float(value_from_cmd)
        except ValueError:
            print(f"Ошибка: Аргумент '{name}' ({value_from_cmd}) не является числом. Переход в режим ручного ввода.")
    while True:
        try:
            val = input(f"Введите коэффициент {name}: ")
            return float(val)
        except ValueError:
            print("Ошибка: Введено некорректное значение. Пожалуйста, введите действительное число.")

def solve_biquadratic(a, b, c):
    roots = []
    d = b**2 - 4*a*c
    print(f"Дискриминант D = {d}")

    if d < 0:
        return []

    sqrt_d = math.sqrt(d)
    y1 = (-b + sqrt_d) / (2*a)
    y2 = (-b - sqrt_d) / (2*a)

    y_values = set()
    y_values.add(y1)
    y_values.add(y2)

    for y in y_values:
        if y > 0:
            x1 = math.sqrt(y)
            x2 = -math.sqrt(y)
            roots.append(x1)
            roots.append(x2)
        elif y == 0:
            roots.append(0.0)

    return sorted(list(set(roots)))

def main():
    args = sys.argv[1:]

    a = get_coefficient('A', args[0] if len(args) > 0 else None)

    if a == 0:
        print("Коэффициент A не может быть равен 0 (уравнение не будет биквадратным).")
        while a == 0:
            try:
                a = float(input("Введите коэффициент A (не равный 0): "))
            except ValueError:
                print("Ошибка ввода.")

    b = get_coefficient('B', args[1] if len(args) > 1 else None)
    c = get_coefficient('C', args[2] if len(args) > 2 else None)

    print(f"\nУравнение: {a}x^4 + {b}x^2 + {c} = 0")

    roots = solve_biquadratic(a, b, c)

    if roots:
        print("Действительные корни:")
        for r in roots:
            print(f"x = {r:.4f}")
    else:
        print("Действительных корней нет.")

if __name__ == "__main__":
    main()
