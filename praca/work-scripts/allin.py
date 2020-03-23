

#one file to rule them all..

### wyświetlić listę funkcji i co robią
print("""wybierz funkcję:
msg() - wiadomość - oferta
reco() - rekomendacja
invit() - zaproszenie na screening
contact() - propozycja pozostania w kontakcie
cta() - call to action
verify() - weryfikacja w bazie
reject() - negatywny feedback""")

import pyperclip

## negatywna informacja zwrotna dla kandydata/tki)
def reject():
    gender = input("podaj płeć - K/M: ")

    name = input("Podaj imię Kandydata w wołaczu: ")

    if gender == "K":
        title = "Pani"
        title_1 = title
        title_2 = title
    else:
        title = "Panie"
        title_1 = "Pana"
        title_2 = "Pański"
    role = input('podaj nazwę stanowiska: ')     ## nazwa stanowiska na które rekomendowany był kandydat
    reason = input('powodem odrzucenia jest: ')

    output = 'Dzień dobry %s %s,\
\n\nKontaktuję się z informacją zwrotną odnośnie rekrutacji na stanowisko %s.\
\nNiestety, nie otrzymaliśmy dla %s zaproszenia do kolejnego etapu. Powodem jest %s.\
\n\nZe swojej strony bardzo dziękuję za zaangażowanie i poświęcony czas. \
Mam nadzieję, że już wkrótce będziemy mogli ponownie współpracować przy kolejnym projekcie.\n\nPozdrawiam serdecznie,\nBartosz Hojnacki' % (title, name, role, title_1, reason)

    pyperclip.copy(output)
    print(output)

## wiadomość oferta dla kandydata/tki
def msg():

    role = input("podaj nazwę stanowiska: ")


    project = input('podaj informacje o projekcie: ') # dodaje informacje dot projektu, czyli o co chodzi w roli

    tasks = []
    task = input(r"wklej zadania: ")
    while task != "":
            tasks.append(task)
            task = input("podaj obowiązki: ")

    skills = []
    skill = input(r"podaj pożądany profil: ")
    while skill != "":
            skills.append(skill)
            skill = input("podaj umiejętność: ")

    client = input('Podaj opis klienta (kogo-czego): ')

    descs = []
        desc = input("Nasz Klient oferuje: ")
    while desc !='':
        descs.append(desc)
        desc = input("Nasz Klient oferuje: ")
    
        

    print("\n\nDzień dobry, \
    \n\nKontaktuję się ponieważ aktualnie poszukuję %s, który dołączy do zespołu mojego Klienta %s " % (role, client))
    print(project)
    print("\nZakres obowiązków obejmuje: ")

    for i in range(len(tasks)-1):
        print("- " + tasks[i] +",")

    print("- " + tasks[-1] + ".")
    print("\nPożądany profil: ")

    for i in range(len(skills)-1):
        print("- " + skills[i] +",")

    print("- " + skills[-1] + ".")

    print('\nKlient oferuje: ')
    for i in range(len(descs)-1):
        print('- ' + descs[i] +',')
        print('- ' + descs[-1] + '.')
        
    print("""
Brzmi sensownie? 

Jeśli tak, to proszę o przesłanie angielskiej wersji CV – to przyspieszy proces rekrutacji, a w razie pytań jestem do dyspozycji.
    """)

## rekomendacja kandydata do klienta
def reco():
    import random

    gender = input('Podaj płeć, jeśli M, zostaw puste: ')
    name = input("Podaj imię kandydata: ")
    surname = input("podaj nazwisko kandydata: ")
    exp = input("podaj lata doświadczenia kandydata: ")

    companies = []
    company = input("podaj firmę,w której pracował kandydat lub wciśnij ENTER: ")

    while company != "":
            companies.append(company)
            company = input("podaj firmę,w której pracował kandydat lub wciśnij ENTER: ")


    roles =[]
    role = input("podaj nazwę stanowiska, na którym pracował kandydat: ")

    while role != "":
        roles.append(role)
        role = input("podaj nazwę stanowiska, na którym pracował kandydat: ")


    tasks_1 = []
    tasks_2 = []
    tasks_3 = []

    tasks = [tasks_1, tasks_2, tasks_3]


    task = input(r"podaj obowiązki na stanowisku 1: ")

    while True:
        
        if task == "":
            break
        else:
            tasks_1.append(task)
            task = input("podaj obowiązki na stanowisku 1: ")        


    task = input(r"podaj obowiązki na stanowisku 2: ")

    while True:
        
        if task == "":
            break
        else:
            tasks_2.append(task)
            task = input("podaj obowiazki na stanowisku 2: ")
            
           

    task = input(r"podaj obowiązki na stanowisku 3: ")

    while True:
        
        if task == "":
            break
        else:
            tasks_3.append(task)
            task = input("podaj obowiazki na stanowisku 3: ")
            

    if gender != 'K':
            titles = ['candidate','mr. ' +str(surname),'applicant']
    else:
            titles = ['candidate','mrs. ' +str(surname),'applicant']



    if gender != 'K':
            pronoun = 'his'
    else:
            pronoun = 'her'

    

    adj = ['was responsible for','was accountable for', str(pronoun) + ' tasks consisted of', str(pronoun) + ' tasks included']

    place = ['While working in', 'While being employed in', 'During employment in', 'In', 'During the work in']

    dodatkowe = input('dodatkowe informacje: ')
    motive = input("Candidate's motivation: ")
    salary = input("Podaj wynagrodzenie brutto kandydata: ")
    notice = input("podaj okres wypowiedzenia kandydata: ")
   


    print('%s %s \n\
    \n\
Candidate with %s years of experience gathered in such companies as:' % (name, surname, exp), end =" ")
    print(*companies, sep = ', ', end =' ')
    print('and positions:', end =" ")
    print(*roles, sep = ', ', end = '.')

    for i in range(len(companies)):
    ##for i in range(3):
    ##        print("\nIn", companies[i], random.choice(titles),"as", roles[i], "was", str(random.choice(adj))+':', tasks[i])
            print(str(random.choice(place)), companies[i], str(random.choice(titles)) + ", as", str(roles[i]) + ", " + str(random.choice(adj)), end =': ')
            print(*tasks[i][0:(len(tasks[i]) - 1)], sep = ', ', end =', ')
            print(''.join(tasks[i][(len(tasks[i])-1)] + '.'))

   

    print('Worth noting fact is that ' + str(dodatkowe))

    print("Candidate's motivation: " + str(motive))
    print('Salary expectations: ' + str(salary) + ' PLN gross')
    print('Notice period: ' + str(notice) + ' month' )


