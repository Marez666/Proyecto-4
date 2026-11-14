# Clase
class Alumno:
    def __init__(self, nombre, matricula, calificacion1, calificacion2, calificacion3):
        self.nombre = nombre
        self.matricula = matricula
        self.calificacion1 = calificacion1
        self.calificacion2 = calificacion2
        self.calificacion3 = calificacion3

    def promedio(self):
        return (self.calificacion1 + self.calificacion2 + self.calificacion3) / 3


# Funciones auxiliares para validar la entrada
def pedir_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Debes ingresar un número mayor a 0.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")


def pedir_calificacion(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if 0 <= valor <= 100:
                return valor
            print("La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada inválida. Ingresa un número.")


# Captura de alumnos
cantidad = pedir_entero_positivo("¿Cuántos alumnos quieres registrar? ")

Alumnos = []
for i in range(cantidad):
    print(f"\n--- Alumno {i + 1} ---")
    nombre = input("Nombre: ")
    matricula = pedir_entero_positivo("Matrícula: ")
    cal1 = pedir_calificacion("Calificación 1: ")
    cal2 = pedir_calificacion("Calificación 2: ")
    cal3 = pedir_calificacion("Calificación 3: ")
    Alumnos.append(Alumno(nombre, matricula, cal1, cal2, cal3))

# Promedio general
promedio_general = sum(alumno.promedio() for alumno in Alumnos) / len(Alumnos)

# Promedios mayor y menor
promedio_mayor = 0
promedio_menor = 100
alumno_mayor = None
alumno_menor = None

for alumno in Alumnos:
    promedio_alumno = alumno.promedio()
    if promedio_alumno > promedio_mayor or alumno_mayor is None:
        promedio_mayor = promedio_alumno
        alumno_mayor = alumno
    if promedio_alumno < promedio_menor or alumno_menor is None:
        promedio_menor = promedio_alumno
        alumno_menor = alumno

# Resultados
print("\n=== Promedio de cada alumno ===")
for alumno in Alumnos:
    print(f"  {alumno.nombre} ({alumno.matricula}): {alumno.promedio():.2f}")

print("\nEl promedio general de todos los alumnos es:", f"{promedio_general:.2f}")
print(f"Promedio mayor: {promedio_mayor:.2f} -> {alumno_mayor.nombre} (matrícula {alumno_mayor.matricula})")
print(f"Promedio menor: {promedio_menor:.2f} -> {alumno_menor.nombre} (matrícula {alumno_menor.matricula})")