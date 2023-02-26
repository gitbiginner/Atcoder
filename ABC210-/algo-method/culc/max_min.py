# https://algo-method.com/tasks/1088

sa, ta = map(int, input().split())
sb, tb = map(int, input().split())

left = max(sa, sb)
right = min(ta, tb)


if sa <= tb:
    print(abs(right-left))
else:
    print(0)
