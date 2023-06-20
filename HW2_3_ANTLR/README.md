# Запуск

[Инструкция](https://evogeek.ru/articles/27474/) для установки и сборки проекта. 

1.Установка ANTLR:
> ```bash
>$ cd /usr/local/lib
>$ sudo curl -O https://www.antlr.org/download/antlr-4.9.2-complete.jar
>$ export CLASSPATH=".:/usr/local/lib/antlr-4.9.2-complete.jar:$CLASSPATH"
>$ alias antlr4='java -jar /usr/local/lib/antlr-4.9.2-complete.jar'
>$ alias grun='java org.antlr.v4.gui.TestRig'
> ```


2. Настройка окружения
```bash
>$ virtualenv venv
>$ source venv/bin/activate
>$ pip install antlr4-python3-runtime
```

3. Генерация файлов (уже есть в папке gen)
```bash
>$ antlr4 -Dlanguage=Python3 grammatica.g4 -visitor -o gen
```

4. Запуск
```bash
>$ python main.py 
```

Пример команд для работы:
```bash
>$ CREATE "biblio"("author":"Olga")   #создание бд
>$ TRUNCATE "biblio"                  #очистка бд
>$ ALTER "biblio" ADD("title":"1986")  #добавление нового элемента
>$ ALTER "biblio" ADD("title":"The Fault in Our Stars")  #добавление нового элемента

>$ RENAME "biblio" TO "library"    #смена имени бд
>$ DELETE FROM "library" WHERE "title" = "1986" #удаление одной записи из бд
>$ DROP "library" #удаление бд
```

## Доступные методы:
1.	CREATE:
   Для создания новой базы данных.
2.	DROP:
   Для удаления базы данных.
3.	ALTER:
   Для добавления нового элемента в базе данных.
4.	TRUNCATE:
   Для удаления всех записей из базы данных.
5.	RENAME:
   Для переименования базы данных.
6.	SELECT:
   Для выборки данных из базы данных.
7.	INSERT:
   Для вставки новых данных в записи базы данных.
8.	UPDATE:
   Для обновления существующих данных в записи базы данных.
9.	DELETE:
   Для удаления записей из базы данных.


