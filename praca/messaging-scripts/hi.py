#!python3

##contact invitation with link to specific job offer

## dict of job offers - key in dict is also
## keyword while using script from windows cmd
## value need to be replaced with actual job offer link

joboffers = {'c++' : 'https://
             'react' : 'https,      
             'angular' : 'https://bit.ly/2lRGMRY',  
             }
import sys, pyperclip

if len(sys.argv) < 5:
    print('uzycie: python hi.py')
    sys.exit()


gender = sys.argv[1]
role = sys.argv[2]
city = sys.argv[3]
link = sys.argv[4]


if gender == "K":
    title = "Pani"
    title_1 = "Panią"
else:
    title = "Panie"
    title_1 = "Pana"




output = "Dzień dobry %s \
\n\nZapraszam do sieci kontaktów oraz przy okazji przedstawiam projekt rekrutacyjny, który może %s zainteresować. \
\nStanowisko to %s, a lokalizacja %s - więcej informacji znaduje się tutaj %s.\
\nPozdrawiam \nBartosz Hojnacki" % (title, title_1, role, city, joboffers[link])

pyperclip.copy(output)


