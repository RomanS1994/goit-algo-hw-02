# Завдання 2

# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до двосторонньої черги (deque з модуля collections в Python), а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, а також бути нечутливою до регістру та пробілів.


from collections import deque 

def is_palindrome(string: str) :
    clear_string = string.lower().replace(" ", "")
    dq = deque(clear_string)
    
    print(dq)
    while True:
        if len(dq) >= 2:
            first_element = dq.pop()
            last_element = dq.popleft()
            if first_element != last_element:
                print('Це не паліндром')
                break
            else:
                print('Це паліндром')
                break
        else: 
            print('Текст закороткий')
            break

message = input('Введіть текст для перевірки >>>  ')
is_palindrome(message)


# help(deque)