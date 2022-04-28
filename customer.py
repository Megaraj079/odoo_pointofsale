from odoo import api,fields,models

class OdoosalesproductID(models.Model):
    
    _name="odoo.sales.customer"
    _description="odoo sales Customer"
    
    customer_id=fields.Integer(string='customer_id',required=True)
    name=fields.Char(string='name',required=True)
    gender=fields.Selection([('male','Male'),('female','Female'),('non-binary','Non-binary')],string='gender')
    
    _sql_constraints=[('unique_customer_id','unique(customer_id)','This Customer ID already exists')]
    _order='customer_id asc'
    
