#!python3

##Zaproszenie do kontaktów

## lista ofert pracy wraz ze skróconymi linkami
JOBOFFERS = {

    "Embedded": "https://nordhr.pl/offer/sees-switz/",
    "Reqs" : "https://bit.ly/2NX6cZr",                            #https://nordhr.pl/offer/requirements-engineer-business-analyst-switzerland/,
    "Dynamics" : "https://nordhr.pl/offer/msdcrm-switz/",
    "Qt" : "https://bit.ly/2t2KXhw",
    "dutch": "https://bit.ly/33tnrIg"
    
            }              


import sys, pyperclip

if len(sys.argv) < 4:
    print('uzycie: python pw.py - skopiowanie hasla wskazanego konta')
    sys.exit()


role = sys.argv[1]
city = sys.argv[2]
link = sys.argv[3]






output = "Dear \
\n\nI would like to add you to my professional network as well as ignite your interest in our latest offer. \
\nThe position is %s in %s - you can find more details here: %s.\
\nBest regards, \nBartosz Hojnacki" % (role, city, JOBOFFERS[link])
pyperclip.copy(output)
