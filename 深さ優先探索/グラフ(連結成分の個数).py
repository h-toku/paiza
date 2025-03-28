import sys

# 再帰の最大深さを増やし、大きなグラフでもスタックオーバーフローを防ぐ
sys.setrecursionlimit(10 ** 6)

def dfs(now: int, num: int):
    color[now] = num  # ノード 'now' に色（または成分番号）を割り当てる
    for i in range(len(graph[now])):
        if color[graph[now][i]] == -1:  # 未訪問の隣接ノードがあれば
            dfs(graph[now][i], num)  # 再帰的に DFS を実行

N, M = map(int, input().split())  # 頂点数 N、辺の数 M

# グラフの隣接リストを作成
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1  # 1-indexed → 0-indexed に変換
    b -= 1  # 1-indexed → 0-indexed に変換
    graph[a].append(b)  # ノード a からノード b へ辺を追加
    graph[b].append(a)  # ノード b からノード a へ辺を追加（無向グラフ）

ans = 0  # 連結成分の数
color = [-1] * N  # 各ノードの訪問状態（-1 は未訪問）
for i in range(N):
    if color[i] == -1:  # 未訪問のノードがあれば
        dfs(i, ans)  # そのノードから DFS を開始
        ans += 1  # 新しい連結成分が見つかったので、連結成分番号を増やす

print(ans)  # 連結成分の数を出力
