#H,Wのグリッドが与えられる。
# 壁#か何もない.で表される
# 壁で区画が区切られているとき、その区画の数を求める



def dfs(y: int, x: int):
    S[y][x] = "#"   # 訪問済みは壁に変更
    for i in range(-1, 2, 2):   # iは-1と1
        if 0 <= y + i < H and S[y + i][x] == ".":   # 範囲内かつ壁でない
            dfs(y + i, x)   # 再帰
        if 0 <= x + i < W and S[y][x + i] == ".":   # 範囲内かつ壁でない
            dfs(y, x + i)   # 再帰


H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]   # グリッドをリストに格納

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":  # 壁でない場合にdfsを実行
            dfs(i, j)
            ans += 1

print(ans)