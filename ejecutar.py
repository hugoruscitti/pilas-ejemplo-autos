import pilasengine
import math

pilas = pilasengine.iniciar()


class AutoTaxi(pilasengine.actores.Actor):

    def iniciar(self, velocidad_inicial):
        self.imagen = "taxi.png"

        # Elije una posicion inicial
        x = pilas.azar(-200, 200)
        y = -300

        # Arma la caja de colision con rotacion al azar
        self.figura = self.pilas.fisica.Rectangulo(x, y, 50, 110)
        self.figura.rotacion = pilas.azar(-30, 30)

        self.imitar(self.figura)
        self.velocidad = velocidad_inicial

    def avanzar(self):
        rotacion_en_radianes = math.radians(self.figura.rotacion + 90)
        dx = math.cos(rotacion_en_radianes) * self.velocidad
        dy = math.sin(rotacion_en_radianes) * self.velocidad
        self.x += dx
        self.y += dy

    def actualizar(self):
        self.avanzar()

        if self.y > 300:
            self.eliminar()


class AutoProtagonista(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "protagonista.png"
        self.figura = self.pilas.fisica.Rectangulo(200, 0, 50, 110, dinamica=False)
        self.imitar(self.figura)
        self.aprender('moverseComoCoche')


pilas.actores.vincular(AutoTaxi)
pilas.actores.vincular(AutoProtagonista)

protagonista = pilas.actores.AutoProtagonista()


def crear_taxi():
    taxi = pilas.actores.AutoTaxi(pilas.azar(1, 4))


# Genera un taxi cada 3 segundos
pilas.tareas.siempre(3, crear_taxi)

pilas.fisica.eliminar_paredes()
pilas.fisica.eliminar_suelo()
pilas.fisica.eliminar_techo()



pilas.fisica.definir_gravedad(0, 0)



pilas.ejecutar()
