def hangman(word):
    wrong = 0
    life=7
    stages = ["",
              "_______      ",
              "|            ",
              "|      |     ",
              "|      0     ",
              "|     /|\    ",
              "|     / \    ",
              "|            "
              ]
    rletters = list(word)  #入力したワードをリストに変換
    board = ["_"] * len(word) #入力した文字の数だけ下線を示そう
    win = False
    while wrong < len(stages) - 1: #len(stages)=8
        print("\n") #double spacing
        msg = "1文字を予想してね! "
        char = input(msg)
        if char in rletters: #もし入力した文字が正解の中にあったら
            for i in range(len(rletters)):
                if rletters[i]==char:
                    board[i]=char
                    rletters[i]='$'
                else:
                    continue
            #cind = rletters.index(char) #正解の中にあった文字のインデックス番号
            #board[cind] = char #下線を正解した文字に入れ替える！
            #rletters[cind] = '$' #文字があった場所はもう変えておく
        else:
            life-=1
            wrong += 1
        print(" ".join(board)) #１ターンが終わったらそこまでの結果を示す
        print(f"残りライフ{life}")
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board: #もし下線が残っていなかったら勝ちとなる
            print("\nあなたの勝ち!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("あなたの負け!正解は {}.".format(word))


print("ハングマンへようこそ!")
hangman(input())
