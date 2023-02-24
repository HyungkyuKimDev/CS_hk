#if 引数が”ok”の場合実
if [ $1 == "ok" ] 
then
  # ok.txt ファイルに（Your input is ok right??)という標準出力が リダイレクト
  echo "Your input is $1 right??" > ok.txt
#引数が”ng”の場合 
elif [ $1 == "ng" ]
then
  # ng.txt ファイルに（ls: A.txt: No such file or directory）という標準エラーがリダイレクト
  ls -l A.txt 2> ng.txt 
fi
