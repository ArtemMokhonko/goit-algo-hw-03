import random

def get_numbers_ticket(min, max, quantity):
    if 1<= min <= max <= 1000 and 1 <= quantity <= max - min+1:
        num_list = range(min, max +1)
        numbers = random.sample(num_list, quantity)              
        return sorted(numbers)
    else:
        return []
    
        


lottery_numbers = get_numbers_ticket(10, 1001, 11)
print(f"Ваші лотерейні числа: {lottery_numbers}")