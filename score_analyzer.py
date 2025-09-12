# スコア分析プログラム

import pandas as pd
import numpy as np

def analyze_scores(csv_file):
    """CSVファイルからスコアデータを読み込み、各参加者の統計を計算する"""
    try:
        # CSVファイルを読み込み
        df = pd.read_csv(csv_file, encoding='utf-8')
        
        print("=== スコア分析結果 ===")
        print(f"データファイル: {csv_file}")
        print(f"総レコード数: {len(df)}件")
        print("=" * 50)
        
        # 各参加者ごとの統計を計算
        participants = df['名前'].unique()
        
        results = []
        
        for participant in participants:
            # 参加者のスコアデータを抽出
            participant_data = df[df['名前'] == participant]['スコア']
            
            # 統計を計算
            mean_score = participant_data.mean()
            max_score = participant_data.max()
            min_score = participant_data.min()
            total_tests = len(participant_data)
            
            results.append({
                '名前': participant,
                '平均点': round(mean_score, 2),
                '最高点': max_score,
                '最低点': min_score,
                '受験回数': total_tests
            })
        
        # 結果を平均点で降順ソート
        results.sort(key=lambda x: x['平均点'], reverse=True)
        
        # 結果を表示
        print("📊 各参加者のスコア統計")
        print("-" * 50)
        print(f"{'順位':<4} {'名前':<10} {'平均点':<8} {'最高点':<8} {'最低点':<8} {'受験回数':<8}")
        print("-" * 50)
        
        for i, result in enumerate(results, 1):
            print(f"{i:<4} {result['名前']:<10} {result['平均点']:<8} {result['最高点']:<8} {result['最低点']:<8} {result['受験回数']:<8}")
        
        print("-" * 50)
        
        # 全体統計
        all_scores = df['スコア']
        overall_mean = all_scores.mean()
        overall_max = all_scores.max()
        overall_min = all_scores.min()
        
        print("\n📈 全体統計")
        print(f"全体平均点: {overall_mean:.2f}")
        print(f"全体最高点: {overall_max}")
        print(f"全体最低点: {overall_min}")
        
        # 科目別統計
        print("\n📚 科目別平均点")
        subject_stats = df.groupby('科目')['スコア'].agg(['mean', 'count']).round(2)
        subject_stats.columns = ['平均点', '受験者数']
        print(subject_stats)
        
        return results
        
    except FileNotFoundError:
        print(f"エラー: ファイル '{csv_file}' が見つかりません。")
        return None
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return None

def main():
    """メイン関数"""
    csv_file = "課題2.csv"
    results = analyze_scores(csv_file)
    
    if results:
        print(f"\n✅ 分析が完了しました。{len(results)}名の参加者データを処理しました。")

if __name__ == "__main__":
    main()

