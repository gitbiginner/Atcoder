Q = int(input())

query = [input().split() for i in range(Q)]


Map = {}
for q in query:
    if q[0] == "1":
        Map[q[1]] = q[2]
    if q[0] == "2":
        print(Map[q[1]])
