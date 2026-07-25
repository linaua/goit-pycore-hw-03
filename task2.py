import random

def get_numbers_ticket(min, max, quantity):
    numbers = []
    
    if min < 1 or max > 1000 or min > max or quantity < 1 or quantity > (max - min + 1):
        print("Invalid input values.")
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 1000, 5)
print("Ваші лотерейні числа:", lottery_numbers)
