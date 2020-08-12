from math import ceil, floor


def karatsuba_multiplication(x, y):
    """
    A much faster way to multiply 2 numbers a and b using the famous Karatsuba
    technique where the numbers are split into high and low bits and then
    multiplied.
    """
    if x < 10 and y < 10:
        return x*y

    n = max(len(str(x)), len(str(y)))
    m = ceil(n/2)
    # print(f'n: {n}, m: {m}')

    x_high = floor(x/10**m)
    x_low = x % (10**m)

    y_high = floor(y/10**m)
    y_low = y % (10**m)

    # print(f'x: {x}; x_high: {x_high}, x_low: {x_low}')
    # print(f'y: {y}; y_high: {y_high}, y_low: {y_low}')

    a = karatsuba_multiplication(x_high, y_high)
    b = karatsuba_multiplication(x_low, y_low)
    c = karatsuba_multiplication(x_high+x_low, y_high+y_low)-a-b

    return a*(10**(m*2))+c*(10**m) + b


print(karatsuba_multiplication(3141592653589793238462643383279502884197169399375105820974944592,
                               2718281828459045235360287471352662497757247093699959574966967627))
# print(karatsuba_multiplication(3567, 32459))
