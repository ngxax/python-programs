# データ可視化プログラム

import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
from matplotlib import rcParams

# 日本語フォント設定

def create_pie_chart(df, save_path='pie_chart.png'):
    """所属ごとの参加者数を円グラフで表示"""
    # 所属ごとの参加者数をカウント
    department_counts = df['所属'].value_counts()
    
    # 円グラフを作成
    plt.figure(figsize=(10, 8))
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    
    wedges, texts, autotexts = plt.pie(
        department_counts.values,
        labels=department_counts.index,
        autopct='%1.1f%%',
        colors=colors,
        startangle=90,
        textprops={'fontsize': 12}
    )
    
    # タイトルとレイアウト
    plt.title('所属ごとの参加者数分布', fontsize=16, fontweight='bold', pad=20)
    plt.axis('equal')
    
    # 凡例を追加
    plt.legend(wedges, [f'{dept}: {count}人' for dept, count in department_counts.items()],
               title="所属別参加者数",
               loc="center left",
               bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"円グラフを {save_path} に保存しました")

def create_bar_chart(df, save_path='bar_chart.png'):
    """所属ごとの平均スコアを棒グラフで表示"""
    # 所属ごとの平均スコアを計算
    department_scores = df.groupby('所属')['スコア'].agg(['mean', 'max', 'min']).round(2)
    
    # 棒グラフを作成
    fig, ax = plt.subplots(figsize=(12, 8))
    
    x = np.arange(len(department_scores.index))
    width = 0.25
    
    bars1 = ax.bar(x - width, department_scores['mean'], width, 
                   label='平均スコア', color='#66b3ff', alpha=0.8)
    bars2 = ax.bar(x, department_scores['max'], width, 
                   label='最高スコア', color='#99ff99', alpha=0.8)
    bars3 = ax.bar(x + width, department_scores['min'], width, 
                   label='最低スコア', color='#ff9999', alpha=0.8)
    
    # グラフの設定
    ax.set_xlabel('所属', fontsize=12, fontweight='bold')
    ax.set_ylabel('スコア', fontsize=12, fontweight='bold')
    ax.set_title('所属ごとのスコア統計', fontsize=16, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(department_scores.index)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # 各バーの上に数値を表示
    def add_value_labels(bars):
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                   f'{height}', ha='center', va='bottom', fontsize=10)
    
    add_value_labels(bars1)
    add_value_labels(bars2)
    add_value_labels(bars3)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"棒グラフを {save_path} に保存しました")

def create_histogram(df, save_path='histogram.png'):
    """全参加者のスコア分布をヒストグラムで表示"""
    # ヒストグラムを作成
    plt.figure(figsize=(12, 8))
    
    # スコアの統計情報を計算
    scores = df['スコア']
    mean_score = scores.mean()
    std_score = scores.std()
    
    # ヒストグラムを描画
    n, bins, patches = plt.hist(scores, bins=15, alpha=0.7, color='skyblue', 
                                edgecolor='black', linewidth=0.5)
    
    # 平均線を追加
    plt.axvline(mean_score, color='red', linestyle='--', linewidth=2, 
                label=f'平均: {mean_score:.1f}')
    
    # グラフの設定
    plt.xlabel('スコア', fontsize=12, fontweight='bold')
    plt.ylabel('人数', fontsize=12, fontweight='bold')
    plt.title('全参加者のスコア分布', fontsize=16, fontweight='bold', pad=20)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 統計情報をテキストで表示
    stats_text = f'平均: {mean_score:.1f}\n標準偏差: {std_score:.1f}\n最小値: {scores.min()}\n最大値: {scores.max()}'
    plt.text(0.02, 0.98, stats_text, transform=plt.gca().transAxes, 
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"ヒストグラムを {save_path} に保存しました")

def main():
    """メイン関数"""
    try:
        # CSVファイルを読み込み
        df = pd.read_csv('課題3.csv', encoding='utf-8')
        
        print("=== データ可視化プログラム ===")
        print(f"データファイル: 課題3.csv")
        print(f"総レコード数: {len(df)}件")
        print(f"所属の種類: {df['所属'].unique()}")
        print("=" * 50)
        
        # データの基本統計を表示
        print("\n📊 データ概要")
        print(f"スコア統計:")
        print(f"  平均: {df['スコア'].mean():.2f}")
        print(f"  中央値: {df['スコア'].median():.2f}")
        print(f"  標準偏差: {df['スコア'].std():.2f}")
        print(f"  最小値: {df['スコア'].min()}")
        print(f"  最大値: {df['スコア'].max()}")
        
        print(f"\n所属別参加者数:")
        for dept, count in df['所属'].value_counts().items():
            print(f"  {dept}: {count}人")
        
        # グラフを作成
        print("\n📈 グラフ作成中...")
        
        # 1. 円グラフ
        print("1. 円グラフを作成中...")
        create_pie_chart(df)
        
        # 2. 棒グラフ
        print("2. 棒グラフを作成中...")
        create_bar_chart(df)
        
        # 3. ヒストグラム
        print("3. ヒストグラムを作成中...")
        create_histogram(df)
        
        print("\n✅ すべてのグラフが作成され、画像ファイルとして保存されました！")
        print("保存されたファイル:")
        print("  - pie_chart.png (円グラフ)")
        print("  - bar_chart.png (棒グラフ)")
        print("  - histogram.png (ヒストグラム)")
        
    except FileNotFoundError:
        print("エラー: 課題3.csv ファイルが見つかりません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
