class Tronco:#se define esta clase para tener interaccion con los sprites y con los objetos del juego
    import pygame
    #metodo constructor para dar a conocer el color de los troncos, sus coordenadas, sus dimensiones
    #ademas de conocer si está ubicado de manera horizontal o vertical y su posicion (vertical u horizontal)
    def __init__ (self, color, cor_x, cor_y, ancho, alto, mediano_o_grande, horizontal_o_vertical):
        self.color = color
        self.x = cor_x
        self.y = cor_y
        self.ancho = ancho
        self.alto = alto
        self.mog = mediano_o_grande
        self.hov = horizontal_o_vertical
    
    #metodo que sobrecarga el tronco
    def __str__ (self):
        if self.mog == True:
            msn = "color:{0}\ncoordenadas:({1},{2})\nAncho: {3} y Alto: {4}\nEs grande {5}".format (self.color, self.x, self.y, self.ancho, self.alto, self.hov)
            return msn
        else:
            msn = "color:{0}\ncoordenadas:({1},{2})\nAncho: {3} y Alto: {4}\nEs mediano {5}".format (self.color, self.x, self.y, self.ancho, self.alto, self.hov)
            return msn