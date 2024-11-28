from GestioneLibri  import AggiuntaLibro
from GestioneLibri  import PrestitoLibro
from GestioneLibri  import RiportaLibro
from GestioneLibri  import DisponibilitàLibro
from GestioneLibri  import LibriDisponibili
from GestioneLibri  import LibriPrestito
from GestioneLibri  import Catalogo
from GestioneLibri  import Prestito
scelta=-1
 
while(scelta != 7):
    print("1. Aggiungi libro alla libreria: ")
    print("2. Prestito libro: ")
    print("3. Riporta il libro: ")
    print("4. Disponibilità libro: ")
    print("5. Libri diponibili nella libreria: ")
    print("6. Libri dati in prestito: ")
    print("7. Esci")
 
    scelta=int(input("Scegli: "))
    print("-------------")
 
    if(scelta == 1):
        AggiuntaLibro()
        #AggiuntaLibro = input()
        #print("Libro aggiunto correttamente alla libreria.")
    elif(scelta == 2):
        PrestitoLibro()
        #PrestitoLibro = input ()
        #print("Prestito effettuato.")
    elif(scelta == 3):
        RiportaLibro()
        #RiportaLibro = input()
        #print("Libro riportato.")
    elif(scelta == 4):
        DisponibilitàLibro()
        #DisponibilitàLibro = input()
        #print("Libro diponibile.")
    elif(scelta == 5):
        LibriDisponibili()
        #LibriDisponibili = input()
        #print("Libro disponibile nella libreria.")
    elif(scelta == 6):
        LibriPrestito()
        #LibriPrestito = input()
        #print("Libro in prestito.")
    elif(scelta == 7):
        pass
    else:
        print("Non capisco.")

print("Uscito con successo.")