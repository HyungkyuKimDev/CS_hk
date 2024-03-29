# - find
# findはファイル・ディレクトリーを探すコマンドだ。

# 使い方1)find <位置＞　<ファイル名＞ // その名前ファイルを探す。
find find.sh
# その結果: find.shの存在を表示
# ない場合は No such file or directoryが表示

# 使い方2)find <位置＞　<*ファイル名＞ // その名前を含むファイルを探す。
find find*
# その結果: findを名前で含むファイルの存在を表示

# 使い方3)find -mtime <日数＞ // その日数間更新されたファイルを探す。
find -mtime -1
# その結果: １日以内に更新されたファイルを探す。

# 使い方4)find -name <ファイル・ディレクトリー名＞ // その名前を含むファイル・ディレクトリーを探す。
find -name find
# その結果: その名前を含むファイル・ディレクトリーを表示
# ファイルだけの場合　-type f　・　ディレクトリーだけの場合　-type d
