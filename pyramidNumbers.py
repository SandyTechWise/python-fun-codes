N = int(input("Enter the Number to print pyramid pattern: "))

for i in range(1, N+1):
    print(" "*(N-i), end="")
    for j in range(1, i+1):
        print(j, end="")
    for k in range(i-1, 0, -1):
        print(k, end="")
    print()
