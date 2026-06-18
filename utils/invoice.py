from reportlab.pdfgen import canvas

def generate_invoice(invoice_id, amount):
    filename = f"reports/invoices/{invoice_id}.pdf"

    c = canvas.Canvas(filename)
    c.drawString(100, 750, f"Invoice ID: {invoice_id}")
    c.drawString(100, 730, f"Amount: {amount}")
    c.save()

    return filename