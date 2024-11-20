# ANTES: Empleado calcuola salario y hace reporte

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_salario(self):
        return self.salario

    def generar_reporte(self):
        # Genera un reporte de salario
        return f"Empleado: {self.nombre}, Salario: {self.salario}"
    
# Despues: Empleado calcula salario y hay otra clase para el reporte


class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_salario(self):
        return self.salario


class ReporteEmpleado:
    def generar_reporte(self, empleado):
        return f"Empleado: {empleado.nombre}, Salario: {empleado.salario}"
