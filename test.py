import csv

def validar_permisos(input_csv, output_txt):
    usuarios_revisados = set()
    permisos_por_usuario = {}

    # Leer el archivo CSV y agrupar los permisos por userName
    with open(input_csv, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            user = row['userName']
            permiso = row['NewPermissionSet']

            if user not in permisos_por_usuario:
                permisos_por_usuario[user] = set()
            
            permisos_por_usuario[user].add(permiso[:6])  # Guardar solo los primeros 6 caracteres

    # Revisar si hay incongruencias
    with open(output_txt, mode='w', encoding='utf-8') as output_file:
        for user, permisos in permisos_por_usuario.items():
            if len(permisos) > 1:  # Si hay más de un valor de prefijo en permisos, hay inconsistencia
                output_file.write(f"Revisar usuario {user}: inconsistencias en los permisos\n")
    
    print(f"Proceso completado. Revisar el archivo {output_txt} para inconsistencias.")

# Uso del script
input_csv = 'permisos.csv'  # Reemplazar con el nombre de tu archivo CSV
output_txt = 'usuarios_inconsistentes.txt'
validar_permisos(input_csv, output_txt)
