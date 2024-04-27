def integer_division(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError
    sign = 1 if bool(dividend < 0) ^ bool(divisor < 0) == 0 else -1
    dividend = abs(dividend)
    divisor = abs(divisor)

    acc_prod = 0
    quotient = 0
    # Assuming 32-bit integer
    for i in range(31, -1, -1):
        tmp = divisor << i
        if acc_prod + tmp <= dividend:
            acc_prod += tmp
            quotient |= 1 << i
    return quotient * sign

def compare_ans(expected, actual):
    return expected == actual

print(f'{integer_division(25, 3) == int(25/3)}')
print(f'{integer_division(-25, 3) == int(-25/3)}')
print(f'{integer_division(1<<32 -1, 3) == int((1<<32 - 1) / 3)}')
print(f'{integer_division(-1<<32 + 1, 3) == int((-1<<32 + 1) / 3)}')
print(f'{integer_division(-1<<32 + 1, 123) == int((-1<<32 + 1) / 123)}')
