import sys

# 再帰の最大深さを増やし、大きなグラフでもスタックオーバーフローを防ぐ
sys.setrecursionlimit(10 ** 6)


def dfs(now: int):
    """
    深さ優先探索（DFS）を実行する関数

    now: 現在のノード（0-indexed）
    """
    unvisited[now] = False  # 訪問済みマークをつける
    print(now + 1)  # 1-indexed でノードを出力

    # 現在のノードに隣接するノードを順に探索
    for next_node in graph[now]:
        if unvisited[next_node]:  # 未訪問なら探索
            dfs(next_node)  # 再帰的に DFS を実行


# --- 入力の受け取り ---
N, M, X = map(int, input().split())  # 頂点数 N、辺の数 M、開始ノード X（1-indexed）
X -= 1  # 1-indexed → 0-indexed に変換

# グラフを隣接リストで構築（無向グラフ）
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1  # 1-indexed → 0-indexed に変換
    b -= 1  # 1-indexed → 0-indexed に変換
    graph[a].append(b)
    graph[b].append(a)

# 各ノードの隣接リストを辞書順（小さい番号順）にソート
for i in range(N):
    graph[i].sort()

# 訪問管理リスト（True: 未訪問, False: 訪問済み）
unvisited = [True] * N

# X を開始点として DFS を実行
dfs(X)
