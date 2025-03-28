# Problem: 幅優先探索（無向グラフ）
#　N頂点の無向グラフとそれらを結ぶ M 本の辺の情報と頂点番号 X が与えられます。
# 現在の頂点に隣接する全ての未訪問の頂点を、
# 現在キューに入っている全ての頂点を探索したのち、
# 番号が一番小さい頂点から順に探索する。

from collections import deque

N, M, X = map(int, input().split())

graph = [[] for _ in range(N)]  # 隣接リスト

for _ in range(M):  # M本の辺の情報を受け取る
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)  # 無向グラフなので両方向に辺を張る

for i in range(N): # 隣接リストをソート(小さい順に取り出すため)
    graph[i].sort()

q = deque()
q.append(X - 1)  # 頂点Xをキューに追加
unvisited = [True] * N  # 未訪問かどうかを記録する配列
unvisited[X - 1] = False    # 頂点Xは訪問済み
while q:    # 幅優先探索
    now = q.popleft()   # キューの先頭を取り出す
    print(now + 1)  # 出力
    for nxt in graph[now]:  # 隣接する頂点を調べる
        if unvisited[nxt]:  # 未訪問の場合
            unvisited[nxt] = False  # 訪問済みにする
            q.append(nxt)   # 頂点nxtをキューに追加