def naive_polynomial(A, B):
    product = [0] * (len(A) * 2 - 1)
    print(product)
    for i in  range(len(A)):
        for j in range(len(B)):
            product[i+j] = product[i+j] + A[i] * B[j]
    return product

x = [3, 2, 5]
y = [5, 1, 2]

print(naive_polynomial(x, y))
