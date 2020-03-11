#!/usr/bin/env python3
# coding: utf-8

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime

# me == my email address
# you == recipient's email address
email_user = "mailforpepper02@gmail.com"
email_pwd = "mailforpepper"
to = "t.hirofumi@x-movjapan.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "HTMLメールテスト送信"
msg['From'] = email_user
msg['To'] = to

# Create the body of the message (a plain-text and an HTML version).
#text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
html = """\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja">
<head>
<meta name="viewport" content="width=device-width" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title></title>
<style>
    img {
        max-width: 100%;
    }
    @media only screen and (max-width: 600px) {
        .wrapper {
            width: 100% !important;
        }
    }
</style>
</head>
      <body style="margin:0;">
          <table class="wrapper" width="600" cellpadding="0" cellspacing="0" align="center">
              <tr>
                  <td class="container" style="background-color:#FFFFFF">
                      <table width="100%" cellpadding="10" cellspacing="0">
                          <tr>
                              <td>
                                  <h1 style="font-size:20px;color:red;">施設内に人を確認しました</h1>
                                  <p>巡回中に人を確認したのでPepperからメール通知します。</p>
                                  <p>添付画像を確認してください。</p>
                                  """
sName = "<p>"
sName += str("テスト")
sName += "さんを見つけました。</p>"
html += sName
sTime = datetime.now().strftime("<p>通知日時：%Y/%m/%d %H:%M:%S</p>")
html += sTime

html += """\
                              </td>
                          </tr>
                      </table>
                  </td>
              </tr>
          </table>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
#part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
#msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
#s = smtplib.SMTP('localhost')
smtp = "smtp.gmail.com"
port = 587
mailServer = smtplib.SMTP(smtp, port)
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
#s.sendmail(me, you, msg.as_string())
#s.quit()
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(email_user, email_pwd)
mailServer.sendmail(email_user, to, msg.as_string())
mailServer.quit()
