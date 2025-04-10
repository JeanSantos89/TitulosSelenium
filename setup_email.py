import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Carrega variáveis do .env (Endereço de Email e Senha do aplicativo GMAIL)
load_dotenv()

# Armazena login e senha de forma seguro
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Configurações do servidor
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# define função que configura email
def config_email(para, assunto, corpo):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = para
        msg['Subject'] = assunto
        msg.attach(MIMEText(corpo, 'plain'))

        # Conexão e envio usando SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo() 
            server.starttls()  
            server.ehlo()  
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, para, msg.as_string())

        print("EMAIL ENVIADO")
    except Exception as e:
        print(f"ERRO AO ENVIAR EMAIL: {e}")

# Formata o assunto e corpo do e-mail antes de chamar a função de configuração/envio.
def enviar_email(destinatario, tipo_livro, TitulosLivros):
    para = destinatario
    assunto = f"Títulos dos livros - Categoria: {tipo_livro}"
    corpo = "\n".join(TitulosLivros)
    config_email(para, assunto, corpo)
