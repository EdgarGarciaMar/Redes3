
with open("P/reporte.txt", "rb") as xy:
    txt = xy.read().decode("latin-1")
print(type(txt))
print(txt)