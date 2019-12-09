fibonacci = [0, 1]
i = 0
sum = 0
while i < 33:
    x = fibonacci[i] + fibonacci[i + 1]
    fibonacci.append(x)
    i += 1
    if max(fibonacci) > 4E6:
        fibonacci.pop()
        print(fibonacci)

for i in fibonacci:
    if i % 2 == 0:
        sum += i

print(sum)