import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../datos/sales.csv")

df["Total"] = df["Cantidad"] * df["Precio"]

ventas_totales = df["Total"].sum()

print("Ventas totales:", ventas_totales)


ventas_producto = df.groupby("Producto")["Total"].sum()

print(ventas_producto)


ventas_producto.plot(kind="bar")

plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Total vendido")

plt.savefig("../resultados/grafico_ventas.png")

ventas_producto.to_csv("../resultados/resumen_ventas.csv")

print("Análisis finalizado")
