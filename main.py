'''
<prog>          -> start> <verif> <stop
<verif>         -> <varia> | <varia> print <verif> | <varia> input <verif> & <varia> ; <verif>
<varia>         -> <exprou> | <exprou> i <varia> | <exprou> s <varia> | <exprou> b <varia>
<exprou>        -> <expret> | <expret> | <exprou>
<expret>        -> <exprpm> | <exprpm> & <expret>
<exprpm>        -> <exprpm> | <exprpm> + <exprfd> | <exprpm> - <exprfd>
<exprfd>        -> <moinsnot> | <exprfd> * <moinsnot> | <exprfd> / <moinsnot> | <exprfd> % <moinsnot>
<moinsnot>      -> <facteur> ~ <moinsnot> | <facteur> - <moinsnot>
<facteur>       -> ( <exprpm> ) | <nombre>
<variable>      -> <nombre> | <nombre> i <variable> | <nombre> s <variable> | <nombre> b <variable>
<nombre>        -> <chiffre> | <nombre> <chiffre> | <nombre> <binaire> | <nombre> <hexa>
<lettre>        -> a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
<hexa>          -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | a | b | c | d | e | f
<binaire>       -> 0 | 1
<chiffre>       -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
'''
listeVarDeclarer = []
preCodeCible = []
debutCodeCible = []
endCodeCible = []

def Prog():
    f=0
    SymboleSuivant(0)
    if SymboleCourant(6) == "start>":
        SymboleSuivant(6)
        codeCible.append("void main()")
        codeCible.append("{")
        codeCible.append("\t_asm")
        codeCible.append("\t{")
        f=verif()
        if SymboleCourant(5) == "<stop":
            SymboleSuivant(5)
            if f==1:
                endCodeCible.append("\t\tpop eax")
            endCodeCible.append("\t}")
            endCodeCible.append("}")
            return True
        else:
            return False
    else:
        return False

