# Lottery number generator
# Stuart F : 29 May 2023

import random
random.seed()

def Lottery():
    numbers = [i for i in range(1,50)]
    results = []

    for i in range(6):
        ball = random.choice(numbers)
        results.append(ball)
        numbers.remove(ball)

    results.sort()
    DisplayResults(results)

def DisplayResults(results):
    for i in results:
        print(f"{i:>4}", end=" ")
    print()


# Generate 100 draws

for i in range(100):
    Lottery()

