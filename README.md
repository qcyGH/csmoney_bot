# .csmoney_bot
Данный телеграм-бот парсит сайт cs.money. Он поможет собрать оружие с определённой категории, при этом фильтрует по скидке (поумолчанию она равняется >= 10), чего нельзя сделать на сайте. Так же, для удобства, при подборе скинов, включены фильтры: "Качество: Прямо с завода", "Скины без блока".
## Бот
Для бота сделано меню и информативные сообщения:
![bot example](/assets/images/bot_example.png)

Пример ошибки, когда не найдо подохдящих предметов:
![error example](/assets/images/error_example.png)
# Установка 
1. Для работы парсера (скрипта на python), нужно использовать **виртуальную среду** (venv):
```
cd csmoney_bot
python -m venv venv_csmoney_bot
source venv_csmoney_bot\\Scripts\\activate
```
- Далее нужно установить пакеты: aiogram, requests, fake-useragent, wheel.
```
pip install aiogram requsts fake-useragent wheel
```
- После чего, нужно прописать команду ``` pip list ``` (она выведет список установленных библиотек), чтобы убедиться, что нужные пакеты установленны в нашу среду. Он должен выглядить вот таким образом: 
![pip list](/assets/images/pip_list.png)   
*Не обращайте внимания что пакетов так много, они нужны для корректной работы тех, которых мы установили* 

2. Теперь можно запускать код. Поумолчанию будут выводиться ножи с ценой от 2000$.
```
python main.py
```
## Настройка бота
1. Для работы нашего бота нам нужен API, для этого заходим в телеграм и находим в поиске бота **@BotFather**, запускаем и создаём нашего бота, после создания мы получим сообщение с **API**:  
![bot api](/assets/images/bot_api.png)  
2. Теперь создадим файл в нашей директории
```
touch bot_token.py
```
Откроем его и добавим **переменную**
```
bot_token = 'your API'
```
*Не забудьте сохранить файл*  

3. Всё готово для работы бота, можем его запускать
```
python csmoney_bot.py
```
- Мы запустили код, если нету никаких ошибок, то переходи в телеграм, в поиске находим бота и пробуем функционал. Для старта напишите ```/start```


P.s  
- Папку **assets** можете удалить, она нужна только для картинок на странице проекта в github.  
  
- Чтобы закрыть бота, нужно в консоли, в которой запускался код, нажать ```Ctrl + C```
