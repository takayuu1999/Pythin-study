# 円周の長さと円の面積の表示
import math

class Circle:
    """ 円クラス """

    # 円周率
    PI = 3.1415

    """ 円周の長さを取得 """
    def calc_circumference(self, radius: int) -> float:
        # 円周の長さを算出
        res = 2 * Circle.PI * radius
        # 
        return math.floor(res * 10 ** 3) / (10 ** 3)

    """ 円の面積を取得 """
    def calc_area(self, radius: int) -> float:
        # 円周の長さを算出
        res = Circle.PI * radius ** 2
        # 
        return math.floor(res * 10 ** 3) / (10 ** 3)

class Main:

    """ メインクラス """
    def execute(self) -> None:
        # 計算実行インスタンスの生成
        circle = Circle()

        # 半径を入力
        radius = int(input("半径を整数値で入力："))

        # 円周の長さを算出
        circumference = circle.calc_circumference(radius)

        # 円の面積を算出
        area = circle.calc_area(radius)

        # 結果を表示
        print("円周の長さは{}です。".format(circumference))
        print("円の面積は{}です。".format(area))

# メインクラスの生成とメイン処理実行
main = Main()
main.execute()