#SIMPLE FIBONACCI NUMBER CALC

def fibonacci(n):
    sequence = [0, 1]

    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

num = int(input("Enter a number: "))

result = fibonacci(num)
print(f"The first {num} fibonacci numbers are: {result}")