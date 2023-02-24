#shellの条件分岐 と 繰り返し処理 を組み合わせるwhile文

# while文は指定された条件式がtrueの場合、繰り返し処理を実行するし、条件式がfalseの場合は繰り返しを終了する。

:<<"END"
#while文の使い方
while 条件式
do
  繰り返し
done

＃条件式(gは大きい lは小さい eは同じを意味)
gt // >
lt // <
ge // >=
le // <=
eq // ==
ne // !== 
END

#　例）　１から１０まで繰り返し処置（条件式は変数iが１０ではない）
i=1
while [ $i -ne 11 ] #条件式(変数iが１０になるまで繰り返す）
do
  echo $i
  ((i++))
done
    

# 条件式に:を入力すれば無限ループが実行される.
# while文の中でif文のbreakを利用すれば無限ループを止まるのが可能だ。

# 例）　jが無限に増える時、jが10になる時にbreakを利用して止まる
j=1
while :
do
  echo $j
  ((j++))

  if [ $j -eq 10 ]; then #　jが10になると止まる
    break
  fi
done