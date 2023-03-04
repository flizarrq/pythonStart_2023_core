# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

from typing import Callable


def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list

    return add_todo, get_all


add, all = notebook()

add('eat')
add('sleep')
add('work')
add('play')
print(all())


# 2) протипізувати перше завдання
#
# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def qwe(num):
    num = str(num)
    res = ' + '.join(ch + '0' * (len(num) - (i + 1)) for i, ch in enumerate(num) if num != '0') + f' = {num}'
    print(res)


qwe(121212)


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, та
# буде виводити це значення після виконання функцій

def inner(func):
    count = 0

    def count_func(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'{count=}')
        res = func(*args, **kwargs)
        return res

    return count_func


list = [1, 2, 3, 4]


@inner
def maxList(list):
    return max(list)


maxList(list)
maxList(list)
maxList(list)
maxList(list)
maxList(list)
maxList(list)
maxList(list)
maxList(list)
maxList(list)
maxList(list)
maxList(list)
