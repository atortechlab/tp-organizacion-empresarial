import pandas as pd
import matplotlib.pyplot as plt

# Leer dataset
df = pd.read_csv("../datos/sales.csv")

# Crear columna total
df["Total"] = df["Cantidad"] * df["Precio"]

# Ventas totales
ventas_totales = df["Total"].sum()

print("Ventas totales:", ventas_totales)

# Agrupar por producto
ventas_producto = df.groupby("Producto")["Total"].sum()

print(ventas_producto)

# Graficar
ventas_producto.plot(kind="bar")

plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Total vendido")

# Guardar gráfico
plt.savefig("../resultados/grafico_ventas.png")

# Guardar resultados
ventas_producto.to_csv("../resultados/resumen_ventas.csv")

print("Análisis finalizado")