def verif():
    t = 0
    x = 0
    y = 0
    z = 0
    if SymboleCourant(5) == "print":
        while SymboleCourant(5) == "print":
            SymboleSuivant(5)
            Lettre()
            if x != 1:
                x = 1
                debutCodeCible.append("#include <stdio.h>")
            if y != 1:
                y = 1
                debutCodeCible.append("const char msgAffichage[] = \"Valeur = %d\\n\"; ")
            codeCible.append("\t\tpush offset msgAffichage")
            codeCible.append("\t\tcall dword ptr printf")
            codeCible.append("\t\tadd esp, 8")
            t=2

    if SymboleCourant(5) == "input":
        while SymboleCourant(5) == "input":
            SymboleSuivant(5)
            if x != 1:
                x = 1
                debutCodeCible.append("#include <stdio.h>")
            if z != 1:
                z = 1
                debutCodeCible.append("const char msgSaisie[] = \"%d\"; ")
                debutCodeCible.append("const char msgEntrez[] = \"Entrez une valeur : \"; ")
                debutCodeCible.append("push offset varSaisie;")
            codeCible.append("\t\tpush offset msgEntrez")
            codeCible.append("\t\tcall dword ptr printf")
            codeCible.append("\t\tadd esp, 4")
            codeCible.append("\t\tpush offset varSaisie")
            codeCible.append("\t\tpush offset msgSaisie")
            codeCible.append("\t\tcall dword ptr scanf")
            codeCible.append("\t\tadd esp, 8")
            codeCible.append("\t\tpush varSaisie")
            codeCible.append("\t\tpop eax")
            if SymboleCourant(1) == "i":
                nomVaria = Lettre()
                codeCible.append("\t\tpop " + nomVaria)
            elif SymboleCourant(1) == "b":
                nomVaria = Lettre()
                codeCible.append("\t\tmov " + nomVaria + ", al")
            elif SymboleCourant(1) == "s":
                nomVaria = Lettre()
                codeCible.append("\t\tmov " + nomVaria + ", ax")
    
    
    if SymboleCourant(4) == "zero":
        SymboleSuivant(4)
        zero()
        t=2

    t = Varia()

    while SymboleCourant(1) == ";":
        SymboleSuivant(1)
        if SymboleCourant(5) == "print":
            while SymboleCourant(5) == "print":
                SymboleSuivant(5)
                Variable()
                Lettre()
                Varia()
                if x!=1:
                    x=1
                    debutCodeCible.append("#include <stdio.h>")
                if y!=1:
                    y=1
                    debutCodeCible.append("const char msgAffichage[] = \"Valeur = %d\\n\"; ")
                codeCible.append("\t\tpush offset msgAffichage")
                codeCible.append("\t\tcall dword ptr printf")
                codeCible.append("\t\tadd esp, 8")
                t=2

        if SymboleCourant(5) == "input":
            while SymboleCourant(5) == "input":
                SymboleSuivant(5)
                if x != 1:
                    x = 1
                    debutCodeCible.append("#include <stdio.h>")
                if z != 1:
                    z = 1
                    debutCodeCible.append("const char msgSaisie[] = \"%d\"; ")
                    debutCodeCible.append("const char msgEntrez[] = \"Entrez une valeur : \"; ")
                    debutCodeCible.append("push offset varSaisie;")
                codeCible.append("\t\tpush offset msgEntrez")
                codeCible.append("\t\tcall dword ptr printf")
                codeCible.append("\t\tadd esp, 4")
                codeCible.append("\t\tpush offset varSaisie")
                codeCible.append("\t\tpush offset msgSaisie")
                codeCible.append("\t\tcall dword ptr scanf")
                codeCible.append("\t\tadd esp, 8")
                codeCible.append("\t\tpush varSaisie")
                codeCible.append("\t\tpop eax")
                if SymboleCourant(1) == "i":
                    nomVaria = Lettre()
                    codeCible.append("\t\tpop " + nomVaria)
                elif SymboleCourant(1) == "b":
                    nomVaria = Lettre()
                    codeCible.append("\t\tmov " + nomVaria + ", al")
                elif SymboleCourant(1) == "s":
                    nomVaria = Lettre()
                    codeCible.append("\t\tmov " + nomVaria + ", ax")
                    
        if SymboleCourant(4) == "zero":
            SymboleSuivant(4)
            zero()
            t=2
                
        Varia()
        f=t
    return f
    
def zero():
    if SymboleCourant(1) in "isb":
        while SymboleCourant(1) in "isb":
            if SymboleCourant(1) == "b":
                nomVaria = Lettre()
                if (nomVaria not in listeVarDeclarer):
                    preCodeCible.append("char " + nomVaria + ";")
                    codeCible.append("\t\tmov " + nomVaria + ", 0")
                    listeVarDeclarer.append(nomVaria)
            elif SymboleCourant(1) == "i":
                nomVaria = Lettre()
                if (nomVaria not in listeVarDeclarer):
                    preCodeCible.append("int " + nomVaria + ";")
                    codeCible.append("\t\tmov " + nomVaria + ", 0")
                    listeVarDeclarer.append(nomVaria)

    
def Varia():
    if SymboleCourant(1) in "isb":
        while SymboleCourant(1) in "isb":
            if SymboleCourant(1) == "i":
                nomVaria = Lettre()
                if SymboleCourant(1) != "=":
                    return False
                SymboleSuivant(1)
                if (nomVaria not in listeVarDeclarer):
                    preCodeCible.append("int " + nomVaria + ";")
                    listeVarDeclarer.append(nomVaria)
                ExprOU()
                codeCible.append("\t\tpop " + nomVaria)
            elif SymboleCourant(1) == "b":
                nomVaria = Lettre()
                if SymboleCourant(1) != "=":
                    return False
                SymboleSuivant(1)
                if (nomVaria not in listeVarDeclarer):
                    preCodeCible.append("char " + nomVaria + ";")
                    listeVarDeclarer.append(nomVaria)
                ExprOU()
                codeCible.append("\t\tpop eax")
                codeCible.append("\t\tmov " + nomVaria + ", al")
            elif SymboleCourant(1) == "s":
                nomVaria = Lettre()
                if SymboleCourant(1) != "=":
                    return False
                SymboleSuivant(1)
                if (nomVaria not in listeVarDeclarer):
                    preCodeCible.append("short " + nomVaria + ";")
                    listeVarDeclarer.append(nomVaria)
                ExprOU()
                codeCible.append("\t\tpop eax")
                codeCible.append("\t\tmov " + nomVaria + ", ax")

    else:
        ExprOU()
        f=1
        return f

