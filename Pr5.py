g = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []  }

h = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
def astar(s, g1):
    o = [s]              # open list
    d = {s: 0}           # distance (g cost)
    p = {s: None}        # parent

    while o:
        n = min(o, key=lambda x: d[x] + h[x])
        if n == g1:
            path = []
            while n:
                path.append(n)
                n = p[n]
            return path[::-1]
        o.remove(n)
        for v, c in g[n]:
            if v not in d or d[n] + c < d[v]:
                d[v] = d[n] + c
                p[v] = n
                o.append(v)

print(astar('A', 'D'))
print("Jayant75")