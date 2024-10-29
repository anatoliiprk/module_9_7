print('------\nЗадание "Декораторы в Python"\n------')

def is_prime(func):
    def wrapper(a, b, c):
        result_func = func(a, b, c)
        flag = True
        i = 2
        while i < result_func:
            if result_func % i == 0:
                flag = False
                break
            i += 1
        if flag:
            print('Простое число')
        else:
            print('Составное число')
        return result_func
    return wrapper

@is_prime
def sum_three(a, b, c):
    sum_ = a + b + c
    return sum_

result = sum_three(2, 3, 6)
print(result)

print('------')