# Problem: 幅優先探索（無向グラフ）
#　N頂点の無向グラフが与えられる。
# 頂点1から頂点Nまでの距離がLである頂点をすべて求めよ。
# ただし、頂点Xからの距離が0であるとする。

from collections import deque

N, X, L = map(int, input().split())

graph = [[] for _ in range(N)]  # 隣接リスト

for _ in range(N - 1):  # 木なので辺はN-1本
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)  # 無向グラフなので両方向に辺を張る

l = [-1] * N    # 頂点iまでの距離
l[X - 1] = 0    # 頂点Xまでの距離は0
q = deque()    # 幅優先探索のキュー
q.append(X - 1)   # 頂点Xをキューに追加
while q:
    prev = q.popleft()  # キューの先頭を取り出す
    for nxt in graph[prev]: # 隣接する頂点を調べる
        if l[nxt] == -1:    # 未訪問の場合
            l[nxt] = l[prev] + 1    # 頂点nxtまでの距離を更新        
            q.append(nxt)   # 頂点nxtをキューに追加

for i in range(N):
    if l[i] == L:   # 頂点iまでの距離がLの場合
        print(i + 1)    # 頂点iを出力