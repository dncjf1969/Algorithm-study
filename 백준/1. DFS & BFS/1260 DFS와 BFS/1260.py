def bfs(V):
    queue = [V]
    visited2[V] = 1
    while queue:
        V = queue.pop(0)
        print(V, end= ' ')
        for i in range(1, n+1):
            if (visited2[i] == 0 and arr[V][i] == 1):
                queue.append(i)
                visited2[i] = 1


def dfs(V):
    visited[V] = 1
    print(V, end=' ')
    for i in range(1, n+1):
        if (visited[i] == 0 and arr[V][i]==1):
            dfs(i)


n, m, k = map(int, input().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    arr[i][j] = arr[j][i] = 1

visited = [0] * (n + 1)
visited2 = [0] * (n + 1)

dfs(k)
print()
bfs(k)