# - top
# topは現在実行されているプロセスの情報（プロセスID ユーザー名　プロセス優先度 メモリ　CPU ... etc)を確認できるコマンドだ。

# 使い方1)top // 現在のプロセスの情報を確認
top
# その結果：プロセスの情報（プロセスID/ユーザー名/メモリ... etc）が出力

# 使い方2)top -n <数＞ // top命令で表示されるプロセスの数を指定
top -n 3
# その結果：３つを表示される。

# 使い方3)top -U <ユーザーの名＞ // あるユーザーのプロセスだけ表示
top -U root
# その結果：rootユーザーのプロセスを表示。

# 使い方4)top -s ＜時間＞// 内容の更新を指定された時間でする。
top -s 5
# その結果：5秒たび更新される。

# 使い方5)top | grep <あるプロセス名＞// あるプロセスを表示する。
top | gerp rcu
# その結果: rcuプロセスだけ表示される。