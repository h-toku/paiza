
#グリッドの行数 H と列数 W が与えられるので、
#マス (y,x) から次の操作を 1 回としたとき、
# N回以内に到達することができるマスを '*' , 
# それ以外のマスを '.' にしたグリッド

from collections import deque # キューのためのモジュール

H, W, N = map(int, input().split())  # グリッドの高さHと幅Wと、到達回数Nを入力
y, x = map(int, input().split())  # スタート地点(y, x)を入力

q = deque()  # BFSのためのキュー
q.append((y, x))  # スタート地点をキューに追加
l = [[-1] * W for _ in range(H)]  # 各セルの訪問状況（距離）を格納するリスト
l[y][x] = 0  # スタート地点の距離を0に設定
mp = [["."] * W for _ in range(H)]  # マップを表現するリスト（最初は全て"."）
mp[y][x] = "*"  # スタート地点に "*" を配置

while q:  # キューが空になるまでループ
    ny, nx = q.popleft()  # キューから現在の位置を取り出す
    if l[ny][nx] == N:
        continue  # 距離がNの地点をスキップ
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 上下左右の移動
        if 0 <= ny + dy < H and 0 <= nx + dx < W:  # 範囲外でないか確認
            if l[ny + dy][nx + dx] == -1:  # 未訪問の場所
                #壁の条件があればS[ny + dy][nx + dx] != "#"などをandで追加
                l[ny + dy][nx + dx] = l[ny][nx] + 1  # 現在の距離 + 1
                mp[ny + dy][nx + dx] = "*"  # 移動先に "*" を配置
                q.append((ny + dy, nx + dx))  # 新しい位置をキューに追加

for i in range(H):
    print(*mp[i], sep="")