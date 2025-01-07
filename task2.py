# Завдання 2

# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до двосторонньої черги (deque з модуля collections в Python), а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, а також бути нечутливою до регістру та пробілів.


from collections import deque 

def is_palindrome(string: str):
    clear_string = string.lower().replace(" ", "")
    dq = deque(clear_string)
    

    while len(dq) > 1:  
        first_element = dq.popleft()  
        last_element = dq.pop()       
        if first_element != last_element:
            return False  
    
    return True 

# Тест
message = input('Введіть текст для перевірки >>>  ')
if len(message) > 1:
    if is_palindrome(message):
        print('Це паліндром!')
    else:
        print('Це не паліндром!')
else:
    print("Текст закороткий")

# help(deque)