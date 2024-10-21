import decimal
import numpy as np
decimal.getcontext().prec = 64

num1_as_str = '123.456789876543212345678987654321'
num2_as_str = '123.456789876543212345678987654321'

num1 = decimal.Decimal(num1_as_str)
num2 = decimal.Decimal(num2_as_str)

integer_part1, fractional_part1 = str(num1).split(".")

print(f"Integer part: {integer_part1}")
print(f"Fractional part: {fractional_part1}")

print(f'difference: {num1 - num2}')
print(num1 ==  num2)

npnum = np.float64(123.456789876543212345678987654321)
npnumdec = decimal.Decimal(npnum)
print(f'yolo {npnumdec}')


print(f'play num {decimal.Decimal(0.0)}')
