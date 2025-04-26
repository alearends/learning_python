from sistema_empleados_poo.empresa import Empresa
from sistema_empleados_poo.empleado import Empleado

print('*** Sistema de Empleados ***')

# Crear una instancia de una empresa
empresa1 = Empresa('Mi Empresa')

# Contratar algunos empleados
empresa1.contratar_empleado('Juan', 'Ventas')
empresa1.contratar_empleado('Maria', 'Marketing')
empresa1.contratar_empleado('Pedro', 'Ventas')
empresa1.contratar_empleado('Ana', 'Recursos Humanos')

# Obtener numero total de empleados de Empresa creada
print(f'Total de empleados en la empresa: {Empleado.obtener_total_empleados()}')

# Obtener numero empleados en el departamento de Ventas
print(f"Empleados en el deparatamento de Ventas: {empresa1.obtener_numero_empleados_departamento('Ventas')}")

# Mostrar todos los Empleados de la Empresa
empresa1.mostrar_todos_los_empleados()

# Para Ejecutar este Sistema:
# Abre la terminal en C:\Users\aleja\Documents\_Certificación_Web\Phyton IBM\IBM Python Avanzado\Experimentos\
# Ejecuta: python -m sistema_empleados_poo.prueba_empleados_empresa
