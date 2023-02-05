def in_ce(far):
    ce = 5/9 * (far - 32)
    print(f"Температура в Цельсий {ce}")
f = int(input("Введите температуру в фаренгейте: "))
in_ce(f)