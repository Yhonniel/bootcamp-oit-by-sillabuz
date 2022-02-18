def getPrimos():
    numbers = [1, 3, 5, 7, 2, 10, 12]
    prime = []

    for num in numbers:
        if num == 2:
            prime.append(num)
        else:
            for n in range(2, num):
                if num % n == 0:
                    # print(f'No es primo {num}')
                    break
                else:
                    # print(f'Si es numero primo {num}')
                    prime.append(num)
                    break

    prime.sort(reverse=True)
    return prime


prime = getPrimos()
print(f'Lista de numero primos {prime}')
