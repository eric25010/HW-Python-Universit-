'''
Definire una funzione es3(lista, testo) che prende:
- una lista di parole (nessuna delle quali e' prefisso dell'altra)
- una stringa di testo. Il testo e' stato ottenuto concatenando alcune delle parole presenti nella lista 'lista'
  (una stessa parola puo' comparire piu' volte nella stringa di testo).
- restituisce una coppia (tupla) formata da:
        - la lista delle parole che, concatenate producono il testo
        - la parola che vi occorre piu' spesso
  (se questa parola non e' unica allora viene restituita quella che precede le altre lessicograficamente).
  Nella lista di output ogni parola appare una sola volta e le parole
  risultano ordinate in base alla loro prima apparizione nella concatenazione che produce il testo
  (i.e. quella che compare per prima al primo posto ecc.ecc.)
  Infine al termine della funzione la lista 'lista' deve risultare modificata come segue:
  in essa saranno state cancellate tutte le parole utilizzate in testo, e tornate come risultato.
  Ad esempio: se lista=['gatto','cane','topo']
  - con  testo='topogattotopotopogattogatto' la risposta e' la coppia (['topo','gatto'],'gatto')
    e lista diviene ['cane']
  se lista=['ala','cena','elica','nave','luce','lana','vela']
  - con testo='lucenavelanavelanaveelica' la risposta e' (['luce','nave','lana','vela','elica'],'nave')
  e ls diviene ['ala','cena']

NOTA: il timeout previsto per questo esercizio è di 5 secondi per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 (ad esempio editatelo dentro Spyder)
'''
def es3(lista, testo):
    stringa = ""
    dizionario = {}
    minimo = lunghezza_minima(lista)
    puntatore1 = 0
    puntatore2 = 0
    while puntatore1 < len(testo):
        stringa = testo[puntatore1 : puntatore2]
        if stringa in lista:
            if stringa not in dizionario: 
                dizionario[stringa] = 1
            else:
                dizionario[stringa] += 1
            puntatore1 = puntatore2
            puntatore2 += minimo - 1
        puntatore2 += 1
    lista = rimozioneElementi(listifica(dizionario)[0], lista)
    return (listifica(dizionario)[0], listaDaDizionario(dizionario)[0])
            
def listaDaDizionario(dizionario):
    chiavi, valori = listifica(dizionario)
    return sorted([chiavi[x] for x in range(len(valori)) if valori[x] == max(valori)])        


def rimozioneElementi(lista_dizionario, lista):
    for parola in lista.copy():
        if parola in lista_dizionario:
            lista.remove(parola)
    return lista

def lunghezza_minima(lista):
    return min([len(parola) for parola in lista])

def listifica(dizionario):
    return list(dizionario.keys()), list(dizionario.values())
