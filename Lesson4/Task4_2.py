# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
import cProfile


def find_prime_number(i):
    num = 2
    cnt = 0
    prime_num = 0
    while True:
        for k in range(2, num+1):
            if num == k:
                cnt += 1
                prime_num = num
                break
            if num % k == 0:
                break
        num += 1
        if cnt == i:
            break
    return prime_num


def sieve_of_eratosthenes(i, n=10000):
    a = [0] * n
    for k in range(n):
        a[k] = k
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    # вывод простого числа
    cnt = 0
    for k in range(len(a)):
        if a[k] != 0:
            cnt += 1
        if cnt == i:
            return a[k]


if __name__ == '__main__':
    cProfile.run("find_prime_number(10)")
    cProfile.run("find_prime_number(100)")
    cProfile.run("find_prime_number(1000)")
    print(find_prime_number(1000))
    # Сложность алгоритма примерно - O(n**2)

    cProfile.run("sieve_of_eratosthenes(10)")
    cProfile.run("sieve_of_eratosthenes(100)")
    cProfile.run("sieve_of_eratosthenes(1000)")
    print(sieve_of_eratosthenes(1000))
    # Сложность алгоритма O(n log log n)

    # Поиск i-го числа в отрезке [1, n] с помощью решета Эратосфена происходит в разы быстрее функции find_prime_number