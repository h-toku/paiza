# Problem: 幅優先探索（無向グラフ）
#　N頂点の無向グラフが与えられる。
# 頂点 X から 頂点 Y へ最短経路で移動したときに通過する
# 頂点の番号を X , Y を含めて通る順に出力してください。

from collections import deque

N, X, Y = map(int, input().split())

graph = [[] for _ in range(N)]  # 隣接リスト

for _ in range(N - 1):  # 木なので辺はN-1本
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)  # 無向グラフなので両方向に辺を張る

l = [-1] * N    # 頂点iまでの距離を記録する配列
l[X - 1] = 0    # 頂点Xまでの距離は0
q = deque()    # 幅優先探索のキュー
q.append(X - 1)   # 頂点Xをキューに追加
prev = [-1] * N   # どのノードから来たかを記録する配列(距離だけなら不要)

while q:
    now = q.popleft()  # キューの先頭を取り出す
    if now == Y - 1:   # 頂点Yに到達した場合
        break   # 探索を終了
    for nxt in graph[now]: # 隣接する頂点を調べる
        if l[nxt] == -1:    # 未訪問の場合
            l[nxt] = l[now] + 1    # 頂点nxtまでの距離を記録
            prev[nxt] = now   # どのノードから来たかを記録(距離だけなら不要)
            q.append(nxt)   # 頂点nxtをキューに追加

#距離だけならprint(l[Y - 1])でOK
#たどりつけない場合は-1を出力

tmp = Y - 1  # 頂点Yから逆にたどっていく
ans = []    # 答えを格納する配列
while tmp != -1:    # 頂点Xに到達するまで繰り返す
    ans.append(tmp) # 答えに頂点tmpを追加
    tmp = prev[tmp] # どのノードから来たかをたどる

for i in ans[::-1]: # 答えを逆順に出力[開始:終了:ステップ]
    print(i + 1)