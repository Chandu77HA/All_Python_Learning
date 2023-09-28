#0) ==>> Star Pattern program (Type-1)

n = int(input("Enter the number :"))
for i in range(1, n+1):
    a = ' *'*i
    print(a.center(n*2," "))

#1) ==>> Star Pattern program (Type-1)

n = 5
print("*"*n)

RESULT:
*****

#2) ==>> Star Pattern program (Type-2)

n = 5
for i in range (n):
    print("=", end=" ")
print()

RESULT:
= = = = =

#3) ==>> Star Pattern program (Type-3)

n = 5
for i in range (n):
    for j in range(n):
        print("$", end="  ")
    print()

RESULT:
$  $  $  $  $
$  $  $  $  $
$  $  $  $  $
$  $  $  $  $
$  $  $  $  $

#4) ==>> Star Pattern program (Type-4)

n = 5
for i in range (n):
    for j in range(i+1):
        print("R", end="  ")
    print()

RESULT:
R
R  R
R  R  R
R  R  R  R
R  R  R  R  R

#5) ==>> Star Pattern program (Type-5)

n = 5
for i in range (n):
    for j in range(i, n):
        print("P", end="  ")
    print()

RESULT:
P  P  P  P  P
P  P  P  P
P  P  P
P  P
P

#6) ==>> Star Pattern program (Type-6)

n = 5
for i in range (n):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i+1):
        print("C", end=" ")
    print()

RESULT:
          C
        C C
      C C C
    C C C C
  C C C C C

#7) ==>> Star Pattern program (Type-7)

n = 5
for i in range (n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, n):
        print("N", end=" ")
    print()

RESULT:
  N N N N N
    N N N N
      N N N
        N N
          N

#8) ==>> Star Pattern program (Type-8)

n = 5
for i in range (n):
    for j in range(i+1, n):
        print(" ", end=" ")
    for j in range(i+1):
        print("S", end=" ")
    for j in range(i):
        print("S", end=" ")
    print()

RESULT:
        S
      S S S
    S S S S S
  S S S S S S S
S S S S S S S S S

#9) ==>> Star Pattern program (Type-9)

n = 5
for i in range (n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i, n):
        print("c", end=" ")
    for j in range(i+1, n):
        print("c", end=" ")
    print()

RESULT:
c c c c c c c c c
  c c c c c c c
    c c c c c
      c c c
        c

#10) ==>> Star Pattern program (Type-10)

n = 5
for i in range (n-1):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print("A", end=" ")
    for j in range(i+1):
        print("A", end=" ")
    print()
for i in range (n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, n):
        print("A", end=" ")
    for j in range(i+1, n):
        print("A", end=" ")
    print()

RESULT:
          A
        A A A
      A A A A A
    A A A A A A A
  A A A A A A A A A
    A A A A A A A
      A A A A A
        A A A
          A

#11) ==>> Star Pattern program (Type-11)

n = 5
for i in range(n):
    for j in range(i+1, n):
        print(" ", end=" ")
    for j in range(i+1):
        print("M", end=" ")
    for j in range(i):
        print("M", end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i+1, n):
        print("M", end=" ")
    for j in range(i+2, n):
        print("M", end=" ")
    print()

RESULT:
        M
      M M M
    M M M M M
  M M M M M M M
M M M M M M M M M
  M M M M M M M
    M M M M M
      M M M
        M

#12) ==>> Number Pattern program (Type-1)

n = 5
for i in range (n):
    for j in range(i+1):
        print(i+1, end="  ")
    print()

RESULT:
1
2  2
3  3  3
4  4  4  4
5  5  5  5  5

#13) ==>> Number Pattern program (Type-2)

print()
n = 5
p = 1
for i in range (n):
    for j in range(i+1):
        print(p, end="  ")
    p += 1
    print()

RESULT:
1
2  2
3  3  3
4  4  4  4
5  5  5  5  5

#14) ==>> Number Pattern program (Type-3)

print()
n = 5
p = 5
for i in range (n):
    for j in range(i, n):
        print(p, end="  ")
    p -= 1
    print()

RESULT:
5  5  5  5  5
4  4  4  4
3  3  3
2  2
1

#15) ==>> Number Pattern program (Type-4)

print()
n = 5
p = 1
for i in range(n):
    for j in range(i+1, n):
        print(" ", end=" ")
    for j in range(i+1):
        print(p, end=" ")
    p += 1
    print()

RESULT:
        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5

#16) ==>> Number Pattern program (Type-5)

print()
n = 5
p = 5
for i in range (n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i, n):
        print(p, end=" ")
    p -= 1
    print()

RESULT:
5 5 5 5 5
  4 4 4 4
    3 3 3
      2 2
        1

#17) ==>> Number Pattern program (Type-6)

