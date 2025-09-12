# 簡単な計算機プログラム

def main():
    """四則演算を行う計算機"""
    print("=== 簡単な計算機 ===")
    
    try:
        # 最初の数値を入力
        num1 = float(input("最初の数値を入力してください: "))
        
        # 四則演算子を入力
        operator = input("演算子を入力してください (+, -, *, /): ")
        
        # 2番目の数値を入力
        num2 = float(input("2番目の数値を入力してください: "))
        
        # 計算を実行
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("エラー: ゼロで割ることはできません")
                return
            result = num1 / num2
        else:
            print("エラー: 無効な演算子です。+, -, *, / のいずれかを入力してください")
            return
        
        # 結果を表示
        print(f"結果: {num1} {operator} {num2} = {result}")
        
    except ValueError:
        print("エラー: 数値を正しく入力してください")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
