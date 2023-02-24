# shellの引数

:<<"END"
#shellの引数
1.コマンドラインで引数をもらう方法
2.引数を変数に割り当て
3.for文を利用して引数を活用
4.引数を確認方法
END

# 1.コマンドラインで引数をもらう方法
# shellを実行する時に引数を入力すれば引数を使える
# 使い方）　bash　ファイル名.sh 引数

# もらった引数は＄1　＄2 ... ＄nで読める。＄#とはもらった引数の数
# 例）引数(10 20 30)をもらってその引数と引数の数を出力
# コマンドラインで　bash arguments.sh 10 20 30 を入力
echo $1
echo $2
echo $3
echo $#

:<<"END"
その結果
:
10
20
30
3
END

# 2.引数を変数に割り当て
# もらった引数は変数に割り当てできる。
# 使い方）　変数＝＄n

# 例）上でもらった引数（10)を変数（number1)に割り当てして出力
# コマンドラインで　bash arguments.sh 10 20 30　 
number1=$1 # number1に＄1を割り当てする
echo "number1 = $1"
:<<"END"
その結果
:
number1 = 10
END

# 3.for文を利用して引数を活用
# もらう引数の数は決まっていない時にはfor文に使える

#　例）上でもらった引数（10 20 30)をfor文に入れて出力
# コマンドラインで　bash arguments.sh 10 20 30　 
echo "Print out Arguments"
echo "Each of Arguments is"
for i in $@
do
  echo "$i"
done
:<<"END"
その結果
:
Print out Arguments
Each of Arguments is
10
20
30
END

# 4.引数を確認方法
# 引数のもらったのか貰わなかったのかを条件式を利用して確認できる。

#　使い方１) [ -z ＄引数 ]　引数の長さが０の場合Trueをreturnする。　
#　例）上でもらった引数（10 20 30)で＄1の引数をもらったのかを確認
# コマンドラインで　bash arguments.sh 10 20 30　 
echo "Is there Argument's number1 here??"
  
if [ -z $1 ]
then
  echo "No It isn't here"
else
  echo "Yes It is here"
fi
:<<"END"
その結果
:
Yes It is here
END

# 使い方２) [ -n $引数 ]　引数の長さが０の場合Falseをreturnする
# 例）上でもらったひきすう（10,20,30）でない＄４の引数をもらったのかを確認
# コマンドラインで　bash arguments.sh 10 20 30　 
echo "Second : Is There Argument's number4 here??"

if [ -n $4 ]
then
  echo "No It isn't here"
else
  echo "Yes It is here"
fi
:<<"END"
その結果
:
Yes It isn't here
END