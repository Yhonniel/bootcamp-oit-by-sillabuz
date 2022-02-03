
# Design Patterned  Builder

#Objetos complejos
# Dividir Trabajo
# Contruir casa

# Cuadra (Juan - Alicia - Fidel - Yefer)
# Juan ( 2 puertas, 4 ventanas, 2 cuatos)
# Alicia ( 2 puertas, 2 ventanas, 1 cochera)
# Fidel (jardin, cochera, ventana)
# Yefer (cuartos, cochera, ventanas)

class Casa:
    puerta = ''
    ventana = ''
    jardin = ''
    cochera = ''
    cuartos = ''

    def __init__(self):
        pass

    def create_puerta(self, puerta):
        self.puerta = puerta

    def create_ventana(self, ventana):
        self.ventana = ventana



    # puerta - ventanas - jardin
    # cochera - cuartos -