print()
n = 5
p = 1
for i in range (n):
    for j in range(i+1, n):
        print(" ", end=" ")
    for j in range(i+1):
        print(p, end=" ")
    for j in range(i):
        print(p, end=" ")
    p += 1
    print()

RESULT:
        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5

#18) ==>> Number Pattern program (Type-7)

print()
n = 5
p = 5
for i in range (n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i, n):
        print(p, end=" ")
    for j in range(i+1, n):
        print(p, end=" ")
    p -= 1
    print()

RESULT:
5 5 5 5 5 5 5 5 5
  4 4 4 4 4 4 4
    3 3 3 3 3
      2 2 2
        1

#19) ==>> Number Pattern program (Type-7)

print()
n = 5
p = 1
for i in range (n-1):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print(p, end=" ")
    for j in range(i+1):
        print(p, end=" ")
    p += 1
    print()

q = 5
for i in range (n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, n):
        print(q, end=" ")
    for j in range(i+1, n):
        print(q, end=" ")
    q -= 1
    print()

RESULT:
          1
        2 2 2
      3 3 3 3 3
    4 4 4 4 4 4 4
  5 5 5 5 5 5 5 5 5
    4 4 4 4 4 4 4
      3 3 3 3 3
        2 2 2
          1


#20) ==>> Number Pattern program (Type-8)

print()
n = 5
p = 1
for i in range(n):
    for j in range(i+1, n):
        print(" ", end=" ")
    for j in range(i+1):
        print(p, end=" ")
    for j in range(i):
        print(p, end=" ")
    p += 1
    print()

q = 4
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i+1, n):
        print(q, end=" ")
    for j in range(i+2, n):
        print(q, end=" ")
    q -= 1
    print()

RESULT:
        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
  4 4 4 4 4 4 4
    3 3 3 3 3
      2 2 2
        1


#21) ==>> Number Pattern program (Type-9)

n = 5
for i in range(n):
    p = 1
    for j in range(i+1):
        print(p, end="  ")
        p += 1
    print()

RESULT:
1
1  2
1  2  3
1  2  3  4
1  2  3  4  5

#22) ==>> Number Pattern program (Type-10)

print()
n = 5
for i in range(n):
    p = 1
    for j in range(i, n):
        print(p, end="  ")
        p += 1
    print()

RESULT:
1  2  3  4  5
1  2  3  4
1  2  3
1  2
1

#23) ==>> Number Pattern program (Type-11)

print()
n = 5
for i in range(n):
    p = 1
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i+1):
        print(p, end=" ")
        p += 1
    print()

RESULT:
          1
        1 2
      1 2 3
    1 2 3 4
  1 2 3 4 5

#24) ==>> Number Pattern program (Type-12)

print()
n = 5
for i in range(n):
    p = 1
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, n):
        print(p, end=" ")
        p += 1
    print()

RESULT:
  1 2 3 4 5
    1 2 3 4
      1 2 3
        1 2
          1

#25) ==>> Number Pattern program (Type-13)

print()
n = 5
for i in range(n):
    p = 1
    for j in range(i+1, n):
        print(" ", end=" ")
    for j in range(i+1):
        print(p, end=" ")
        p += 1
    for j in range(i):
        print(p, end=" ")
        p += 1
    print()

RESULT:
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9

#26) ==>> Number Pattern program (Type-14)

print()
n = 5
p = 5
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i, n):
        print(p, end=" ")
    for j in range(i+1, n):
        print(p, end=" ")
    p -= 1
    print()

RESULT:
5 5 5 5 5 5 5 5 5
  4 4 4 4 4 4 4
    3 3 3 3 3
      2 2 2
        1

#27) ==>> Number Pattern program (Type-15)

print()
n = 5
for i in range(n):
    p = 5
    for j in range(i+1):
        print(p, end="  ")
        p -= 1
    print()

RESULT:
5
5  4
5  4  3
5  4  3  2
5  4  3  2  1

#28) ==>> Number Pattern program (Type-16)

print()
n = 5
k = 5
for i in range (n):
    p = k
    for j in range(i):
        print(" ", end=" ")
    for j in range(i, n):
        print(p, end=" ")
        p -= 1
    k -= 1
    print()

RESULT:
5 4 3 2 1
  4 3 2 1
    3 2 1
      2 1
        1


#29) ==>> Number Pattern program (Type-17)

n = 5
for i in range(n):
    p = 1
    for j in range(i+1, n):
        print(" ", end=" ")
    for j in range(i+1):
        print(p, end=" ")
        p += 1
    for j in range(i):
        print(p, end=" ")
        p -= 1
    print()

RESULT:
        1
      1 2 3
    1 2 3 4 3
  1 2 3 4 5 4 3
1 2 3 4 5 6 5 4 3

#30) ==>> Number Pattern program (Type-18)

n = 4
p = 1
for i in range(n):
    for j in range(i+1):
        print(p, end="  ")
        p += 1
    print()

RESULT:
1
2  3
4  5  6
7  8  9  10