## zaproszenie na rozmowę - screening
def invit():   

    gender = input("podaj płeć - K/M: ")

    name = input("Podaj imię Kandydata w wołaczu: ")

    if gender == "K":
        title = "Pani"
        title_1 = title
        title_2 = title
    else:
        title = "Panie"
        title_1 = "Pańskiego"
        title_2 = "Pański"
    date = input("Data rozmowy: ")

    hour = input("Godzina rozmowy: ")


    output = 'Dzień dobry %s %s, \n\
\nDziękuję za zainteresowanie i przesłanie CV. Kolejny krok to dłuższa rozmowa telefoniczna (około 30 min.), \
skoncentrowana na przedstawieniu firmy oraz stanowiska, a także poznaniu %s doświadczenia. \n\
\nJako termin rozmowy proponuję %s, godzina %s - jak ten termin wpisuje się w %s kalendarz?  \n\
\nPozdrawiam serdecznie, \nBartosz Hojnacki'  % (title, name, title_1, date, hour, title_2)

    pyperclip.copy(output)

    print(output)

    
## propozycja pozostania w kontakcie po odrzuceniu przedstawionej oferty pracy:               
def contact():

    gender = input("podaj płeć - K/M: ")

    name = input("Podaj imię Kandydata w wołaczu: ")

    if gender == "K":
        title = "Pani"
        title_1 = title
    else:
        title = "Panie"
        title_1 = "Pańska"
    
    print("Dzień dobry %s %s," % (title, name))
    print("")
    print("Dziękuję za informację zwrotną. Proponuję, abyśmy pozostali w kontakcie na wypadek kolejnych projektów \
z mojej strony lub gdyby %s sytuacja uległa zmianie." % (title_1))
    print("")
    print("Pozdrawiam serdecznie, \nBartosz Hojnacki")


    output = "\nDzień dobry %s %s,\
\n\nDziękuję za informację zwrotną. Proponuję, abyśmy pozostali w kontakcie na wypadek kolejnych projektów \
z mojej strony lub gdyby %s sytuacja uległa zmianie. \n\nPozdrawiam serdecznie, \nBartosz Hojnacki"  % (title, name, title_1)

    pyperclip.copy(output)

## call to action po zaakceptowaniu inmaila i braku dalszych działań
def cta():

    gender = input("podaj płeć - K/M: ")

    name = input("Podaj imię Kandydata w wołaczu: ")

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
        

    output = "\nDzień dobry %s %s,\n\nwidzę, że %s %s wiadomość, \
ale nie %s informacji zwrotnej. \n\nJakich informacji %s %s ode mnie, \
aby przystąpić do rekrutacji? \n\nPozdrawiam serdecznie, \nBartosz Hojnacki" % (title, name, action, title_1, action_1, action_2, title_1)

    pyperclip.copy(output)

## weryfikacja kandydacie w bazie klienta
def verify():

    candidatesAmount = input("Podaj liczbę kandydatów do zweryfikowania: ")



    if candidatesAmount == "1":

        name = input("Podaj imię kandydata: ")
        surname = input("Podaj nazwisko: ")
        email = input("Podaj login maila: ")+"@"
        number = input("Podaj ostatnie 3 cyfry numeru: ")


        print("""
Dzień dobry,

przesyłam nazwisko do weryfikacji:
%s, %s, %s \n"""  % (name + ' ' + surname, email, "xxx xxx " + number))

        output = 'Dzień dobry, \
\n\nprzesyłam nazwisko do weryfikacji: \n\n\
%s, %s, %s \n' % (name + ' ' + surname, email, "xxx xxx " + number)

        pyperclip.copy(output)

    else:
        i = 0
        while i in range(int(candidatesAmount)):
            name = input("Podaj imię kandydata: ")
            surname = input("Podaj nazwisko: ")
            email = input("Podaj login maila: ")+"@"
            number = input("Podaj ostatnie 3 cyfry numeru: ")

            i+=1
        else:
            print("""
Dzień dobry,

przesyłam nazwiska do weryfikacji:
%s, %s, %s \n""" % (name + ' ' + surname, email, number))
