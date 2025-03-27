from collections import deque

H, W = map(int, input().split())    # グリッドの行数 H と列数 W
sy, sx = map(int, input().split())  # スタート地点の座標 sy, sx
gy, gx = map(int, input().split())  # ゴール地点の座標 gy, gx
S = [list(input()) for _ in range(H)] # グリッドの情報 S

q = deque()  # BFSのためのキュー
q.append((sy, sx))  # スタート地点をキューに追加
reachable_from_start = [[-1] * W for _ in range(H)]  
# 到達距離を記録するリスト 可否を判定するだけならbool型で十分
# reachable_from_start = [[False] * W for _ in range(H)]
reachable_from_start[sy][sx] = 0  # スタート地点の距離は0

while q:
    ny, nx = q.popleft()  # キューから現在の位置を取り出す
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 上下左右に移動
        if (0 <= ny + dy < H and 0 <= nx + dx < W):  # 範囲内か確認
            if S[ny + dy][nx + dx] != '#' and reachable_from_start[ny + dy][nx + dx] == -1:
                 # 移動先が壁でなく、未到達の場合
                reachable_from_start[ny + dy][nx + dx] = reachable_from_start[ny][nx] + 1  
                # 到達距離を更新
                q.append((ny + dy, nx + dx))  # 新しい位置をキューに追加

if reachable_from_start[gy][gx] != -1:  # ゴール地点に到達できるか
    print(reachable_from_start[gy][gx]) # 到達できるなら到達距離を出力
else:
    print("No")
