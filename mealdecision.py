import random

gohan = ["オムライス","ハンバーグ", "からあげ",
"チャーハン", "サンドイッチ", "カレー","ポトフ"
, "海鮮丼", "お好み焼き", "うどん", "そば",
 "ラーメン", "パスタ","いなり","煮物","焼き魚",
"中華風炒め物", "ステーキ", "焼肉", "餃子",
"オムレツ", "トン汁", "きのこ料理", "チーズ系",
 "魚のムニエル", "魚の揚げ物", "野菜炒め",
  "天ぷら", "ひじき系","パン系","鶏のソテー","豚肉のソテー",
  "ジャーマンポテト","ほうれん草のバター炒め",
  "刺身定食", "サラダ"]

stopper = 0
while stopper == 0:
    randomizer = random.randint(0,len(gohan)-1)
    gohandecided = gohan[randomizer]
    print(gohandecided)
    input1 = int(input("決まったら1を入力、もう一回抽選するなら適当に数値を入力"))
    if input1 == 1:
        stopper = 1
        print("献立は{}に決定".format(gohandecided))
    else:
        pass
