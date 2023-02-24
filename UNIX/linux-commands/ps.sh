# - ps
# psはプロセス情報・PID(Process ID)を確認するコマンドだ。

# 使い方1)ps // 現在シェルで実行中のプロセスを出力
ps
# その結果：プロセスのPID TTY TIME CMD　が出力

# 使い方2)ps -e // 現在実行中のプロセス全て出力
ps -e
# その結果：上と同じ

# 使い方3)ps -f // プロセスの全ての情報を出力
ps -f 
# その結果：上の情報で UID PPID C STIME が追加されて出力

# 使い方4) ps -ef | grep <PID> // あるPIDを探す・
ps -ef | grep chrome
# その結果：上のPIDの情報が出力される。