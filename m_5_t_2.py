import re
from typing import Callable, Generator

text = ("Загальний дохід працівника складається з декількох частин: "
"1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.")

def generator_numbers(text: str) -> Generator[float, None, None]:
    # Виокремлються числа з тексту
    for match in re.findall(r'(?<=\s)\d+\.\d+(?=\s)|^\d+\.\d+(?=\s)|(?<=\s)\d+\.\d+$', text):
        yield float(match)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    # Підрахунок суми чисел
    return sum(func(text))

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")