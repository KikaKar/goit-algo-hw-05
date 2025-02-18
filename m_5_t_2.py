text = "1 Абаламага 2"

def generator_numbers(text: str):
    digits = "".join(filter(str.isdigit, text))
    return digits
    #def sum_profit(text: str, func: Callable):
print (generator_numbers(text))