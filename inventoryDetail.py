from odoo import api,fields,models

class OdoosalesproductID(models.Model):
    _name = "odoo.sales.inventory.detail"
    _description = "Odoo sales Inventory"        
    
    name=fields.Char(string='name',required=True)
    price=fields.Integer(String='price',required=True)
    gst=fields.Integer(String='GST',required=True)
    quantity=fields.Integer(String='quantity',required=True)
    set_product_image=fields.Binary(String='set_product_image')
    state=fields.Selection([('godown','Godown'),('selling floor','Selling floor')],string="status",default='godown')