import math


# complejidad de 0(1)
def o_1(n):
    return 1


# complejidad de 0(log n)
def o_log_n(n):
    return math.log(n, 10)


# complejidad de 0(n)
def o_n(n):
    return n


# complejidad de 0(n log n)
def o_n_log_n(n):
    return n * math.log(n, 10)


# complejidad de 0(n**2)
def o_n_2(n):
    return n ** 2


# complejidad de 0(2**n)
def o_2_n(n):
    return 2 ** n


if __name__ == "__main__":
    n = 1000

    print(o_1(n))
    print(o_log_n(n))
    print(o_n(n))
    print(o_n_log_n(n))
    print(o_n_2(n))
    print(o_2_n(n))

