import cmath

def solve_quadratic(a, b, c):
    """
    Решает квадратное уравнение вида ax^2 + bx + c = 0.
    Возвращает корни уравнения, включая комплексные числа.
    """
    if a == 0:
        if b == 0:
            return "Нет решений" if c != 0 else "Бесконечное множество решений"
        return f"Линейное уравнение, корень: {-c / b}"
    
    # Вычисление дискриминанта
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    
    # Вычисление корней
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)
    
    return root1, root2

# Пример использования
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

result = solve_quadratic(a, b, c)
print(f"Результат: {result}")