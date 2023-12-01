
# README CREATION IN PROGRESS (it was dark outside, i left it to do in the next day)

### Create new translation

- instalar o pybabel
```bash
$ sudo apt install python3-babel
```

- configure o "babel.cfg"
(arquivo babel.cfg explicação)

- extrair mensagens do código
```bash
$ pybabel extract -F babel.cfg -o messages.pot .
```

- criar o arquivo .po do idioma desejado
```bash
$ pybabel init -i messages.pot -d locale -l <LANG>
```
> Rename LANG as the language you want to use. Ex.: pt_BR, en_US, jp_JP, es_CO

- editar o arquivo e traduzir as mensagens

`locale/<LANG>/LC_MESSAGES/messages.po`
> You can use the en_US "messages.po" as a base for the translation, instead of the original one, because the program is originally in Portuguese-BR.

- compile para transformar em .mo (binário)
```bash
$ pybabel compile -d locale
```