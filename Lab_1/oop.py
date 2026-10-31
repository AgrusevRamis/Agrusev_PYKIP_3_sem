import sys
import math

class BiquadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        roots = []
        d = self.b**2 - 4*self.a*self.c
        print(f"Дискриминант D = {d}")

        if d < 0:
            return []

        sqrt_d = math.sqrt(d)
        y1 = (-self.b + sqrt_d) / (2*self.a)
        y2 = (-self.b - sqrt_d) / (2*self.a)

        y_values = {y1, y2}

        for y in y_values:
            if y > 0:
                roots.append(math.sqrt(y))
                roots.append(-math.sqrt(y))
            elif y == 0:
                roots.append(0.0)

        return sorted(roots)

    def __str__(self):
        return f"{self.a}x^4 + {self.b}x^2 + {self.c} = 0"

def get_valid_coefficient(name, cmd_val=None):
    if cmd_val is not None:
        try:
            return float(cmd_val)
        except ValueError:
            print(f"Аргумент '{name}' некорректен. Введите вручную.")

    while True:
        try:
            return float(input(f"Введите коэффициент {name}: "))
        except ValueError:
            print("Ошибка: нужно ввести число.")

def main():
    args = sys.argv[1:]

    a = get_valid_coefficient('A', args[0] if len(args) > 0 else None)
    while a == 0:
        print("Коэффициент A не может быть 0.")
        a = get_valid_coefficient('A')

    b = get_valid_coefficient('B', args[1] if len(args) > 1 else None)
    c = get_valid_coefficient('C', args[2] if len(args) > 2 else None)

    eq = BiquadraticEquation(a, b, c)
    print(f"\nРешение уравнения: {eq}")

    roots = eq.solve()

    if roots:
        print("Корни:")
        for r in roots:
            print(f"x = {r:.4f}")
    else:
        print("Действительных корней нет.")

if __name__ == "__main__":
    main()
