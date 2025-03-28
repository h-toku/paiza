import sys

# 再帰の最大深さを増やし、大きなグラフでもスタックオーバーフローを防ぐ
sys.setrecursionlimit(10 ** 6)

def dfs(now: int, num: int):
    """
    現在のノード 'now' に対して DFS を実行し、'num' の色を付けて隣接ノードを再帰的に探索する。

    now: 現在のノード
    num: 現在ノードに割り当てる色 (1 または -1)
    """
    color[now] = num  # ノード 'now' に色を割り当てる
    for i in range(len(graph[now])):
        if color[graph[now][i]] == 0:  # 隣接ノードが未訪問なら
            dfs(graph[now][i], -num)  # 隣接ノードに対して反対の色を付けて探索
        else:
            if color[now] == color[graph[now][i]]:  # 同じ色の隣接ノードがあれば二部グラフではない
                global ok
                ok = False  # 二部グラフでないことが確認された


# --- 入力の受け取り ---
N, M = map(int, input().split())

# グラフの隣接リストを作成
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1  # 1-indexed → 0-indexed に変換
    b -= 1  # 1-indexed → 0-indexed に変換
    graph[a].append(b)  # ノード a からノード b へ辺を追加
    graph[b].append(a)  # ノード b からノード a へ辺を追加（無向グラフ）

ok = True  # 二部グラフかどうかを判定するフラグ

color = [0] * N  # ノードの色を管理するリスト (0: 未訪問, 1: 色1, -1: 色2)
for i in range(N):
    if color[i] == 0:  # 未訪問のノードに対して DFS を実行
        dfs(i, 1)  # 最初のノードに色1を割り当てて探索を開始

if ok:
    print("Yes")  # 二部グラフであれば "Yes" を出力
else:
    print("No")  # 二部グラフでなければ "No" を出力
