# Skills Test
from pyscript import display, document
# INDEX.HTML
#Calculate for receipt
def calc_receipt(e):
     # Get customer name
     name = document.getElementById('cust-name').value or "Valued Customer"

     #Clear previous output
     document.getElementById('receipt').innerHTML= " "

     # Calculate subtotal
     subtotal = (
     120 * document.getElementById('iced-coffee').checked
     + 150 * document.getElementById('latte').checked
     + 160 * document.getElementById('matcha').checked
     + 120 * document.getElementById('choco-mousse').checked
     + 120 * document.getElementById('caramel').checked
     + 30 * document.getElementById('water').checked
     + 130 * document.getElementById('cake').checked
     )

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
     
     # Get category code
     categoryCode = document.getElementById('Cat').value

     # Get product code
     productCode = document.getElementById('prod-name').value

     # Get stock amount
     theStock = document.getElementById('stoc-quan').value or '0'

     #Clear previous output
     document.getElementById('sku').innerHTML= " "

     # Show sku output
     display(f'{categoryCode}-{productCode}-{theStock}', target='sku')
