'''
Написати функцію, яка буде рекурсивно рахувати суму
'''

def rec_sum(n: int) -> int: # 5 -> 5 + 4 + 3 + 2 + 1 
    # Умова для зупинки рекурсії
    if n <= 0:
        return 0

    # Рекурсивний виклик
    return n + rec_sum(n - 1) # 5 + rec_num(4) -> 5 + 4 + rec_num(3) -> ... -> 5 + 4 + 3 + 2 + 1 + 0

# print(rec_sum(3))

def rec_sum(n: int, level: int = 0) -> int:
    if n <= 0:
        print(f'Level: {level} |rec_sum({n})= 0')
        return 0 
    
    print(f'Level: {level} | rec_sum({n}) = {n} + rec_sum({n - 1})')
    result = n + rec_sum(n - 1, level=level + 1)
    print(f'Level: {level} | rec_sum({n}) = {result}')
    return result

print(rec_sum(3))