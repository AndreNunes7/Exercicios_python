import random
num = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
print(f"Os valores sorteados foram:", end=' ')
for n in num:
    print(f"{n}", end=' ')
print(f"\nO maior valor foi {max(num)}")
print(f"O menor valor foi {min(num)}")
