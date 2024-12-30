# Importa la clase datetime del módulo para manejar fechas y horas
from datetime import datetime 
# Clase Empleado 
class Empleado:
    # Inicializa un objeto de la clase Empleado
    def __init__(self, nombre, salario, fecha_ingreso):
        # Almacena el nombre
        self.nombre = nombre
        # Almacena el salario
        self.salario = salario  
        # Almacena la fecha de ingreso
        self.fecha_ingreso = fecha_ingreso  

# Calcula la antigüedad en años a partir de la fecha de ingreso
def calcular_antiguedad(fecha_ingreso):
    # Obtiene la fecha y hora actuales
    hoy = datetime.now()  
    # Calcula la diferencia de años
    años = hoy.year - fecha_ingreso.year  
    # Ajusta la antigüedad (mes y día actuales son anteriores al mes y día de ingreso)
    if hoy.month < fecha_ingreso.month or (hoy.month == fecha_ingreso.month and hoy.day < fecha_ingreso.day):
        años -= 1 
        # Retorna la antigüedad en años 
    return años  

# Determina los beneficios según su antigüedad
def determinar_beneficios(años):
    #lista vacía para almacenar los beneficios
    beneficios = []
    # Bono anual si la antigüedad es de 5 años o más
    if años >= 5:
        beneficios.append("Bono anual")  
    # Días de vacaciones si la antigüedad es de 3 años o más
    if años >= 3:
        beneficios.append("5 días adicionales de vacaciones")
    # Retorna la lista de beneficios
    return beneficios  

# Ejecuta el flujo del programa
def principal():
    # Datos de prueba
    nombre_empleado = "María García"
    salario_empleado = 60000
    fecha_ingreso_empleado = datetime(2019, 3, 20)
    
    # Crear objeto empleado
    empleado = Empleado(nombre_empleado, salario_empleado, fecha_ingreso_empleado)
    
    # LLamada a las funciones
    antiguedad = calcular_antiguedad(empleado.fecha_ingreso)  
    beneficios = determinar_beneficios(antiguedad)
    
    # Muestra los resultados en la consola
    print(f"Empleado: {empleado.nombre}")  
    print(f"Salario: ${empleado.salario}")  
    print(f"Antigüedad: {antiguedad} años")
    print("Beneficios Asignados:", ", ".join(beneficios) if beneficios else "Ninguno")

if __name__ == "__main__":
    # Llama a la función principal al ejecutar el script
    principal()  