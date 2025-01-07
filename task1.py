# Завдання 1

# Потрібно розробити програму, яка імітує приймання й обробку заявок: програма має автоматично генерувати нові заявки (ідентифіковані унікальним номером або іншими даними), додавати їх до черги, а потім послідовно видаляти з черги для "обробки", імітуючи таким чином роботу сервісного центру.


from queue import Queue 
import random
#Створити чергу заявок
queue = Queue()

# # Перевіряємо, чи черга порожня
# print(queue.empty()) 
# # Перевіряємо, чи черга повна
# print(queue.full()) 
# # Перевіряємо розмір черги
# print(queue.qsize()) 


def generate_request(count):
    new_request = {"id": f"{count}"}
    queue.put(new_request)
    print(f'Заявку додано {new_request}')


def process_request():
    if not queue.empty():
        current_request = queue.get()
        print(f"Обробляється заявка: '{current_request}'")

        print(f'Черга не пуста, розмір {queue.qsize()}')
    else:
        print('Черга пуста')

def main():
    count = 0
    while True:
        print("\nМеню:")
        print("1. Створити нову заявку")
        print("2. Обробити заявку")
        print("3. Вийти")
        choice = input("Виберіть дію (1/2/3): ")
        
        if choice == "1":
            count += 1 
            generate_request(count)
        elif choice == "2":
            process_request()
        elif choice == "3":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Запуск програми
if __name__ == "__main__":
    main()


# help(Queue)






