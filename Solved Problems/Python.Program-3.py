#1) ==>> Number Pattern program

n = 5
for i in range(n):
    for j in range(i+1, n):
        print(" ", end=" ")
    for j in range(i+1):
        print(n-(n-(i+1)), end=" ")
    print()

RESULT:
        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5

#2) ==>> Number Pattern program

print()
n = 5
for i in range (n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i, n):
        print(n-i, end=" ")
    print()

RESULT:
5 5 5 5 5
  4 4 4 4
    3 3 3
      2 2
        1

#3) ==>> Number Pattern program

print()
n = 5
for i in range (n):
    for j in range(i+1, n):
        print(" ", end=" ")
    for j in range(i+1):
        print(n-(n-(i+1)), end=" ")
    for j in range(i):
        print(n-(n-(i+1)), end=" ")
    print()

RESULT:
        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5

#4) ==>> Number Pattern program

print()
n = 5
for i in range (n):
    for j in range(i+1, n):
        print(" ", end=" ")
    for j in range(i+1):
        print(n-i, end=" ")
    for j in range(i):
        print(n-i, end=" ")
    print()

RESULT:
        5
      4 4 4
    3 3 3 3 3
  2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 1