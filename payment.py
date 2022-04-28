from odoo import api,fields,models

class Odoosalespayment(models.Model):
    
    _name="odoo.sales.payment"
    _description="odoo sales Payment"
    
    grand_total = fields.Float(String='grand_total')
    cash=fields.Float(String='cash')
    upi_payment = fields.Char(String='upi_payment')
    card_payment = fields.Selection([('credit','Credit'),('debit','Debit')],required=True)
    card_bank = fields.Selection([('sbi','SBI'),('icici','ICICI'),('iob','IOB'),('axis','AXIS'),('hdfc','HDFC'),('indian bank','Indian Bank')]) 
    card_holder=fields.Char(String='card_holder')
    card_number=fields.Integer(String='card_number')
    
    def online_payment(self):
        print('upi_payment')