import math
from datetime import datetime
import os

def parse_float_input(prompt):
    value = input(prompt).strip().replace(',', '.')
    try:
        return float(value)
    except ValueError:
        raise ValueError("Некорректное число")

def main():
    try:
        a = parse_float_input("Введите a: ")
        b = parse_float_input("Введите b: ")
        x_start = parse_float_input("Введите начальное значение x (xн): ")
        x_end = parse_float_input("Введите конечное значение x (xк): ")
        delta_x = parse_float_input("Введите шаг Δx: ")
        
        if delta_x <= 0:
            print("Ошибка: шаг Δx должен быть положительным.")
            return
            
    except ValueError as e:
        print(f"Ошибка: {e}")
        return

    current_date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    file_exists = os.path.exists('results.txt')

    with open('results.txt', 'a', encoding='utf-8') as file:
        # Запись заголовка только если файл новый
        if not file_exists or os.stat('results.txt').st_size == 0:
            file.write("ФИО: Бричка Владислав Сергеевич\n")
            file.write("Группа: СКС-23\n\n")

        # Разделитель с датой выполнения
        file.write(f"=== Дата выполнения: {current_date} ===\n")
        file.write(f"Параметры: a={a}, b={b}, xн={x_start}, xк={x_end}, Δx={delta_x}\n")
        file.write("x\t\t\ty\n")
        file.write("----------------------------\n")

        x = x_start
        while x <= x_end + 1e-9:
            if x > a:
                try:
                    term = math.exp(x - a)
                    arg = b - x
                    if arg == 0:
                        y = math.nan
                    else:
                        log_val = math.log(abs(arg))
                        y = term - log_val ** 2
                except:
                    y = math.nan
            elif x < -0.5:
                try:
                    term = (x - a) ** 2
                    angle = b - x
                    tan_val = math.tan(angle)
                    y = term + tan_val ** 3
                except:
                    y = math.nan
            else:
                if b < x < a:
                    total = 0.0
                    for l in range(3, 9):
                        total += (x - math.sqrt(l)) / l
                    y = total
                else:
                    y = math.nan

            x_str = f"{x:.2f}"
            y_str = f"{y:.3f}" if not math.isnan(y) else "не определен"
            
            print(f"{x_str}\t\t{y_str}")
            file.write(f"{x_str}\t\t{y_str}\n")

            x = round(x + delta_x, 10)

        file.write("\n")  # Пустая строка между запусками

if __name__ == "__main__":
    main()