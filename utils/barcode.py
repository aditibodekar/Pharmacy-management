import barcode
from barcode.writer import ImageWriter

def create_barcode(code):
    code128 = barcode.get('code128', code, writer=ImageWriter())
    filename = code128.save(f"static/barcodes/{code}")
    return filename