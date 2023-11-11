class Curso: 
    def __init__(self, nombre, codigo):
        self.nombre=nombre
        self.codigo=codigo
        self.estudiantes_inscritos=[]

    def inscribir_estudiante(self, estudiante):
        self.estudiantes_inscritos.append(estudiante)
    
    def mostrar_estudiantes(self):
        print(f"Estudiantes inscritos en el curso '{self.nombre}':")
        for estudiante in self.estudiantes_inscritos:
            print(estudiante)