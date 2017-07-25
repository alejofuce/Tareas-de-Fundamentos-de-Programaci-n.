import pilasengine
pilas = pilasengine.iniciar(500,400)

def entrada():
	pilas.escenas.Normal()
	pilas.actores.Menu( [ ( " Iniciar Juego" , iniciar_juego ) , ( " Instrucciones " , instrucciones_juego ) , ( " Salir " , salida ) , ] )
	
	mi_fondo = pilas.fondos.Fondo("data/fondo.png.")
	cartel= pilas.actores.Banana()
	cartel.imagen = "data/cartel.png."
	cartel.escala = 0.3
	cartel.x = -2
	cartel.y = -35

def iniciar_juego():
    
    pilas.escenas.Normal()
    pilas.fondos.Fondo("data/fondo.png.")
    puntaje = pilas.actores.Puntaje(color = pilas.colores.rojo)
    puntaje.x = -200
    puntaje.y = 180
    
    def crear_miactor():                   
        esponja=pilas.actores.Mono()
        esponja.escala = 0.5
        esponja.y = -144
        esponja.aprender('MoverseConElTeclado')
        esponja.aprender('LimitadoABordesDePantalla')
        esponja.radio_de_colision= 25
        esponja.aprender('puedeexplotar')
    
    def crear_hamburguesa():
                
        hamburguesa = pilas.actores.Pelota(x = pilas.azar(-250,250), y = 180)
        hamburguesa.imagen = ("data/hambu2.png")
        hamburguesa.escala = 0.025
        hamburguesa.aprender('eliminarsesisaledepantalla')

        def eliminar_hamburguesa():
			hamburguesa.eliminar()
        
        pilas.tareas.agregar(2.5,eliminar_hamburguesa)       

    def crear_medusas():
        medusa = pilas.actores.Aceituna(x = pilas.azar(-250,250), y = 200)
        medusa.y = [200,-220],3
        medusa.imagen = ("data/helado.png")
        medusa.escala = 0.09
        medusa.aprender('eliminarsesisaledepantalla')

    def comer_rico(crear_miactor , crear_hamburguesa,):
      
        crear_hamburguesa.eliminar()
        puntaje.aumentar(10)
    
    def comer_feo(crear_miactor , crear_medusas) :
        crear_miactor.eliminar()
        texto = pilas.actores.Texto("Cuidado con lo que comes")
        texto.color = pilas.colores.Color(0, 0, 0)
        TSK.terminar()
        TSL.terminar()
        pilas.tareas.agregar(5, entrada)
        
    pilas.colisiones.agregar('mono',  'pelota', comer_rico)
    pilas.colisiones.agregar('mono', 'aceituna', comer_feo)
    
    TSK = pilas.tareas.siempre(5 , crear_hamburguesa)
    TSL = pilas.tareas.siempre(10 , crear_medusas)

    crear_miactor()
 	
                
def instrucciones_juego():
	
    pilas.escenas.Normal()

    texto = pilas.actores.Texto("")
    texto.color = pilas.colores.Color(0, 0, 0)
    texto.y = 150
    texto.x = 0
    
    texto1 = pilas.actores.Texto("Come las bananas")
    texto1.color = pilas.colores.Color(0, 0, 0)
    texto.escala = 0.5
    texto1.escala = 0.5
    texto1.y = 65
    texto1.x = 20

    in1 = pilas.actores.Aceituna()
    in1.imagen = "data/hambu2.png."
    in1.escala = 0.020
    in1.x = -100
    in1.y = 65

    texto2 = pilas.actores.Texto("Evita los helados")
    texto2.color = pilas.colores.Color(0, 0, 0)
    texto2.escala = 0.5 
    texto2.x = 20

    in2 = pilas.actores.Banana()
    in2.imagen = "data/helado.png."
    in2.escala = 0.1
    in2.x = -100
    in2.y = -5
    
    in3 = pilas.actores.Estrella()
    in3.imagen = "data/estrella.png."
    in3.escala = 0.2
    in3.x = 115
    in3.y = -100
    
    ins = pilas.interfaz.Boton("S")
    ins.x = -100
    ins.y = -75

    textoins = pilas.actores.Texto("Salir")
    textoins.color = pilas.colores.Color(0, 0, 0)
    textoins.escala = 0.5
    textoins.x = 20
    textoins.y = -70
    
    ini = pilas.interfaz.Boton("I")
    ini.x = -100
    ini.y = -130

    textoini = pilas.actores.Texto(" Instrucciones ")
    textoini.color = pilas.colores.Color(5, 5, 5)
    textoini.escala = 0.5
    textoini.x = 20
    textoini.y = -130
    
    
    salir1 = pilas.interfaz.Boton("salir")
    salir1.conectar(salir_juego)
    salir1.y = -175
    
    fondo_instruc = pilas.fondos.Fondo("data/inst.png.")
    fondo_instruc.escala = 0.5
    
def salir_juego():
	pilas.escenas.Normal()
	pilas.fondos.Fondo("data/gracias.png.")
	#textofinal = pilas.actores.Texto(" Gracias por jugar conmigo ")
	#textofinal.color = pilas.colores.Color(255, 0, 0, 128)
	#textofinal.x = 80
	#textofinal.y = 100
	salir = pilas.interfaz.Boton("salir")
	salir.conectar(salida)
	salir.y = -150
	salir.x = 200

def salida():
    pilas.terminar()
	

entrada()
                        
pilas.ejecutar()