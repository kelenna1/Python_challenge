import calculator
x, y = 5, 3

add_result = calculator.add(x, y)
print(f"{x} + {y} = {add_result}")

subtract_result = calculator.subtract(x, y)
print(f"{x} - {y} = {subtract_result}")

multiply_result = calculator.multiply(x, y)
print(f"{x} * {y} = {multiply_result}")

division_result = calculator.divide(x, y)
print(f"{x} / {y} = {division_result:.2f}")