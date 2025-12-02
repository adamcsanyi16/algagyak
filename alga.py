m, n = map(int, input().split())

hely = 0

for i in range(1, m + 1):
    sor = list(map(int, input().split()))
    
    if all(x == 0 for x in sor):
        hely = i
        break

print(hely)