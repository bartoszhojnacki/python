#!python3

##ask to remain in touch with candidate after declining presented job offer

import sys, pyperclip

if len(sys.argv) < 3:
    print('uzycie: python contact.py')
    sys.exit()


gender = sys.argv[1]
name = sys.argv[2]

if gender == "K":
    title = "Pani"
    title_1 = title
else:
    title = "Panie"
    title_1 = "Pańska"


output = "Dzień dobry %s %s,\
\n\nDziękuję za informację zwrotną. Proponuję, abyśmy pozostali w kontakcie na wypadek kolejnych projektów \
z mojej strony lub gdyby %s sytuacja uległa zmianie. \n\nPozdrawiam serdecznie, \nBartosz Hojnacki"  % (title, name, title_1)
pyperclip.copy(output)
