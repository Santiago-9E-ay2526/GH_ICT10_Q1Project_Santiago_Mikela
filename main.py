# Skills Test
from pyscript import display, document
# INDEX.HTML
#Calculate for receipt
def calc_receipt(e):
     # Get customer name
     name = document.getElementById('cust-name').value or "Valued Customer"

     #Clear previous output
     document.getElementById('receipt').innerHTML= " "

     subtotal = 0

     # Check selected items and calculate subtotal
     if document.getElementById('iced-coffee').checked:
          subtotal = subtotal + 120
     if document.getElementById('latte').checked:
          subtotal = subtotal + 150
     if document.getElementById('matcha').checked:
          subtotal = subtotal + 160
     if document.getElementById('choco-mousse').checked:
          subtotal = subtotal + 120
     if document.getElementById('caramel').checked:
          subtotal = subtotal + 120
     if document.getElementById('water').checked:
               subtotal = subtotal + 30
     if document.getElementById('cake').checked:
          subtotal = subtotal + 130

     # Calculate VAT and total
     vat = subtotal * 0.12
     total = subtotal + vat

     # Show receipt output
     display(f"""
          Customer Name: {name},
          Subtotal: ₱{subtotal:.2f},
          VAT: ₱{vat:.2f},
          Total Amount: ₱{total:.2f}
          """,
          target='receipt')


# SKU.HTML
#Calculate for SKU
def calc_sku(e):
     # Get category name
     theCategory = document.getElementById('Cat').value

     # SKU of category
     if theCategory == "perishables":
          categoryCode = "PER"
     elif theCategory == "non-perishables":
          categoryCode = "NPR"
     elif theCategory == "pastries":
          categoryCode = "PAS"
     elif theCategory == "beverages":
          categoryCode = "BEV"

     # Get product name (can be e.g. strawberry, vanilla (add-ons of the drinks), etc.)
     theProduct = document.getElementById('prod-name').value

     # SKU of product
     if theProduct == "iced-coffee":
          productCode = "ICF"
     elif theProduct == "latte":
          productCode = "LAT"
     elif theProduct == "matcha":
          productCode = "MAT"
     elif theProduct == "chocolate-mousse":
          productCode = "CHM"
     elif theProduct == "caramel-macchiato":
          productCode = "CRM"
     elif theProduct == "bottled-water":
          productCode = "BTW"
     elif theProduct == "chocolate-cake":
          productCode = "CHC"

     # Input stock amount
     theStock = document.getElementById('stoc-quan').value or '0'

     #Clear previous output
     document.getElementById('sku').innerHTML= " "

     # Show sku output
     display(f'{categoryCode}-{productCode}-{theStock}', target='sku')