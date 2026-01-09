def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
D, P = map(int, input().split())

H = D / P
N = H
res = 0

while N > 1:
    i = 0
    count = 0

    # it'll give prime num set
    while True:
        k = (i * H) + N

        if is_prime(int(k)) and k < D:
            count += 1

        if i == (P - 1):
            break
        i += 1

    # if all elements of set are prime
    # ie if count == P then all elements of set are prime
    if count == P:
        res += 1

    N -= 1

print(res, end=" ")
