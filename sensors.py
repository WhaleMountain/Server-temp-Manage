import re
import subprocess
import smtplib
from email.mime.text import MIMEText
import datetime

def sensors():#コマンド実行, 実行結果を返す
    return subprocess.check_output("sensors").decode()

def get_temp():#テキストからcpuの温度のみを取得
    res = sensors()
    temp = res.split()
    cnt = 0
    for i in temp:
        if i == "temp1:":
            cnt += 1
            break
        else:
            cnt +=1
    return float(re.sub(r'\D','',temp[cnt]))/10

def judge(temp): #管理者にメールを送信するかの判定
    send = 0     #1の時メールを送信する
    warning = 0  #1の時シャットダウンする
    time = datetime.datetime.today()
    time = time.strftime("%Y-%m-%d")

    if temp >= 90.0:
        send = 1
        warning = 1
        sub = "Warning "+time
        s_msg = "Warning: The computer temperature is high.\nTherefore, shutdown the computer.\nCPU_temp:"+str(temp)
    elif temp >= 60.0:
        send = 1
        sub = "Attention "+time
        s_msg = time+"\nAttention: The computer temperature is high.\nCPU_temp:"+str(temp)

    if send == 1:
        send_mail(sub,s_msg,warning)

def send_mail(sub,s_msg,warning):#メール転送設定, メール送信
    #タイトル, 送信元, 送信先, メッセージの代入
    jp = "iso-2022-jp" #日本語の送信可能にするおまじないの文字
    msg = MIMEText(s_msg.encode(jp),"plain",jp,)
    msg["Subject"] = sub
    msg["From"] = "root@whalemountain.com"
    msg["To"] = "mk@whalemountain.com"

    #SMTPサーバ指定, 送信
    server = smtplib.SMTP("whalemountain.com")
    server.send_message(msg)

    #cpuの温度が90℃以上の場合実行される
    if(warning): 
        shutdown()

def shutdown(): #cpuの温度が90℃以上の場合実行される
    cmd = ["shutdown", "-h", "now"]
    subprocess.check_call(cmd)

if __name__ == "__main__":
    temp = get_temp()
    judge(temp)