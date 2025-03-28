from collections import deque


def dfs(now: int):
    """
    深さ優先探索 (DFS) を用いて X から Y までの距離を測る関数

    now: 現在のノード（0-indexed）
    """
    global dfs_count  # DFS で Y に到達するまでのステップ数をカウントするための変数
    dfs_unvisited[now] = False  # 現在のノードを訪問済みにする

    # Y にまだ到達していない場合にカウントを増やす
    if dfs_unvisited[Y]:  
        dfs_count += 1

    # 隣接ノードを探索（辞書順の小さい順）
    for next_node in graph[now]:
        if dfs_unvisited[next_node]:  # 未訪問なら探索
            dfs(next_node)


# --- 入力の受け取り ---
N, X, Y = map(int, input().split())  # 頂点数 N、開始ノード X、目標ノード Y（1-indexed）
X -= 1  # 1-indexed → 0-indexed に変換
Y -= 1  # 1-indexed → 0-indexed に変換

# グラフの構築（隣接リスト）
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1  # 1-indexed → 0-indexed に変換
    b -= 1  # 1-indexed → 0-indexed に変換
    graph[a].append(b)
    graph[b].append(a)

# 各ノードの隣接リストを辞書順（小さい番号順）にソート
for i in range(N):
    graph[i].sort()

# 訪問管理用リスト（DFS と BFS で別々に管理）
dfs_unvisited = [True] * N
bfs_unvisited = [True] * N

# DFS の探索ステップ数
dfs_count = 0
dfs(X)  # DFS を実行

# BFS の探索
bfs_count = 0
q = deque([X])  # BFS 用のキュー（最初に X を追加）
bfs_unvisited[X] = False  # 開始ノードを訪問済みにする

while q:
    now = q.popleft()  # キューの先頭からノードを取得（FIFO: 先入れ先出し）

    # 目標ノード Y に到達したら探索終了
    if now == Y:
        break
    else:
        bfs_count += 1  # まだ到達していない場合、探索カウントを増やす

    # 隣接ノードを探索
    for next_node in graph[now]:
        if bfs_unvisited[next_node]:  # 未訪問なら探索
            bfs_unvisited[next_node] = False
            q.append(next_node)  # キューに追加（次の探索対象）

# BFS と DFS の比較
if bfs_count < dfs_count:
    print("bfs")  # BFS の方が短い（最短経路）
elif bfs_count == dfs_count:
    print("same")  # 両者の経路長が同じ
else:
    print("dfs")  # DFS の方が短い（通常はありえないが、誤実装の可能性）
