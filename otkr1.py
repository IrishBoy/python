
a, b, c = map(int, input().split())

n = int(input())

if n <=  7:
    print(min(c, b, n * a))
elif 7 < n < 28 :
    d7 = n // 7
    r1= n % 7
    print(min(c, b * (d7 + 1), b * d7 + a * r1, n * a))
else :
    s = (n // 28) * (min(28 * a, 4 * b,c))
    rest = n % 28
    if rest != 0:
        rest7 = rest // 7
        s+=(min(rest * a,rest7 * b + a * (rest - rest7 * 7), c))
    type(s)
    print(s)
