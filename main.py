import pandas as pd

# Cargar los archivos
csv_file = "usuarios_permisos.csv"  # Nombre del archivo CSV
excel_file = "permisos.xlsx"  # Nombre del archivo Excel

# Leer el CSV
df_csv = pd.read_csv(csv_file)

# Leer el archivo de Excel con todas sus hojas
sheets = pd.read_excel(excel_file, sheet_name=None)  # Dict con hojas

# Función para obtener las primeras 4 palabras del accountName
def get_sheet_name(account_name):
    return " ".join(account_name.split()[:4])  # Toma las primeras 4 palabras

# Crear una lista para almacenar los resultados
resultados = []

# Procesar cada fila del CSV
for _, row in df_csv.iterrows():
    account_name = row["accountName"]
    user_name = row["userName"]
    permission_name = row["permissioName"]  # Cuidado con el nombre exacto de la columna
    
    # Obtener el nombre de la hoja
    sheet_name = get_sheet_name(account_name)
    
    if sheet_name in sheets:
        df_sheet = sheets[sheet_name]  # Obtener la hoja
        # Buscar el permissionName en la hoja
        match = df_sheet[df_sheet["permissionName"] == permission_name]
        
        if not match.empty:
            new_group = match["newGroup"].values[0]
            resultados.append([account_name, user_name, permission_name, new_group])
        else:
            print(f"Permiso '{permission_name}' no encontrado en hoja '{sheet_name}'")
    else:
        print(f"No se encontró la hoja para '{sheet_name}'")

# Convertir resultados a DataFrame y guardarlos
df_resultado = pd.DataFrame(resultados, columns=["accountName", "userName", "permissionName", "newGroup"])
df_resultado.to_csv("usuarios_con_grupo.csv", index=False)

print("Proceso completado. Resultados guardados en 'usuarios_con_grupo.csv'")
