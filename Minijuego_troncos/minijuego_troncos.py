import pygame 

def main (): #el main es donde quiero crear el juego 
    ###crear un fondo de pantalla de un solo color 

    pygame.init () #arrancar pygame, o prepararlo 
    size_up = 720
    superficie = pygame.display.set_mode ((size_up, size_up)) #aca indico cuantos pixeles por cuantos pixeles (500 x 500) 
                                            #lo que reciba debe ser una tupla 
    largo_o = (0, 0, 120, 360)
    largo_p = (600, 120, 120, 360)
    largo_q = (0, 360, 360, 120)
    
    mediano_a = (120, 0, 120, 240)
    mediano_b = (240, 0, 240, 120)
    mediano_c = (480, 0, 120, 240)
    mediano_d = (240, 120, 120, 240)
    mediano_e = (360, 360, 120, 240)
    mediano_f = (240, 480, 120, 240)
    mediano_g = (480, 480, 240, 120)
    mediano_h = (0, 600, 240, 120)
    mediano_i = (360, 600, 240, 120)
    
    mediano_x = (360, 240, 240, 120)
    
    amarillo = (255, 255, 0)
    morado = (97, 50, 107)
    azul_oscuro = (0, 0, 255)
    verde_claro = (152, 251, 152)
    naranja = (255, 165, 0)
    azul_claro = (0, 191, 255)
    rosado = (255, 182, 193)
    morado_oscuro = (75, 0, 130)
    verde_oscuro = (0, 100, 0)
    gris = (192, 192, 192)
    beige = (245, 245, 220)
    amarillo_palido = (255, 255, 102)
    rojo = (255, 69, 0)

    while True: 
        evento = pygame.event.poll() #estar atento a los eventos 
        if evento.type == pygame.QUIT: #boton cerrar 
            break 

        superficie.fill ((0, 0, 0)) 
                        #lo que reciba debe ser una tupla 

        superficie.fill (amarillo, largo_o)
        superficie.fill (morado, largo_p)
        superficie.fill (azul_oscuro, largo_q)
        superficie.fill (verde_claro, mediano_a)
        superficie.fill (naranja, mediano_b)
        superficie.fill (azul_claro, mediano_c)
        superficie.fill (rosado, mediano_d)
        superficie.fill (morado_oscuro, mediano_e)
        superficie.fill (verde_oscuro, mediano_f)
        superficie.fill (gris, mediano_g)
        superficie.fill (beige, mediano_h)
        superficie.fill (amarillo_palido, mediano_i)
        superficie.fill (rojo, mediano_x)
        

        pygame.display.flip () #muestra en pantalla 

    pygame.quit () 

  

main () 
