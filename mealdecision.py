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
main = ["鶏のソテー","豚肉のソテー","刺身","ハンバーグ","からあげ","焼き魚", "焼肉","餃子","魚のムニエル", "魚の揚げ物"]  #Fish meat
sub = ["ほうれん草のお浸し","ほうれん草バター炒め","ひじき煮","ベビーリーフのサラダ","中華風炒め物","野菜炒め", "きのこ料理", "サラダ"]   #salad
carbo = ["白いご飯","パスタ", "パン","うどん", "そば"]  #rice katofeln
soup = ["みそ汁", "トン汁","ポトフ","わかめの中華スープ","卵の中華スープ"]  #miso soup


while True:
    """This loop is highly controversial I assume"""
    try:
        run_mode = int(input("適当に一品表示・・・1, バランスの取れた献立を表示・・・2"))
        break
    except:
        try:
            run_mode = int(input("数値で入力してください。適当に一品表示・・・1, バランスの取れた献立を表示・・・2"))
            break
        except:
            continue
if run_mode == 1:
    stopper = 0
    while stopper == 0:
        randomizer = random.randint(0,len(gohan)-1)
        gohandecided = gohan[randomizer]
        print(gohandecided)
        while True:
            try:
                input1 = int(input("決まったら1を入力、もう一回抽選するなら適当に数値を入力"))
                break
            except:
                try:
                    input1 = int(input("数値で入力してください。"))
                    break
                except:
                    continue

        if input1 == 1:
            stopper = 1
            print("献立は{}に決定".format(gohandecided))
        else:
            pass
elif run_mode == 2:
    stopper = 0
    while stopper == 0:
        r_main = random.randint(0,len(main)-1)
        r_sub  = random.randint(0,len(sub)-1)
        r_carbo = random.randint(0,len(carbo)-1)
        r_soup = random.randint(0,len(soup)-1)
        menu = "主食 : {}\n主菜 : {}\n副菜 : {}\n汁物 : {}".format(carbo[r_carbo],main[r_main],sub[r_sub],soup[r_soup])
        print(menu)
        input1 = int(input("変更しますか？ y = 1, N = 2"))
        if input1 == 1:
            continue
        else:
            stopper = 1 
