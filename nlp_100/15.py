import sys

# 末尾N行を表示するプログラム
def tail(file_path, N):
    with open(file_path, 'r') as file:
        lines = file.readlines()  # 全ての行をリストとして読み込む
        for line in lines[-N:]:   # 末尾からN行だけスライスして表示
            print(line.strip())

# コマンドライン引数の処理
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_path> <N>")
    else:
        file_path = sys.argv[1]  # ファイルのパス
        N = int(sys.argv[2])     # 表示する行数
        tail(file_path, N)
