# - curl
# curlはプロトコルを利用してURLで示されるネットワーク上の場所との間でデータの送受信するコマンドだ。

# 使い方1)curl ipinfo.io // 自分のグローバルIPを確認
curl ipinfo.io
# その結果：自分のIP/CITY/REGION... etcが出力

# 使い方2)curl ＜サイトのURL＞ // サイトをGETする
curl https://www.google.com/ 
# その結果：GOOGLEのサイトをGETする。

# 使い方3)curl -o <出力パス＞　<サイトのURL> // GETしたそのサイトの内容をHTMLに出力
curl -o /Users/khk36/Desktop/Pg/bootcamp/shell/google.html https://www.google.com/ 
# その結果：GOOGLEのサイトの情報を自分のHTMLファイルにもらう。

# 使い方4) curl -d <KEY VALUE> <サイトのURL＞ // KEYとVALUEをサイトにPOST（送信）する
curl -d "company=GOOGLE" https://www.google.com/ 
# その結果：company=GOOGLE 内容をGOOGLEに送信
