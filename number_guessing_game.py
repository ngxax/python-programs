# 数当てゲームプログラム

import random

def main():
    """1〜100の数当てゲーム"""
    print("=== 数当てゲーム ===")
    print("コンピューターが1〜100の間の数字を選びました。")
    print("その数字を当ててみてください！")
    print("-" * 40)
    
    # ランダムな数字を生成（1〜100）
    target_number = random.randint(1, 100)
    attempts = 0  # 試行回数をカウント
    
    while True:
        try:
            # ユーザーの予想を入力
            guess = int(input("あなたの予想を入力してください (1-100): "))
            attempts += 1
            
            # 入力範囲のチェック
            if guess < 1 or guess > 100:
                print("1〜100の範囲で入力してください。")
                continue
            
            # 正解かどうかをチェック
            if guess == target_number:
                print(f"🎉 正解です！おめでとうございます！")
                print(f"答えは {target_number} でした。")
                print(f"試行回数: {attempts}回")
                break
            elif guess < target_number:
                print("📈 もっと大きい数字です！")
            else:
                print("📉 もっと小さい数字です！")
                
        except ValueError:
            print("エラー: 数値を正しく入力してください。")
        except KeyboardInterrupt:
            print("\nゲームを終了します。")
            break
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            break

if __name__ == "__main__":
    main()