def ExprOU():
    ExprET()
    while SymboleCourant(1) in "|":
        SymboleSuivant(1)
        ExprET()
        codeCible.append("\t\tpop ebx")
        codeCible.append("\t\tpop eax")
        codeCible.append("\t\tor eax, ebx")
        codeCible.append("\t\tpush eax")

def ExprET():
    ExprF()
    while SymboleCourant(1) in "&":
        SymboleSuivant(1)
        ExprF()
        codeCible.append("\t\tpop ebx")
        codeCible.append("\t\tpop eax")
        codeCible.append("\t\tand eax, ebx")
        codeCible.append("\t\tpush eax")
        
def ExprF():
    ExprPM()
    while SymboleCourant(1) in "F":
        SymboleSuivant(1)
        ExprPM()
        codeCible.append("\t\tpop ebx")
        codeCible.append("\t\tpop eax")
        codeCible.append("\t\tadd eax, ebx")
        codeCible.append("\t\timul eax, 2")
        codeCible.append("\t\tpush eax")

def ExprPM():
    ExprFD()
    while SymboleCourant(1) in "+-":
        if SymboleCourant(1) == '+':
            SymboleSuivant(1)
            ExprFD()
            codeCible.append("\t\tpop ebx")
            codeCible.append("\t\tpop eax")
            codeCible.append("\t\tadd eax, ebx")
            codeCible.append("\t\tpush eax")
        elif SymboleCourant(1) == '-':
            SymboleSuivant(1)
            ExprFD()
            codeCible.append("\t\tpop ebx")
            codeCible.append("\t\tpop eax")
            codeCible.append("\t\tsub eax, ebx")
            codeCible.append("\t\tpush eax")

def ExprFD():
    ExprMoinsNot()
    while SymboleCourant(1) in "*/%":
        if SymboleCourant(1) == '*':
            SymboleSuivant(1)
            ExprMoinsNot()
            codeCible.append("\t\tpop ebx")
            codeCible.append("\t\tpop eax")
            codeCible.append("\t\timul eax, ebx")
            codeCible.append("\t\tpush eax")
        elif SymboleCourant(1) == '/':
            SymboleSuivant(1)
            ExprMoinsNot()
            codeCible.append("\t\tpop ebx")
            codeCible.append("\t\tpop eax")
            codeCible.append("\t\tcdq")
            codeCible.append("\t\tidiv ebx")
            codeCible.append("\t\tpush eax")
        elif SymboleCourant(1) == '%':
            SymboleSuivant(1)
            ExprMoinsNot()
            codeCible.append("\t\tpop ebx")
            codeCible.append("\t\tpop eax")
            codeCible.append("\t\tcdq")
            codeCible.append("\t\tidiv ebx")
            codeCible.append("\t\tpush edx")

def ExprMoinsNot():
    Facteur()
    if SymboleCourant(1) == '-':
        SymboleSuivant(1)
        Facteur()
        codeCible.append("\t\tpop eax")
        codeCible.append("\t\tneg eax")
        codeCible.append("\t\tpush eax")
    elif SymboleCourant(1) == '~':
        SymboleSuivant(1)
        Facteur()
        codeCible.append("\t\tpop eax")
        codeCible.append("\t\tnot eax")
        codeCible.append("\t\tpush eax")
    elif SymboleCourant(1) == 'f':
        SymboleSuivant(1)
        Facteur()
        codeCible.append("\t\tpop eax")
        codeCible.append("\t\timul eax, 2")
        codeCible.append("\t\tpush eax")

