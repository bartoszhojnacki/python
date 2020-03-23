#!python3

##request for feedback after accepted invitation
##yet without any response


             
import sys, pyperclip

if len(sys.argv) < 2:
    print('uzycie: python pw.py - skopiowanie hasla wskazanego konta')
    sys.exit()


gender = sys.argv[1]




if gender == "K":
    title = "Pani"
    osoba = "miała"
else:
    title = "Pan"
    osoba = "miał"




output = "Dzień dobry,\
\n czy %s %s już okazję zapoznać się z ofertą, którą przesłałem w zaproszeniu?\
\n Będę bardzo wdzięczny za informację zwrotną.\
\nPozdrawiam serdecznie, \nBartosz Hojnacki" % (osoba, title)

pyperclip.copy(output)


