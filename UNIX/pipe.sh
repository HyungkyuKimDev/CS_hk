#　shellのpipe

:<<"END"
shellのpipe

1。shellのpipeとは
２。shellのpipeの使い方
END

# １。shellのpipeとは
# Linuxのコマンドを使っえ標準出力された内容をpipe（｜）の後のコマンドでも処理されるようにするコマンドだ。

# 2。shellのpipeの使い方
# 使うコマンドの中で｜（pipe)を入れて使う
# 例）コマンド１　｜　コマンド２　｜　コマンド３　｜　... ｜ コマンドN

# 例）lsのコマンドで行数を出力した後、wc　-lでその行数素カウントする・。
ls | wc -l
#　その結果：１（ファイルが１つ）

# pipeのteeコマンド
# teeコマンドはpipeで処理を共にする時に使う。

# 例）ls -lコマンドでls.txtにファイルにそのコマンドの結果を入れたと共にwc -lで行数をカウントする。
ls -l | tee ls.txt | wc -l
# その結果:ls.txtファイルにls -lの結果があり、行数（２）が出力