import sys
import math

# ファイルを行単位でN分割するプログラム
def split_file(file_path, N):
    with open(file_path, 'r') as file:
        lines = file.readlines()  # ファイルの全行をリストに読み込む
        total_lines = len(lines)
        lines_per_file = math.ceil(total_lines / N)  # 各ファイルに含まれる行数を計算

        # ファイルを分割して書き込み
        for i in range(N):
            start = i * lines_per_file
            end = min(start + lines_per_file, total_lines)
            with open(f"split_{i+1}.txt", 'w') as output_file:
                output_file.writelines(lines[start:end])
            print(f"split_{i+1}.txtに行数 {start+1} から {end} を書き込みました。")

# コマンドライン引数の処理
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_path> <N>")
    else:
        file_path = sys.argv[1]  # ファイルのパス
        N = int(sys.argv[2])     # 分割数
        split_file(file_path, N)
