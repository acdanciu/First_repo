
# if
piesa_faina=False
print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

# if else
# daca nr este par primtam acest lucru
# altfel printam impar
nr = 4
# par se imparte exact la 2
# daca se imparte la 2 restul e 0
if nr % 2 == 0:
    print('nr par')
else:
    print('impar')

# este un nr pozitiv?
if (nr>0):
    print ('pozitiv')
else:
    print('nr nu este pozitiv')

# if, else if, else
# cum ne saluta robotelul in functie de ora

# luam date de la tastatura
# ne asiguram ca sunt transformate din str in int
# ora = int(input('introdu ora'))
# if ora < 0:
#     print('ora negativa')
# elif ora <= 11:
#     print('Buna dimineata')
# elif ora <= 18:
#     print('Buna ziua')
# elif ora <=21:
#     print('Buna seara')
# elif ora <=24:
#     print('Noapte buna')
# else:
#     print('ora invalida')

# ctrl + /

# robotel telefonic
optiunea = int(input('alege o optiune'))
if optiunea == 0:
    print('meniu anterior')
elif optiunea == 1:
    print('ati ales romana')
elif optiunea == 2:
    print('ati ales engleza')
else:
    print('nu ati ales optiunea, mai incearca')
