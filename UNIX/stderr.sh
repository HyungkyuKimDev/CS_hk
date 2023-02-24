# リダイレクト

:<<"END"
リダイレクトは
Unixでコマンドの実行結果（stdout)・エラー結果(stderr)の出力・データ入力元(stdin)をデフォルトから変更すること

Unixにはファイルディスクリプタというものがり、プロセスと使用するファイルとを結び付けている。
あるプロセスがファイルを作成する場合、必ずプロセスはそのファイルを使ってファイルへアクセスしている。
ファイルディスクリプタは０〜２に数値で表現する。
1 標準入力　stdin
2 標準出力　stdout
3 標準エラー　stderr
END

:<<"END"
stderrとは

１。エラーの内容を出力する標準エラー出力。標準エラーだけ出力したい場合は[2>]を使う。
２。標準エラーと標準出力を共にする場合、＆を使って２つの出力先を同じにする。
END

# 例１-1）存在しない”A.txt"ファイルの確認する命令で標準エラーが出力
ls -l A.txt > stdout.txt # A.txtは存在しないのでエラーが出力される。
#　その結果：ls:A.txt: No such file or directory）出力

# 例１-2)上の＞代わりに２＞を使う場合
ls -l B.txt 2> stdout2.txt
#　その結果：stdout2.txtのファイルの中で（ls:B.txt: No such file or directory）がある

#　例２）＆を使うと標準エラーと標準出の出力先を同じになる。
ls -l C.txt stdout3.txt > stdout3.txt 2>&1
:<<"END"
その結果：
stdout3.txtの中
ls: C.txt: No such file or directory
-rw-r--r--  1 khk36  staff  0  2 21 18:55 stdout3.txt
END
