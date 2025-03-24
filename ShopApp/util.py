import os

INVOICE_FILE = "invoice_number.txt"  

def get_next_invoice_number():
    if not os.path.exists(INVOICE_FILE):
        with open(INVOICE_FILE, "w") as file:
            file.write("0")  

    with open(INVOICE_FILE, "r") as file:
        last_invoice = int(file.read().strip())

    next_invoice = last_invoice + 1

  
    with open(INVOICE_FILE, "w") as file:
        file.write(str(next_invoice))

    # return next_invoice
    return str(next_invoice).zfill(6) 
