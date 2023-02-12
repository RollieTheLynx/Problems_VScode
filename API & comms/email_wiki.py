# -*- coding: utf-8 -*-
"""
http://codius.ru/articles/Python_%D0%9A%D0%B0%D0%BA_%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D1%82%D1%8C_%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE_%D0%BD%D0%B0_%D1%8D%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D1%83%D1%8E_%D0%BF%D0%BE%D1%87%D1%82%D1%83

Отправляем избранную статью недели Вики на почту
"""

import requests
from bs4 import BeautifulSoup
import smtplib
import mimetypes                                            # Импорт класса для обработки неизвестных MIME-типов, базирующихся на расширении файла
from email import encoders                                  # Импортируем энкодер
from email.mime.base import MIMEBase                        # Общий тип
from email.mime.text import MIMEText                        # Текст/HTML
from email.mime.image import MIMEImage                      # Изображения
from email.mime.audio import MIMEAudio                      # Аудио
from email.mime.multipart import MIMEMultipart              # Многокомпонентный объект
import my_keys
import os


def get_wiki():
    url = 'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
    response = requests.get(url)
    if not response.ok: # .status_code == 200:
        print(f"Code: {response.status_code}, url: {url}")
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.find('h2', class_='main-header main-box-header').text.strip()
    text = soup.find('div', id='main-tfa').findChildren("p", recursive=False)
    image = soup.find('img')['src']
    return title, text, image


def attach_file(msg, filepath):                             # Функция по добавлению конкретного файла к сообщению
    filename = os.path.basename(filepath)                   # Получаем только имя файла
    ctype, encoding = mimetypes.guess_type(filepath)        # Определяем тип файла на основе его расширения
    if ctype is None or encoding is not None:               # Если тип файла не определяется
        ctype = 'application/octet-stream'                  # Будем использовать общий тип
    maintype, subtype = ctype.split('/', 1)                 # Получаем тип и подтип
    if maintype == 'text':                                  # Если текстовый файл
        with open(filepath) as fp:                          # Открываем файл для чтения
            file = MIMEText(fp.read(), _subtype=subtype)    # Используем тип MIMEText
            fp.close()                                      # После использования файл обязательно нужно закрыть
    elif maintype == 'image':                               # Если изображение
        with open(filepath, 'rb') as fp:
            file = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
    elif maintype == 'audio':                               # Если аудио
        with open(filepath, 'rb') as fp:
            file = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
    else:                                                   # Неизвестный тип файла
        with open(filepath, 'rb') as fp:
            file = MIMEBase(maintype, subtype)              # Используем общий MIME-тип
            file.set_payload(fp.read())                     # Добавляем содержимое общего типа (полезную нагрузку)
            fp.close()
            encoders.encode_base64(file)                    # Содержимое должно кодироваться как Base64
    file.add_header('Content-Disposition', 'attachment', filename=filename) # Добавляем заголовки
    msg.attach(file)                                        # Присоединяем файл к сообщению

def process_attachement(msg, files):                        # Функция по обработке списка, добавляемых к сообщению файлов
    for f in files:
        if os.path.isfile(f):                               # Если файл существует
            attach_file(msg,f)                              # Добавляем файл к сообщению
        elif os.path.exists(f):                             # Если путь не файл и существует, значит - папка
            dir = os.listdir(f)                             # Получаем список файлов в папке
            for file in dir:                                # Перебираем все файлы и...
                attach_file(msg,f+"/"+file)                 # ...добавляем каждый файл к сообщению

def send_mail(title, text, image):
    text = ''.join([str(item) for item in text]) # соединяем все <p>
    addr_from, password = my_keys.mailru()
    addr_to = "rolliethelynx@gmail.com"
    

    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = addr_to
    msg['Subject'] = f'Избранная статья Википедии – {title}' # Тема сообщения

    # msg.attach(MIMEText(body, 'plain'))                    # Добавляем в сообщение текст

    html = f"""\
    <html>
    <head></head>
    <body>
        <h1>
            {title}
        </h1>
        <br>
            <img src='https:{image}'>
            {text}
    </body>
    </html>
    """
    msg.attach(MIMEText(html, 'html', 'utf-8'))         # Добавляем в сообщение HTML-фрагмент

    files = ['F:\\lulz\\Cats\\1239yTt3bmA.jpg']         # Список файлов, если вложений нет, то files=[]
    process_attachement(msg, files)    

    server = smtplib.SMTP('smtp.mail.ru', 25)           # Создаем объект SMTP
    # server.set_debuglevel(True)                       # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
    server.starttls()                                   # Начинаем шифрованный обмен по TLS
    server.login(addr_from, password)                   # Получаем доступ
    server.send_message(msg)                            # Отправляем сообщение
    server.quit()                                       # Выходим
    print('Email sent!')


def main():
    title, text, image = get_wiki()
    send_mail(title, text, image)


if __name__ == "__main__":
    main()
