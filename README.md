lm-sensorsでCPUの温度を取得し一定度数になるとメールでの通知, 自動シャットダウン(理想)をする。

私の環境ではsensors実行後temp1に表示されるのでそちらの温度で判定をする。

人それぞれ環境が違うと思われるのでget_temp()の中身は変更してください。

以下参考にしたサイト

Python3で日本語のメールを送信

https://qiita.com/ColdFreak/items/1294258400f3ef149c3b

python上でunixコマンドを実行する

https://qiita.com/tdrk/items/9b23ad6a58ac4032bb3b

pythonで文字列から数字だけ取り出す

https://qiita.com/sakamossan/items/161db7418ade037f6f3d