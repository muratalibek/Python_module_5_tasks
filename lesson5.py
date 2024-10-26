"""
# Упражнение 1. Пользователь вводит строку на английском языке, например 'Hello World'. 
# Вы печатаете данную строку без гласных букв. То есть: 'Hll Wrld'. Гласные буквы в английском: A», «E», «I», «O», «U», «Y
strings = str(input())
strings.lower()

without_vowels = list()
for item in strings:
    if item == 'a':
        continue
    elif item == 'o':
        continue
    elif item == 'i':
        continue
    elif item == 'u':
        continue
    elif item == 'y':
        continue
    elif item == 'e':
        continue
    else:
        without_vowels.append(item)
new_strings = "".join(without_vowels)
        
print(new_strings)

# Упражнение 2. Пользователь вводит число N с клавиатуры. Программа выводит значение факториала этого числа. 5! (5 факториал) = $1*2*3*4*5$

number = int(input('Enter the number: '))
factorial = 1
for i in range(1, number + 1):
    factorial = factorial*i
print(factorial)

# Упражнение 3. Пользователь вводит два натуральных числа a и b. Программа выводит на экран сумму всех чисел от  a до b включительно.

number = 0
number1 = int(input('Enter the number 1: '))
number2 = int(input('Enter the number 2: '))
for k in range(number1, number2 + 1):
    number = number + k
print(number)

# Упражнение 4. Пользователь вводит два натуральных числа a и b. Программа выводит на экран сумму всех четных чисел от  a до b включительно.

number = 0
number1 = int(input('Enter the number 1: '))
number2 = int(input('Enter the number 2: '))
for k in range(number1, number2 + 1):
    if k%2 == 0:
        number = number + k
print(number)


# Упражнение 5. x = 100. Пользователь вводит числа, если число четное вы его прибавляете к x, если нечетное отнимаете от x. Все это продолжается 
# до тех пор пока x не отрицательный. В таком случае вы больше не просите пользователя вводить и числа и выводите x на  экран.
x = 0
while x >= 0 and x < 100:
    number = int(input('Enter the number: '))
    if number%2 == 0:
        x = x + number
    else:
        x = x - number
    print(x)



# Упражнение 6. Просите пользователя придумать логин до тех пор пока логин не состоит только из букв. После этого выведите логин на экран

login = ""
while not login.isalpha():
    login = input('Enter the login, please: ')
    print('Login must contain only letters! Please, try again: ')
print(login.lower())
"""

# Упражнение 7. Пользователь вводит пароль через input. Верный пароль это 'abc123'. У пользователя есть 7 попыток ввести верный пароль.
# Если пароль введен правильно пишем поздравление, если за 7 попыток не смог ввести правильный пароль пишем 'попытки закончились.

password_saved = "abc123"
password = ""
tries = 1
while tries <= 7:
    password = input('Enter password: ')
    if password != password_saved:
        print(f'Entered password not correct it is remain {7 - tries} tries!')
        tries = tries + 1
        if tries == 8:
            print('Tries ended')
    else:
        print(f'Congragulate you, password {password} is correct!')
        break
