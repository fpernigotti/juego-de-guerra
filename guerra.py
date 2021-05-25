from random import shuffle

class Carta:
    palos =["Espada","basto","copa","oro"]
    
    valores = [None,None,"2","3","4","5","6","7","8","9","sota","caballo","rey","Ancho"]
    
    def __init__(self, v,p):
        
        self.valor = v
        self.palo = p
    
    def __lt__(self, c2):
        
        if self.valor < c2.valor:
            return True
        if self.valor == c2.valor:
            if self.palo < c2.palo:
                return True
            else: 
                return False
        return False
        
    def __gt__(self, c2):
        if self.valor > c2.valor:
            return True
        if self.valor == c2.valor:
            if self.palo > c2.palo:
                return True
            else: 
                return False
        return False
        
       
    def __repr__(self):
        v = self.valores[self.valor]+ " de "+self.palos[self.palo]
        return v
##Prueba de cartas##       
#carta1 = Carta(10, 2)
#carta2 = Carta(11, 3)

#print(carta1)
#print(carta2)
#print(carta1 < carta2)

class Mazo:
    def __init__(self):
        self.cartas = []
        for i in range(2,14):
            for j in range(4):
                self.cartas.append(Carta(i,j))
        shuffle(self.cartas)
    
    def quitar_carta(self):
        if len(self.cartas) == 0:
            return
        return self.cartas.pop()


##Prueba de creacion de mazo##        
#mazo = Mazo()

#for carta in mazo.cartas:
#    print (carta)

class Jugador:
    def __init__(self, nombre):
        self.ganada=0
        self.carta = None
        self.nombre = nombre


#### JUEGO DE GUERRA###

class Guerra:
    def __init__(self):
        nombre1 = input("Jugador 1:")
        nombre2 = input("Jugador 2:")
        self.mazo = Mazo()
        self.jugador1 = Jugador(nombre1)
        self.jugador2 = Jugador(nombre2)
        
    def ganador_ronda(self, ganador):
        g = "{} ganó esta ronda!"
        g = g.format(ganador)
        print(g)
        
    def ganador_juego (self, jugador1, jugador2):
        
        if jugador1.ganada > jugador2.ganada:
            return jugador1.nombre
        
        if jugador1.ganada < jugador2.ganada:
            return jugador2.nombre
        
        return "Fue un empate!"
        
    
    def robo(self, j1n,j1c,j2n,j2c):
        r = "{} robo {}  {} robo {}"
        r = r.format(j1n,j1c,j2n,j2c)
        print (r)
    
    def jugar(self):
        
        cartas = self.mazo.cartas
        print ("Comienza la guerra!!")
        
        while len(cartas) >= 2:
           
            instrucciones = " ´r´ para retirarse. Cualquier tecla para continuar: "
            respuesta = input(instrucciones)
            
            if respuesta == "r":
                break
        
            j1c = self.mazo.quitar_carta()
            j2c = self.mazo.quitar_carta()
            j1n = self.jugador1.nombre
            j2n = self.jugador2.nombre
            
            self.robo(j1n, j1c, j2n, j2c)
            if j1c > j2c:
                self.jugador1.ganada +=1
                self.ganador_ronda(self.jugador1.nombre)
            
            else:
                self.jugador2.ganada +=1
                self.ganador_ronda(self.jugador2.nombre)
            
        win = self.ganador_juego(self.jugador1, self.jugador2)
        print("Acabo la guerra, gano {}".format(win))
    
    
j = Guerra()
    
j.jugar()
    