def Facteur():
    if SymboleCourant(1) == '(':
        SymboleSuivant(1)
        ExprOU()
        if SymboleCourant(1) == ')':
            SymboleSuivant(1)
    else:
        Variable()

def Variable():
    if SymboleCourant(1) in "isb":
        while SymboleCourant(1) in "isb":
            if SymboleCourant(1) == "i":
                nomVaria = Lettre()
                if SymboleCourant(1) != "=":
                    codeCible.append("\t\tpush " + nomVaria)
                    return False
                SymboleSuivant(1)
                Nombre()
            elif SymboleCourant(1) == "b":
                nomVaria = Lettre()
                if SymboleCourant(1) != "=":
                    codeCible.append("\t\tmovsx eax, " + nomVaria )
                    codeCible.append("\t\tpush eax")
                    return  False
                SymboleSuivant(1)
                Nombre()
            elif SymboleCourant(1) == "s":
                nomVaria = Lettre()
                if SymboleCourant(1) != "=":
                    codeCible.append("\t\tmovsx eax, " + nomVaria)
                    codeCible.append("\t\tpush eax")
                    return False
                SymboleSuivant(1)
                Nombre()
    else:
        Nombre()


def Nombre():
    if SymboleCourant(2) == "0b":
        SymboleSuivant(2)
        if Binaire() == True:
            nb = ord(SymboleCourant(1)) - 0x30
            SymboleSuivant(1)
            while Chiffre() == True:
                nb = nb * 2 + ord(SymboleCourant(1)) - 0x30
                SymboleSuivant(1)
            codeCible.append("\t\tpush dword ptr " + str(nb))

    elif SymboleCourant(2) == "0x":
        SymboleSuivant(2)
        nb=0
        if Hexa() == True:
            while Hexa() == True:
                if SymboleCourant(1) in "abcdef":
                    nb = nb * 16 + ord(SymboleCourant(1)) - 0x57
                    SymboleSuivant(1)

                elif SymboleCourant(1) in "0123456789":
                    nb = nb * 16 + ord(SymboleCourant(1)) - 0x30
                    SymboleSuivant(1)
            codeCible.append("\t\tpush dword ptr " + str(nb))


    elif Chiffre() == True:
        nb = ord(SymboleCourant(1)) - 0x30
        SymboleSuivant(1)
        while Chiffre() == True:
            nb = nb * 10 + ord(SymboleCourant(1)) - 0x30
            SymboleSuivant(1)
        codeCible.append("\t\tpush dword ptr " + str(nb))


def Hexa():
    if SymboleCourant(1) in "0123456789abcdef":
        return True
    else:
        return False


def Binaire():
    if SymboleCourant(1) in "01":
        return True
    else:
        return False


def Chiffre():
    if SymboleCourant(1) in "0123456789":
        return True
    else:
        return False

def Lettre():
    listeElement=""
    while Caractere()==True:
        listeElement = listeElement + SymboleCourant(1)
        SymboleSuivant(1)
    return listeElement

def Caractere():
    if SymboleCourant(1) in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return True
    else:
        return False

def SymboleCourant(n):
    return programme[posCourante:posCourante + n]

def SymboleSuivant(n):
    global posCourante
    posCourante = posCourante + n
    while posCourante < len(programme) and programme[posCourante] == ' ':
        posCourante = posCourante + 1

programme = ("start>"
                "print 3;" 
                "zero bVar;" 
                "zero iVar;"
                "iVar = 32 * f78 - 45 F 100"
                "<stop")
codeCible = []
posCourante = 0


if Prog() == True:
    for debut in debutCodeCible:
        print(debut)
    for pre in preCodeCible:
        print(pre)
    print("")
    for c in codeCible:
        print(c)
    for end in endCodeCible:
        print(end)
    print("\nCompilation terminée avec succès!")
else:
    print("Erreur de compilation : le caractere", SymboleCourant(1),
          "à la " + str(posCourante + 1) + "e position est invalide!")

