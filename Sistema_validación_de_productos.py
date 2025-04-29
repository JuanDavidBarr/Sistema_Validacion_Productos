#Sistema de validación de productos
#Inicializamos las variables que guardaran la data ingresada por el usuario
while True:
    nombre_producto = input("Ingrese el nombre del producto: ")


#Usamos el loop while para preguntar el precio del producto una vez más, hasta que el usuario ingrese un valor válido.
    while True:
        precio_unidad_producto = input("Ingrese el precio por unidad del producto: ")
        cantidad_de_productos_adquiridos = input("Ingrese la cantidad de productos adquiridos: ")
        porcentaje_descuento = input("Ingrese el porcentaje de descuento: ")
    
    
#Validamos las variables ingresadas por el usuario. Utilizamos "is alpha" para validar que el valor ingresado sea numérico.
        if precio_unidad_producto.isdigit() and cantidad_de_productos_adquiridos.isdigit() and porcentaje_descuento.isdigit():
#Convertimos las variables a su tipo de dato correspondiente, además agregamos "abs" para evitar que el usuario ingrese un valor negativo.
            precio_unidad_producto = abs(float(precio_unidad_producto))
            cantidad_de_productos_adquiridos = abs(int(cantidad_de_productos_adquiridos))
            porcentaje_descuento = abs(float(porcentaje_descuento))
        
        
#Validamos que el porcentaje de descuento ingresado se encuentre entre 0 y 100.
            if porcentaje_descuento < 0 or porcentaje_descuento > 100:
                print("Por favor, ingrese un porcentaje de descuento válido entre 0 y 100.")
            else:
                break
        else:
            print("Por favor, ingrese solo valores numéricos.")
        
        
#Preguntamos al usuario si el producto tiene un descuento
#Usamos el loop while para preguntar si el producto tiene descuento una vez más, hasta que el usuario ingrese un valor válido.
    while True:
#Usamos los metodos lower y strip, el primero para asegurarnos de que la respuesta sea en minúscula. El segundo para eliminar espacios al inicio y al final.
        producto_tiene_descuento = input("¿El producto tiene descuento? (si/no): ").lower().strip()
    
    
#Validamos si el producto tiene descuento
        if producto_tiene_descuento == "no":
#Calculamos el costo total de la compra sin descuento
            costo_total_compra = precio_unidad_producto * cantidad_de_productos_adquiridos
#Redondeamos el resultado a 2 decimales
            costo_total_compra = round(costo_total_compra, 2)
            print(f"El costo total de {cantidad_de_productos_adquiridos} unidad/es de {nombre_producto} es: {costo_total_compra}")
            break
    
    
        elif producto_tiene_descuento == "si":
            costo_total_compra = precio_unidad_producto * cantidad_de_productos_adquiridos
#Calculamos el costo total de la compra con descuento. Usamos abs para asegurarnos que la resta de un valor positivo.
            costo_final_compra_descuento = costo_total_compra * abs(porcentaje_descuento - 100)/100
#Redondeamos el resultado a 2 decimales
            costo_final_compra_descuento = round(costo_final_compra_descuento, 2)
            print(f"El costo total de {cantidad_de_productos_adquiridos} unidad/es de {nombre_producto} es: {costo_final_compra_descuento}")
            break
        else:
            print("Ingrese por favor una respuesta válida (si/no).")
            
            
#Preguntamos al usuario si desea ingresar otro producto
    producto_adicional = input("¿Desea ingresar otro producto? (si/no): ").lower().strip()
#Validamos la respuesta del usuario
    if producto_adicional == "no":
        print("Gracias por usar el sistema de validación de productos.")
        break
    elif producto_adicional != "si":
        print("Ingrese por favor una respuesta válida (si/no).")
#El programa termina cuando el usuario ingresa "no" a la pregunta de si desea ingresar otro producto.
    

    

