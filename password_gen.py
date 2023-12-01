import random
from random import randint
import tkinter as tk
import customtkinter as ctk
import gettext
import locale
from pathlib import Path
import os


_domain = 'messages'

gettext.bindtextdomain(_domain, 'locale')
gettext.textdomain(_domain)

lang = locale.getdefaultlocale()[0] + '.' + locale.getdefaultlocale()[1] if locale.getdefaultlocale() else 'en_US.utf-8'
# If you need to test another language, or if the app is not using your language
#        comment the line above and uncomment the line below.
#lang = 'en_US.utf-8'

localedir = Path(__file__).parent / 'locale'
os.environ['LANG'] = lang
locale.setlocale(locale.LC_ALL, lang)

gettext.bindtextdomain(_domain, localedir)
gettext.textdomain(_domain)
gettext.install(_domain, localedir=localedir, names=('ngettext',))
gettext.translation(_domain, localedir=localedir, languages=[lang], fallback=True)

_ = gettext.gettext


def random_password(passw, ran):
    CHAR_MAX = 48
    
    try:
        letry.configure(text_color='black')
        if int(ran) > CHAR_MAX:
            1 + 'a'
        n = 0
        passw = list(passw)
        for i in range(int(ran)):
            n += 1
            choice = randint(1, 4)
            if choice == 1:
                ranc = random.sample('abcdefghijklmnopqrstuvwxyz', 1)[0]
            elif choice == 2:
                ranc = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)[0]
            elif choice == 3:
                ranc = random.sample('0123456789', 1)[0]
            elif choice == 4:
                ranc = random.sample('!@#$&', 1)[0]
            while ranc in passw:
                choice = randint(1, 4)
                if choice == 1:
                    ranc = random.sample('abcdefghijklmnopqrstuvwxyz', 1)[0]
                elif choice == 2:
                    ranc = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)[0]
                elif choice == 3:
                    ranc = random.sample('0123456789', 1)[0]
                elif choice == 4:
                    ranc = random.sample('!@#$&', 1)[0]
            passw.insert(i+n, ranc)
        if not any(char in passw for char in ['!', '@', '#']):
            passw[-2] = random.sample('!@#', 1)[0]
        result.set(''.join(passw))
        return ''.join(passw)
    
    except (ValueError, TypeError, IndexError) as e:
        letry.configure(text_color='#c93416')
        
        if isinstance(e, ValueError):
            result.set(_('Apenas números'))
        elif isinstance(e, TypeError):
            result.set(_('Caractéres máx: ')+ f'{CHAR_MAX}')
        elif isinstance(e, IndexError):
            result.set(_('Caractéres insuficientes'))

    except Exception as e:
        letry.configure(text_color='#c93416')
        result.set(f'Error {e}')


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title(_('Gerador de Senhas'))
app.geometry('500x230')

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()


label1 = ctk.CTkLabel(app, text=_('Digite uma palavra desejada (opcional)'))
label1.place(relx=0.3, rely=0.2, anchor=tk.CENTER)

entry1 = ctk.CTkEntry(app)
entry1.place(relx=0.3, rely=0.3, anchor=tk.CENTER)

label2 = ctk.CTkLabel(app, text=_('Digite o número de caracteres'))
label2.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

entry2 = ctk.CTkEntry(app)
entry2.place(relx=0.3, rely=0.6, anchor=tk.CENTER)

botao = ctk.CTkButton(app, text=f"{_('Gerar Senha')}", command=lambda: random_password(entry1.get(), entry2.get()))
botao.place(relx=0.7, rely=0.6, anchor=tk.CENTER)

result = tk.StringVar()
result.set('')
letry = ctk.CTkEntry(app, textvariable=result, state='readonly')
letry.place(relx=0.7, rely=0.3, anchor=tk.CENTER)

app.mainloop()