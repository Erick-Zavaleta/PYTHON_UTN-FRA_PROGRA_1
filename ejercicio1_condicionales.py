# A partir del ingreso de la altura en centimetros de un jugador de baloncesto, el programa debera
# determinar la posicion del jugador en la cancha, considerando los siguientes parametros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o mas: Ala-Pivot o Pivot


try:
    altura = float(input("Ingrese su altura en cm, para indicar su posicion de juego: "))

    if altura <= 0 or altura >= 300:
        print("Por favor, ingrese una altura válida.")

    elif altura < 160:
        print(f"Con {altura} cm de altura, su posición es base.")

    elif altura <= 179:
        print(f"Con {altura} cm de altura, su posición es escolta.")

    elif altura <= 199:
        print(f"Con {altura} cm de altura, su posición es alero.")

    else:
        print(f"Con {altura} cm de altura, su posición es ala-pivot o pivot.")

except ValueError:
    print("Por favor, ingrese un número válido en centímetros.")