meses = {
    "enero": {"dias": 31, "festivos": ["Año Nuevo"]},
    "febrero": {"dias": 28, "festivos": ["Día de San Valentín"]},
    "marzo": {"dias": 31, "festivos": ["Día de San José"]},
    "abril": {"dias": 30, "festivos": []},
    "mayo": {"dias": 31, "festivos": ["Día del Trabajo"]},
    "junio": {"dias": 30, "festivos": []},
    "julio": {"dias": 31, "festivos": []},
    "agosto": {"dias": 31, "festivos": []},
    "septiembre": {"dias": 30, "festivos": []},
    "octubre": {"dias": 31, "festivos": []},
    "noviembre": {"dias": 30, "festivos": []},
    "diciembre": {"dias": 31, "festivos": ["Navidad"]}
}
nombre_mes = input("Ingrese el nombre de un mes del año: ")
if nombre_mes in meses:
    datos_mes = meses[nombre_mes]
    print(f"{nombre_mes} tiene {datos_mes['dias']} días.")
    if datos_mes['festivos']:
        print(f"Festivos: {', '.join(datos_mes['festivos'])}")
    else:
        print("No hay festivos en este mes.")
else:
    print("El mes ingresado no es válido.")





