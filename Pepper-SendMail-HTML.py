import sys, os
import smtplib, email
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText

def mail(email_user, to, subject, text, attach, email_pwd, smtp, port):
  msg = email.MIMEMultipart.MIMEMultipart('alternative')
  msg['From'] = email_user
  msg['To'] = to
  msg['Subject'] = subject

  msg.attach(email.MIMEText.MIMEText(text, 'html'))
  #part1 = MIMEText(text, 'html')
  #msg.attach(part1)

  if attach:
     part = email.MIMEBase.MIMEBase('application', 'octet-stream')
     part.set_payload(open(attach, 'rb').read())
     email.Encoders.encode_base64(part)
     part.add_header('Content-Disposition',
             'attachment; filename="%s"' % os.path.basename(attach))
     msg.attach(part)

  if( port != "" ):
      mailServer = smtplib.SMTP(smtp, port)
  else:
      mailServer = smtplib.SMTP(smtp)
  mailServer.ehlo()
  mailServer.starttls()
  mailServer.ehlo()
  mailServer.login(email_user, email_pwd)
  mailServer.sendmail(email_user, to, msg.as_string())

  mailServer.close()

class MyClass(GeneratedClass):
  def __init__(self):
    GeneratedClass.__init__(self, False)

  def onLoad(self):
    pass

  def onUnload(self):
    #puts code for box cleanup here
    pass

  def onInput_onSend(self):
    sEmailUser = self.getParameter("From")
    aTo = self.getParameter("To").split(";")
    sSubject = self.getParameter("Subject")
    #sText = self.getParameter("Contents")
    sAttachedFilePath = self.getParameter("Attachment")
    sPwd = self.getParameter("Password")
    sSmtp = self.getParameter("SMTP address")
    sPort = int( self.getParameter("Port number") )
    sText = """\
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

    if p:
        sName = "<p>"
        sName += str(p)
        sName += "さんを見つけました。</p>"
        sText += sName
    sTime = datetime.now().strftime("<p>通知日時：%Y/%m/%d %H:%M:%S</p>")
    sText += sTime

    sText += """\
                              </td>
                          </tr>
                      </table>
                  </td>
              </tr>
          </table>
      </body>
    </html>
    """
    try:
        sPort = int( sPort )
        bValidPort = ( sPort >= 0 and sPort <= 65535 )
    except:
        bValidPort = False
    if( not bValidPort ):
        raise Exception( str(sPort) + " is not a valid port number to use to send e-mail. It must be an integer between 0 and 65535. Please check that the port parameter of the box is correct." )
    for address in aTo:
      try:
        mail(
          sEmailUser,
          address,
          sSubject,
          sText,
          sAttachedFilePath,
          sPwd,
          sSmtp,
          sPort)
      except smtplib.SMTPAuthenticationError as e:
        raise(Exception("Authentication error, server answered : [%s] %s" % (e.smtp_code, e.smtp_error)))


    self.onSent() # activate output of the box
