n = int(input("Введите число: "))
def divisible():
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
list = []
for i in divisible():
    list.append(str(i))
print(",".join(list))