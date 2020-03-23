#!python3

##Call to action after candidate's acceptance to InMail message,
##yet without any further action

import sys, pyperclip

if len(sys.argv) < 3:
    print('uzycie: prośba o akcję')
    sys.exit()


gender = sys.argv[1]
name = sys.argv[2]

if gender == "K":
    title = "Pani"
    action = "zaakceptowała"
    action_1 = "pozostawiła"
    action_2 = "potrzebowałaby"
    title_1 = title
    title_2 = title
else:
    title = "Panie"
    action = "zaakceptował"
    action_1 = "pozostawił"
    action_2 = "potrzebuje"
    title_1 = "Pan"

output = "Dzień dobry %s %s,\n\nwidzę, że %s %s wiadomość, \
ale nie %s informacji zwrotnej. \n\nJakich informacji %s %s ode mnie, \
aby przystąpić do rekrutacji? \n\nPozdrawiam serdecznie, \nBartosz Hojnacki" % (title, name, action, title_1, action_1, action_2, title_1)

pyperclip.copy(output)
