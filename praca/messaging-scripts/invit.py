#!python3

import sys, pyperclip

if len(sys.argv)<5:
    print('użycie: python invit.py - wykreowanie zaproszenia na rozmowę')
    sys.exit()

gender = sys.argv[1]
name = sys.argv[2]
date = sys.argv[3]
hour = sys.argv[4]


if gender == "K":
        title = "Pani"
        title_1 = title
        title_2 = title
else:
    title = "Panie"
    title_1 = "Pańskiego"
    title_2 = "Pański"


output = 'Dzień dobry %s %s, \n\
\nDziękuję za zainteresowanie i przesłanie CV. Kolejny krok to dłuższa rozmowa telefoniczna (około 30 min.), \
skoncentrowana na przedstawieniu firmy oraz stanowiska, a także poznaniu %s doświadczenia. \n\
\nJako termin rozmowy proponuję %s, godzina %s - jak ten termin wpisuje się w %s kalendarz?  \n\
\nPozdrawiam serdecznie, \nBartosz Hojnacki'  % (title, name, title_1, date, hour, title_2)

pyperclip.copy(output)    





    
