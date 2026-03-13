import csv
import os

CSV_FILE = "products.csv"

initial_products = [
    ["Название", "Цена", "Количество"],
    ["Яблоки", "100", "50"],
    ["Бананы", "80", "30"],
    ["Молоко", "120", "20"],
    ["Хлеб", "40", "100"]
]

def create_initial_file():
    """Создает CSV-файл с данными"""
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(initial_products)
    print(f"Создан файл {CSV_FILE} с данными")

def load_products():
    """Загружает данные из CSV-файла"""
    products = []
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                products.append(row)
    except FileNotFoundError:
        print(f"Файл {CSV_FILE} не найден. Создаю новый...")
        create_initial_file()
        return load_products()
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return []
    return products

def save_products(products):
    """Сохраняет данные в CSV-файл"""
    try:
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(products)
        print("Данные сохранены в файл")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")

def display_products(products):
    """Отображает все товары в виде таблицы"""
    if len(products) <= 1:
        print("Список товаров пуст")
        return
    
    print("\n" + "=" * 50)
    print("Товары на складе")
    print("=" * 50)
    
    print(f"{products[0][0]:<15} {products[0][1]:<10} {products[0][2]:<12}")
    print("-" * 50)
    
    total_items = 0
    total_value = 0
    
    for product in products[1:]:
        name = product[0]
        price = int(product[1])
        quantity = int(product[2])
        
        print(f"{name:<15} {price:>8} ₽ {quantity:>10} шт.")
        
        total_items += quantity
        total_value += price * quantity
    
    print("-" * 50)
    print(f"Всего товаров: {total_items} шт.")
    print(f"Общая стоимость: {total_value} ₽")
    print("=" * 50)

def add_product(products):
    """Добавляет новый товар"""
    print("\n Добавление нового товара")  # ИСПРАВЛЕНО
    print("-" * 30)
    
    name = input("Введите название товара: ").strip()
    if not name:
        print("Название не может быть пустым")
        return products
    
    try:
        price = int(input("Введите цену товара (₽): "))
        if price <= 0:
            print("Цена должна быть положительным числом")
            return products
    except ValueError:
        print("Некорректный ввод цены")
        return products
    
    try:
        quantity = int(input("Введите количество товара: "))
        if quantity < 0:
            print("Количество не может быть отрицательным")
            return products
    except ValueError:
        print("Некорректный ввод количества")
        return products
    
    products.append([name, str(price), str(quantity)])
    print(f"Товар '{name}' добавлен")
    
    return products

def search_product(products):
    """Поиск товара по названию"""
    if len(products) <= 1:
        print("Список товаров пуст")
        return
    
    print("\n Поиск товара")
    print("-" * 30)
    
    query = input("Введите название товара для поиска: ").strip().lower()
    if not query:
        print("Введите название для поиска")
        return
    
    found = []
    for product in products[1:]:
        if query in product[0].lower():
            found.append(product)
    
    if found:
        print(f"\nНайдено товаров: {len(found)}")
        print("-" * 30)
        for product in found:
            name = product[0]
            price = int(product[1])
            quantity = int(product[2])
            total = price * quantity
            print(f"📦 {name}")
            print(f"   Цена: {price} ₽")
            print(f"   Количество: {quantity} шт.")
            print(f"   Общая стоимость: {total} ₽")
            print()
    else:
        print(f"Товары с названием '{query}' не найдены")

def calculate_total_value(products):
    """Расчет общей стоимости всех товаров"""
    if len(products) <= 1:
        print("Список товаров пуст")
        return
    
    print("\n Общая стоимость товаров")
    print("-" * 40)
    
    total_value = 0
    total_items = 0
    
    print(f"{'Товар':<15} {'Цена':<8} {'Кол-во':<8} {'Стоимость':<10}")
    print("-" * 40)
    
    for product in products[1:]:
        name = product[0]
        price = int(product[1])
        quantity = int(product[2])
        value = price * quantity
        
        print(f"{name:<15} {price:>6} ₽ {quantity:>6} шт. {value:>10} ₽")
        
        total_value += value
        total_items += quantity
    
    print("-" * 40)
    print(f"Всего товаров: {total_items} шт.")
    print(f"Итого: {total_value} ₽")
    print("=" * 40)
    
    return total_value

def main():
    """Главная функция программы"""
    print("=" * 50)
    print("Система учета товаров")
    
    products = load_products()
    
    while True:
        print("=" * 50)
        print("Меню управления")
        print("=" * 50)
        print("1. Показать все товары")
        print("2. Добавить новый товар")
        print("3. Поиск товара по названию")
        print("4. Рассчитать общую стоимость")
        print("5. Сохранить и выйти")
        print("6. Выход без сохранения")
        print("-" * 50)
        
        choice = input("Выберите действие (1-6): ").strip()
        
        if choice == "1":
            display_products(products)
        
        elif choice == "2":
            products = add_product(products)
        
        elif choice == "3":
            search_product(products)
        
        elif choice == "4":
            calculate_total_value(products)
        
        elif choice == "5":
            save_products(products)
            print("Бай-бай")
            break
        
        elif choice == "6":
            if input("Вы точно хотите выйти без сохранения? (д/н): ").lower() == 'д':
                print("Бай-бай")
                break
        
        else:
            print("Выбери от 1 до 6, пж")

if __name__ == "__main__":
    main()