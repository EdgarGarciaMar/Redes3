#Imports de la clase
from fpdf import FPDF

"""
En esta clase se usa la biblioteca de FPDF, para construir los pdfs de los reportes,
esta clase es llamada por la clase Menu
"""
class Fpdf(FPDF):
    pass #dormir el constructor

    #Mètodo para agregar imagenes al pdf
    def logo(self,name,x,y,w,h):
        self.image(name,x,y,w,h)
    #Mètodo para generar el cuerpo del pdf segùn la informaciòn del archivo del agente
    def texts(self):
        with open("/home/edgar/Documents/GitHub/Redes3/4. AdministraciónDeContabilidad/P/reporte.txt","rb") as xy:
            txt = xy.read().decode("latin-1")
            self.set_xy(10.0,300.0)
            self.set_text_color(76.0,32,250)
            self.set_font("Arial","",12)
            self.multi_cell(0,10,txt)
    def texts2(self):
        txt = "Estadisticas".center(50,"-")
        self.set_xy(60.0,70.0)
        self.set_text_color(76.0,32,250)
        self.set_font("Arial","",12)
        self.multi_cell(0,10,txt)
    #Mètodo para generar el titulo del pdf
    def titles(self,title):
        self.set_xy(0.0,0.0)
        self.set_font("Arial","B",16)
        self.set_text_color(220,50,50)
        self.cell(w=210.0,h=40.0,align="C",txt=title,border=0)
#Menu de prueba del pdf
if __name__ == "__main__":
    pdf = Fpdf()
    pdf.add_page()
    pdf.titles("localhost")
    pdf.texts("localhost")
    pdf.set_author("Gestor de SNMP")
    pdf1 = "localhost100" + ".pdf"
    pdf.output(pdf1)