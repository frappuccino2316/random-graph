import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import random

def main():
    print("ファイルのパスを入力")
    path = input()
    df = pd.read_csv(path, encoding='shift-jis')
    print(df)
    
    random_idx_first = random.randint(0, len(df.columns)-1)
    random_idx_second = random.randint(0, len(df.columns)-1)
    pair = [random_idx_first, random_idx_second]

    plt.figure()
    df.iloc[:, [min(pair), max(pair)]].plot(kind="scatter", x=df.columns[min(pair)], y=df.columns[max(pair)], figsize=(9, 6))
    plt.savefig("fig.png")

if __name__ == "__main__":
    main()
