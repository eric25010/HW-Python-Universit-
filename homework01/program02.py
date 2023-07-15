'''
Abbiamo n pulsanti numerati da 1 a N ed N lampadine anch'esse numerate da 1 a N.
Il generico pulsante x cambia lo stato (da accesa a spenta o viceversa) della lampadina x 
e di tutte le lampadine il cui numero identificativo e' un divisore di x.
Ad esempio il pulsante 18 cambia lo stato delle lampadine 1,2,3,6,9,18.
Ogni pulsante puo' essere premuto al massimo una volta e i pulsanti vanno premuti 
in ordine crescente (una volta premuto il pulsante x  non e' piu' possibile premere 
i pulsanti da 1 a x-1).
Sapendo N e l'insieme 'accese' delle lampadine al momento accese
bisogna individuare la sequenza crescente di bottoni da premere perche'
tutte le lampadine risultino accese.
Definire una funzione es2(N, accese) che dati:
- il numero N di lampadine
- l'insieme 'accese' contenente gli identificativi delle lampadine al momento accese
determina e restituisce la lista contenente nell'ordine i pulsanti da premere perche' 
le N lampadine risultino tutte accese.
Ad esempio per N=6 e accese={2,4} es2(N, accese) restituisce la lista [2,5,6] infatti:
-all'inizio sono accese le lampadine {2,4}
-dopo aver premuto il pulsante 2 saranno accese le lampadine {1,4}
-dopo aver premuto il pulsante 5 saranno accese le lampadine {4,5}
-dopo aver premuto il pulsante 6 saranno accese le lampadine {1,2,3,4,5,6}

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 (ad esempio editatelo dentro Spyder)
'''
import math

def es2(N, ins):
    # inserite qui il vostro codice
    ins2 = ins.copy()
    lista_premuti = []
    while N > 0:
       if N not in ins2:
           lista_premuti.append(N)
           accensioneOSpegnimento(listaDivisori(N), ins2)
       N-=1
    return sorted(lista_premuti)


def listaDivisori(N):
    l=[n for n in range(1, int(math.sqrt(N)) + 1) if N % n == 0]
    return aggiuntaLista(N,l)


def aggiuntaLista(N,l):
    l2 = l.copy()
    l2.reverse()
    lunghezza = len(l)-1
    while lunghezza >= 0:
        if not int(N/l2[lunghezza]) in l:
            l.append(int(N/l2[lunghezza]))
        lunghezza-=1
    return sorted(l)
    
def accensioneOSpegnimento(l,ins):
     for interruttore in l:
         if interruttore in ins:
            ins.remove(interruttore)
         else:
            ins.add(interruttore)
     return ins
    
