#shellの繰り返し処理

:<<"END"
shellの繰り返し処理
1.shellのfor文
2.shellのfor文にseqを使う方法
END

# shellのfor文
# shellのfor文は指定した回数まで繰り返す方法だ。

:<<"END"
for 変数　in リスト
do
  繰り返し処理
done
#リストの数（指定された回数）まで変数を利用して繰り返し処理をする。
END

# 1から１０までの表示を繰り返しのfor文
for i in 1 2 3 4 5 6 7 8 9 10
do 
  echo $i
done

:<<"END"
その結果
:
1
2
3
4
5
6
7
8
9
10
END

# 文字列を繰り返すこと・変数を指定することも可能
# 例）i1 i2 i3 i4 i5 にそれぞれcake1 cake2 ... cake5を指定した後、繰り返す。
l1=cake1
l2=cake2
l3=cake3
l4=cake4
l5=cake5

for i in $l1 $l2 $l3 $l4 $l5
do
  echo $i
done

:<<"END"
その結果
:
cake1
cake2
cake3
cake4
cake5
END

# shellのfor文にseqを使う方法

# seqで回数を指定できる。
# リストの代わりに`seq 数`を入力する。

# 例）上の１から１０までの繰り返すのをseqを利用して作成
for i in `seq 10`
do
  echo $i
done

#　その結果は上と同じ  
