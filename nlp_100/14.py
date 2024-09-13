import sys

# 先頭N行を表示するプログラム
def head(file_path, N):
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if i >= N:
                break
            print(line.strip())

# コマンドライン引数の処理
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_path> <N>")
    else:
        file_path = sys.argv[1]  # ファイルのパス
        N = int(sys.argv[2])     # 表示する行数
        head(file_path, N)
