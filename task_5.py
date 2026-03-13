import json
import os
from datetime import datetime

JSON_FILE = "library.json"
EXPORT_FILE = "available_books.txt"

initial_books = [
    {
        "id": 1,
        "title": "Мастер и Маргарита",
        "author": "Булгаков",
        "year": 1967,
        "available": True
    },
    {
        "id": 2,
        "title": "Преступление и наказание",
        "author": "Достоевский",
        "year": 1866,
        "available": False
    }
]

def load_books():
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(initial_books, f, ensure_ascii=False, indent=4)
        return initial_books
    
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Ашибка при загрузке файла: {e}")
        return []

def save_books(books):
    try:
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(books, f, ensure_ascii=False, indent=4)
        print("Данные сохранены")
    except Exception as e:
        print(f"Ашибка при сохранении: {e}")

def display_books(books):
    if not books:
        print("\nБиблиотека пуста")
        return
    
    print("\n" + "=" * 80)
    print(f"{'ID':<4} {'Название':<30} {'Автор':<20} {'Год':<6} {'Статус':<10}")
    print("=" * 80)
    
    for book in books:
        status = "Доступна" if book['available'] else "Выдана"
        title = book['title'][:28] + ".." if len(book['title']) > 28 else book['title']
        author = book['author'][:18] + ".." if len(book['author']) > 18 else book['author']
        
        print(f"{book['id']:<4} {title:<30} {author:<20} {book['year']:<6} {status}")
    print("=" * 80)
    print(f"Всего книг: {len(books)}")

def search_books(books):
    if not books:
        print("\nБиблиотека пуста")
        return
    
    print("\nПоиск книг")
    print("-" * 40)
    query = input("Введите автора или название для поиска: ").strip().lower()
    
    if not query:
        print("Введите текст для поиска")
        return
    
    results = []
    for book in books:
        if (query in book['title'].lower() or 
            query in book['author'].lower()):
            results.append(book)
    
    if results:
        print(f"\nНайдено книг: {len(results)}")
        display_books(results)
    else:
        print(f"Ничего не найдено по запросу '{query}'")

def add_book(books):
    print("\nДОБАВЛЕНИЕ НОВОЙ КНИГИ")
    print("-" * 40)
    new_id = max(book['id'] for book in books) + 1 if books else 1
    
    title = input("Введите название книги: ").strip()
    if not title:
        print("Название не может быть пустым")
        return books
    
    author = input("Введите автора: ").strip()
    if not author:
        print("Автор не может быть пустым")
        return books
    
    try:
        year = int(input("Введите год издания: "))
        if year < 0 or year > datetime.now().year + 10:
            print(f"Год должен быть между 0 и {datetime.now().year + 10}")
            return books
    except ValueError:
        print("Введите корректный год")
        return books
    
    avail = input("Книга доступна? (да/нет): ").strip().lower()
    available = avail in ['да', 'д', 'yes', 'y', 'true', '1']
    
    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "year": year,
        "available": available
    }
    
    books.append(new_book)
    save_books(books)
    print(f"Книга '{title}' добавлена с ID {new_id}")
    
    return books

def change_status(books):
    if not books:
        print("\nБиблиотека пуста")
        return books
    
    print("\nИзменение статуса книги")
    print("-" * 40)
    
    try:
        book_id = int(input("Введите ID книги: "))
    except ValueError:
        print("ID должен быть числом")
        return books
    
    for book in books:
        if book['id'] == book_id:
            book['available'] = not book['available']
            new_status = "доступна" if book['available'] else "выдана"
            
            save_books(books)
            print(f"Статус книги '{book['title']}' изменен на '{new_status}'")
            return books
    
    print(f"Книга с ID {book_id} не найдена")
    return books

def delete_book(books):
    if not books:
        print("\nБиблиотека пуста")
        return books
    
    print("\nУдаление книги")
    print("-" * 40)
    
    try:
        book_id = int(input("Введите ID книги для удаления: "))
    except ValueError:
        print("ID должен быть числом")
        return books
    
    for i, book in enumerate(books):
        if book['id'] == book_id:
            title = book['title']
            
            confirm = input(f"Удалить книгу '{title}'? (д/н): ").strip().lower()
            if confirm in ['д', 'да', 'y', 'yes']:
                books.pop(i)
                save_books(books)
                print(f"Книга '{title}' удалена")
            else:
                print("Удаление отменено")
            return books
    
    print(f"Книга с ID {book_id} не найдена")
    return books

def export_available(books):
    available_books = [b for b in books if b['available']]
    
    if not available_books:
        print("\n Нет доступных книг для экспорта")
        return
    
    try:
        with open(EXPORT_FILE, 'w', encoding='utf-8') as f:
            f.write("Список доступных книг\n")
            f.write(f"Дата экспорта: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 50 + "\n\n")
            
            for book in available_books:
                f.write(f"ID: {book['id']}\n")
                f.write(f"Название: {book['title']}\n")
                f.write(f"Автор: {book['author']}\n")
                f.write(f"Год: {book['year']}\n")
                f.write("-" * 30 + "\n")
            
            f.write(f"\nВсего доступных книг: {len(available_books)}")
        
        print(f"Экспортировано {len(available_books)} книг в файл {EXPORT_FILE}")

        print("\nПервые 3 экспортированные книги:")
        for book in available_books[:3]:
            print(f"   • {book['title']} — {book['author']}")
        
    except Exception as e:
        print(f"Ошибка при экспорте: {e}")

def print_menu():
    print("\n" + "=" * 60)
    print("Система учета книг в библио")
    print("=" * 60)
    print("1. Просмотр всех книг")
    print("2. Поиск по автору/названию")
    print("3. Добавить новую книгу")
    print("4. Изменить статус доступности")
    print("5. Удалить книгу по ID")
    print("6. Экспорт доступных книг")
    print("7. Выход")
    print("-" * 60)

def main():
    books = load_books()
    
    while True:
        print_menu()
        choice = input("Выберите действие (1-7): ").strip()
        
        if choice == "1":
            display_books(books)
        
        elif choice == "2":
            search_books(books)
        
        elif choice == "3":
            books = add_book(books)
        
        elif choice == "4":
            books = change_status(books)
        
        elif choice == "5":
            books = delete_book(books)
        
        elif choice == "6":
            export_available(books)
        
        elif choice == "7":
            print("\n👋 До свидания!")
            break
        
        else:
            print(" Пожалуйста, выберите 1-7")

if __name__ == "__main__":
    main()