# shellのechoコマンド


# echoコマンドは画面に文字列を表示するコマンドだ。
# echoの使い方
# echo [オプション]　[文字列」] 

# 例）”Hello, World"を表示する
echo "Hello, World"
# その結果：Hello, World

# 変数を表示する
# 例） 変数（number）に数（１００)を保存した後出力する
a=1200
echo $a
# その結果：1200

# 複数の変数を表紙する
# 例）　変数（menu&price)を表紙
menu=bread
price=500
echo order: $menu And Its price: $price
# その結果: order: bread And Its price: 500

#　計算値を表示する
#  `expr  \＜計算値＞`で計算値を囲む。
# 例）　breadが３個の場合を表紙
n=3
echo order: $menu number: $n And Its price: `expr $price \* $n` 
# その結果： order: bread number: 3 And Its price: 1500

:<<'END'
echoコマンドのオプション
-n // 改行を挿入しない 
-e // バックスラッシュでのエスケープを解釈する
-E // バックスラッシュでのエスケープを解釈しない
END

# 例）　上のオプションを使って"Hello World\n my friends"を画面に表紙

# -nの場合
echo -n "Hello World\n my friends"
# その結果: Hello World\n my friends$

# -eの場合
echo -e "Hello World\n my friends" 
# その結果: HEllo World
#          my friends

# -Eの場合
echo -E "Hello World\n my firends"
#　その結果: Hello World\n my firends


# ファイルにechoの内容を出力する
# ファイルにechoの内容を作成・上書き
# 例） abc.txtのファイルに”abc"を入力
echo 'abc' > abc.txt

# ファイルにechoの内容を追加する
# 例） abc.txtのファイルに”abc”を追加
echo 'abc' >> a.txt
