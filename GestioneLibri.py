Catalogo = ["Cappuccetto rosso", "Biancaneve", "Il piccolo principe", "Harry Potter", "Il signore degli anelli", "L'alchimista"]
Prestito = []


def AggiuntaLibro() :
    AggiuntaLibro = input()
    AggiuntaLibro.append(Catalogo)
    print(AggiuntaLibro)

def PrestitoLibro() :
    ricerca = input("Che libro vuoi prendere in prestito\n")
    if ricerca in Catalogo:
        Catalogo.remove(ricerca)
        Prestito.append(ricerca)
    else:
        print("Libro non disponibile")
    print(PrestitoLibro)


def RiportaLibro() :
    ricerca = input("Che libro vuoi restituire\n")
    if ricerca in Prestito:
        Prestito.remove(ricerca)
        Catalogo.append(ricerca)
        print("Libro restituito")
    else:
        print("Libro non disponibile")


def DisponibilitàLibro():
    DisponibilitàLibro = input()
    if DisponibilitàLibro in Catalogo:
        print("Libro diponibile.")
    else:
        print("Libro non diponibile.")



def LibriDisponibili():

    for i in Catalogo:
     print(f"{i}")
    

    
def LibriPrestito() :
    ricerca = input("Che libro cerchi?\n")
    LibriPrestito = input()
    if LibriPrestito in Prestito:
        print("Libro in prestito.")
    else:
        print("Libro non in prestito")