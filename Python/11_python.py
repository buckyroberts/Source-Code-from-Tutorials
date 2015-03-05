numbersTaken = [2, 5, 12, 13, 17]

print("Here are the numbers that are still available")

for n in range(1,20):
    if n in numbersTaken:
        continue
    print(n)
