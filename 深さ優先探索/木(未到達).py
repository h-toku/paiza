#木を構成する 1 〜 N の番号がつけられた頂点とそれらを結ぶ辺の情報と
#頂点番号 X が与えられるので、頂点 X から次のルールにしたがって
#深さ優先探索をしたときに訪れる頂点番号を順に出力してください。
#現在の頂点に隣接している頂点のうち、未訪問かつ番号が一番小さい頂点を探索する。

def dfs(now: int):
    """
    深さ優先探索 (DFS) を実行する関数

    now: 現在のノード（0-indexed）
    """
    # 現在のノードを訪問済みにする
    unvisited[now] = False

    # 1-indexed で現在のノード番号を出力
    print(now + 1)

    # 接続されているノードを順に探索（辞書順の小さい方から）
    for i in range(len(graph[now])):
        next_node = graph[now][i]  # 隣接ノードを取得
        if unvisited[next_node]:   # まだ訪問していない場合
            dfs(next_node)         # 再帰的に DFS を実行


# --- 入力の受け取り ---
N, X = map(int, input().split())  # 頂点数 N、開始ノード X（1-indexed）

# グラフを隣接リスト（リストのリスト）として構築
graph = [[] for _ in range(N)]

# N-1 本の辺を読み込んでグラフを作成（無向グラフ）
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1  # 1-indexed → 0-indexed に変換
    b -= 1  # 1-indexed → 0-indexed に変換
    graph[a].append(b)
    graph[b].append(a)

# 各ノードの隣接リストを辞書順（小さい番号順）にソート
for i in range(N):
    graph[i].sort()

# 訪問管理用のリスト（True: 未訪問, False: 訪問済み）
unvisited = [True] * N

# X を 0-indexed に変換して DFS を開始
dfs(X - 1)

