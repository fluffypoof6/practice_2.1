from datetime import datetime
import os

LOG_FILE = "calculator.log"

def add_to_log(num1, num2, op, result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    a = int(num1) if num1.is_integer() else num1
    b = int(num2) if num2.is_integer() else num2
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {a} {op} {b} = {result}\n")

def show_last_operations():
    if not os.path.exists(LOG_FILE):
        print("\nИстория операций пуста")
        return
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        if not lines:
            print("\nИстория операций пуста")
            return
        
        print("\n" + "=" * 50)
        print("\n Последние 5 операции:")
        print("=" * 50)
        
        for line in lines[-5:]:
            print(f"  {line.strip()}")
        print("=" * 50)
        
    except Exception as e:
        print(f"Ошибка при чтении лога: {e}")

def clear_log():
    try:
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            pass
        print("Лог-файл очищен")
    except Exception as e:
        print(f"Ошибка при очистке лога: {e}")

def print_menu():
    """Выводит меню"""
    print("\n" + "=" * 50)
    print("Калькулятор")
    print("=" * 50)
    print("Доступные команды:")
    print("+, -, *, / - операции")
    print("history/история - показать историю")
    print("clearя/очистить - очистить лог")
    print("q/й - выход")
    print("-" * 50)

show_last_operations()

while True:
    print_menu()
    
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Нужно вводить числа")
        continue
    
    op = input("Введите операцию (+, -, *, /, history, clear, q): ").strip().lower()
    
    if op == '+':
        result = num1 + num2
        print(f"Результат: {num1} + {num2} = {result}")
        add_to_log(num1, num2, op, result)
    elif op == '-':
        result = num1 - num2
        print(f"Результат: {num1} - {num2} = {result}")
        add_to_log(num1, num2, op, result)
    elif op == '*':
        result = num1 * num2
        print(f"Результат: {num1} * {num2} = {result}")
        add_to_log(num1, num2, op, result)
    elif op == '/':
        if num2 == 0:
            result = "Ошибка: деление на ноль"
            print(f"ноу {result}")
            add_to_log(num1, num2, op, "ERROR")
        else:
            result = num1 / num2
            print(f"Результат: {num1} / {num2} = {result}")
            add_to_log(num1, num2, op, result)  
    elif op == 'history' or op == 'история':
        show_last_operations()
        continue  # Возвращаемся в начало цикла без запроса чисел
    elif op == 'clear' or op == 'очистить':
        clear_log()
        continue  # Возвращаемся в начало цикла без запроса чисел
    elif op == 'q' or op == 'й':
        print("бб")
        break
    else:
        print("Неизвестная операция")