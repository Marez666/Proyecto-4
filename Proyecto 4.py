# clase 
class Alumno:
    def __init__(self, nombre, matricula, calificacion1, calificacion2, calificacion3):
        self.nombre = nombre
        self.matricula = matricula
        self.calificacion1 = calificacion1
        self.calificacion2 = calificacion2
        self.calificacion3 = calificacion3
    def promedio(self):
        return (self.calificacion1 + self.calificacion2 + self.calificacion3) / 3

#Alumnos
Alumnos = [
    Alumno("Angel", 26496709, 60, 70, 80),
    Alumno("Matias", 26499447, 85, 90, 95),
    Alumno("Luisa", 26491056, 80, 85, 90),
    Alumno("Jorge", 26490409, 75, 80, 85),
    Alumno("Daniela", 26491054, 95, 100, 100),
    Alumno("Martin", 26492065, 100, 100, 100),
    Alumno("Sofia", 26491057, 85, 90, 95),
    Alumno("Valentina", 26491058, 90, 95, 100),
    Alumno("Diego", 26491059, 70, 75, 80),
    Alumno("Camila", 26491060, 75, 80, 85)
]
# Promedio general
promedio_general = sum(alumno.promedio() for alumno in Alumnos) / len(Alumnos)

# Promedios mayor y menor 
promedio_mayor = 0
promedio_menor = 100
alumno_mayor = None
alumno_menor = None

for alumno in Alumnos:
    promedio_alumno = alumno.promedio()
    if promedio_alumno > promedio_mayor:
        promedio_mayor = promedio_alumno
        alumno_mayor = alumno
    if promedio_alumno < promedio_menor:
        promedio_menor = promedio_alumno
        alumno_menor = alumno
# Promedio de cada alumno, uno por uno
for alumno in Alumnos:
    print(f"  {alumno.nombre} ({alumno.matricula}): {alumno.promedio():.2f}")

print("El promedio de general de todos los alumnos es:", f"{promedio_general:.2f}")
print(f"Promedio mayor: {promedio_mayor:.2f} -> {alumno_mayor.nombre} (matrícula {alumno_mayor.matricula})")
print(f"Promedio menor: {promedio_menor:.2f} -> {alumno_menor.nombre} (matrícula {alumno_menor.matricula})")