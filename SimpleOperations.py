from functools import partial

class SimpleOperations:
    
    def apply_discount(self, price, discount):
        """Aplica un descuento al precio dado y retorna el nuevo precio."""
        return price * (1 - discount)
        

    def calculate_tax(self, price, tax_rate):
        """Calcula y agrega el impuesto al precio dado."""
        return price * (1 + tax_rate)

# Crear una instancia de SimpleOperations


def main():
    print("=================================================================.")
    print("Test Case 1: Apply Discount")
    print("=================================================================.")
    # Crear instancia de SimpleOperations
    simple_ops = SimpleOperations()
    # Definir una versión especializada de apply_discount con un descuento del 10%
    apply_10_percent_discount = partial(simple_ops.apply_discount, discount=0.10)  # Dejamos un argumento definido, en este caso el de descuento
    
    
    # Calcular el precio final con el descuento del 10%
    precio = 100
    precio_con_descuento = apply_10_percent_discount(precio)
    print(f"El precio original es: {precio}")
    print(f"Precio con 10% de descuento: {precio_con_descuento}")

    print("=================================================================.")
    print("Test Case 2: Calculate Tax")
    print("=================================================================.")
    # Definir una versión especializada de calculate_tax con una tasa de impuesto del 21%
    calculate_21_percent_tax = partial(simple_ops.calculate_tax, tax_rate=0.21)
    
    # Calcular el precio final con el impuesto del 21%
    precio_con_impuesto = calculate_21_percent_tax(precio)
    print(f"El precio original es: {precio}")
    print(f"Precio con 21% de impuesto: {precio_con_impuesto}")

# Comprobar si este módulo se ejecuta como un script independiente
if __name__ == "__main__":
    main()


