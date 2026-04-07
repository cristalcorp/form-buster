import fitz
from pypdf import PdfReader

def read_pdf_accro(pdf_file):
    reader = PdfReader(pdf_file)

    fields = reader.get_fields()

    if fields is None:
        print("❌ Aucun champ trouvé (pas un PDF formulaire)")
    else:
        for name, field in fields.items():
            print(f"Nom du champ: {name}")
            print(f"  Valeur actuelle: {field.get('/V')}")
            print(f"  Type: {field.get('/FT')}")
            print()

def write_pdf_fitz(pdf_file):
    pdf_path = pdf_file
    output_path = "output_pdf_coord.pdf"

    doc = fitz.open(pdf_path)
    page = doc[0]

    page.insert_text(
        (225, 150),   # x, y
        "Jean Dupont",
        fontsize=11,
    )

    doc.save(output_path)
    doc.close()

