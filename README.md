# ALEJANDRO BARRECHE RUIZ
## Examen Algoritmos


## Ordenamiento de burbuja. BUBBLE SORT

Es un **algoritmo** que _recorre repetidamente una lista que necesita ordenarse_. Compara elementos adyacentes y los intercambia si están en el orden incorrecto. Este procedimiento se repite hasta que no se requiere más intercambios, lo que indica que la lista se encuentra ordenada.

A continuación se muestra un código realizado por mi que _implementa el algoritmo de ordenamiento:_

```py
class Buble_sort():
    def __init__(self, lista):
        self._lista = lista
        self.tamaño = len(self.lista)

    
    @property
    def lista(self):
        return self._lista
    
    def algoritmo_ordenar(self):
        for i in range(self.tamaño):
            for j in range(self.tamaño - i - 1):
                if self.lista[j] > self.lista[j + 1]:
                    self.lista[j], self.lista[j+1] = self.lista[j + 1], self.lista[j]
        return self.lista
```

Si observamos el algoritmo vemos que su complejidad algorítmica es alta debido a los dos bucles necesarios para implementar el algoritmo, por lo que ***no sería un algoritmo muy efizac***. Esto conlleva que este algoritmo sea eficaz en pocas situaciones.

**¿CUÁNDO ES RECOMENDABLE USAR ESTE ALGORITMO?**

- Cuando la lista tenga una cantidad de elementos pequeña
- Cuando la lista se encuentre casi ordenada

**¿CÓMO FUNCIONA EL CÓDIGO?**

- El **primer bucle** nos permite ir reduciendo el límite superior; porque cada vez que recorramos toda la lista, sabemos que **al menos** el último elemento está ordenado, por lo que no es necesario compararlo en todas las iteraciones.

- El **segundo bucle** es el que nos permite comparar dos elementos adayacentes y realizar la lógica correspondiente:
    1. En caso de que los dos elementos sean iguales (_lista[j] == lista [j+1]_) no hará nada
    2. En caso de que el primer elemento sea menor que el segundo (_lista[j] < lista [j+1]_) no hará nada
    3. En caso de que el primer elemento sea mayor que el segundo (_lista[j] > lista [j+1]_) intercambiará los elementos y seguirá comprobando


### EJEMPLO DE APLICACIÓN DEL ALGORITMO
[34, 7 , 23, 32, 5]

**PRIMERA ITERACIÓN DEL BUCLE**

[**34**, **7** , 23, 32, 5]   (_34 > 7_) -->   [**7**, **34** , 23, 32, 5]

[7, **34** , **23**, 32, 5]   (_34 > 23_) -->   [7, **23** , **34**, 32, 5]

[7, 23 , **34**, **32**, 5]   (_34 > 32_) -->   [7, 23 , **32**, **34**, 5]

[7, 23 , 32, **34**, **5**]   (_34 > 5_) -->   [7, 23 , 32, **5**, **34**]

**SEGUNDA ITERACIÓN DEL BUCLE** (Comprueba hasta el elemento en la posición _3_ de la tabla)

[**7**, **23** , 32, 5, _34_]   (_7 < 23_) -->   [**7**, **23** , 32, 5, _34_]

[7, **23** , **32**, 5, _34_]   (_23 < 32_) -->   [7, **23** , **32**, 5, _34_]

[7, 23 , **32**, **5**, _34_]   (_32 > 5_) -->   [7, 23 , **5**, **32**, _34_]

**TERCERA ITERACIÓN DEL BUCLE** (Comprueba hasta el elemento en la posición _2_ de la tabla)

[**7**, **23** , 5, _32_, _34_]   (_7 < 23_) -->   [**7**, **23** , 5, _32_, _34_]

[7, **23** , **5**, _32_, _34_]   (_23 > 5_) -->   [7, **5** , **23**, _32_, _34_]

**CUARTA ITERACIÓN DEL BUCLE** (Comprueba hasta el elemento en la posición _1_ de la tabla)

[**7**, **5** , _23_, _32_, _34_]   (_7 > 5_) -->   [**5**, **7** , _23_, _32_, _34_]


**RESULTADO FINAL**

[_5_, _7_ , _23_, _32_, _34_]


## EJERCICIO RECURSIVIDAD. FACTORIAL DE UN NÚMERO

### **HIPÓTESIS**

- Proporcionar el factorial de un número 

### **PRECONDICIÓN**

- El número debe ser un _entero no negativo_

### **POSCONDICIÓN**

- La función _factorial()_ devuelve el factorial del número si se cumplen las condiciones

### **ENTRADA**

- Un _número_ cuyo tipo es '***int***'

### **SALIDA**

- El factorial del _número_ cuyo tipo también es '***int***'

### **EFECTO**

- Primero calculas el factorial de 1
- Para calcular el factorial de 2, multiplicas el número por el factorial del número anterior, en este caso el 1
- Para calcular el factorial de 3, multiplicas el número por el factorial del número anterior, en este caso el 2
- ...


