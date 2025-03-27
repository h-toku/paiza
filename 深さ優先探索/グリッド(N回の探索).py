#グリッドの行数 H と列数 W とマス (y,x) が与えられる
#深さ優先探索で Nママス移動した後にいるマスの座標を順に出力

H, W, y, x = map(int, input().split())

def dfs(times: int, y: int, x: int):
    if times == N:  # 終了条件
        print(y, x) # 出力
    else:
        if 0 <= y - 1:  #グリッドの上に移動できれば、移動して再帰呼び出し
            dfs(times + 1, y - 1, x)
        if x + 1 < W:   #グリッドの右に移動できれば、移動して再帰呼び出し
            dfs(times + 1, y, x + 1)        
        if y + 1 < H:   #グリッドの下に移動できれば、移動して再帰呼び出し
            dfs(times + 1, y + 1, x)
        if 0 <= x - 1:  #グリッドの左に移動できれば、移動して再帰呼び出し
            dfs(times + 1, y, x - 1)


dfs(0, y, x)    # 深さ優先探索の呼び出し0回目からスタート