
from fpdf import FPDF

class Fpdf(FPDF):
    pass #dormir el constructor
    def logo(self,name,x,y,w,h):
        self.image(name,x,y,w,h)

    def texts(self,name):
        with open(name+".txt","rb") as xy:
            txt = xy.read().decode("latin-1")
            self.set_xy(10.0,80.0)
            self.set_text_color(76.0,32,250)
            self.set_font("Arial","",12)
            self.multi_cell(0,10,txt)

    def titles(self,title):
        self.set_xy(0.0,0.0)
        self.set_font("Arial","B",16)
        self.set_text_color(220,50,50)
        self.cell(w=210.0,h=40.0,align="C",txt=title,border=0)

if __name__ == "__main__":
    pdf = Fpdf()
    pdf.add_page()
    pdf.titles("localhost")
    pdf.texts("localhost")
    pdf.set_author("Gestor de SNMP")
    pdf1 = "localhost100" + ".pdf"
    pdf.output(pdf1)