def printGreeting():
    print("Buna ziua! Bine ati venit!")

def printGreetingByName(nume, prenume):
    print(f'Buna Ziua {nume}  {prenume}')

def mediaNr(a,b,c):
    return (a+b+c)/3

def piValue():
    return 3.14

# exercitiu
# daca persoana e majora, altfel false
def verificareMajor(varsta):
    if varsta >=18:
        return True
    else:
        return False

# zona de apelare (desktop)
printGreeting()
printGreeting()
printGreetingByName('Sanpetrean', 'Andy')
print(mediaNr(3,4,3))
print (piValue())
#se ia varsta utilizatorului
# print(verificareMajor(18))

age = int(input('introduceti varsta dvs'))
if verificareMajor(age):
    print('Cont creat. Bine ai venit in aplicatie')
else:
    print('Nu ai varsta necesara (18) pt a paria')