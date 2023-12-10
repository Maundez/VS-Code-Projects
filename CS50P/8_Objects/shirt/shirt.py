from fpdf import FPDF

class Shirt():
    def __init__(self, name) -> None:
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font('helvetica', "B", size=50)
        self._pdf.cell(0, 60, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
        
        self._pdf.image("shirt.png", w=self._pdf.epw) 
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x = 44, y = 135, text=f"{name} took CS50")
        
    def save(self, name):
        self._pdf.output(name)

name = input("Name: ")
pdf = Shirt(name)
pdf.save("shirtificate.pdf")
