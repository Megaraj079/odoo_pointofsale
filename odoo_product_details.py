from odoo import  api,fields,models

class Odoosalesproductdetails(models.Model):
    _name = "odoo.sales.product_details"
    _description = "odoo sales Product details"      
  
    
    name=fields.Many2one(comodel_name='odoo.sales.customer',required=True)    
    grand_total=fields.Integer(compute='onchange_grand_total', String='grand_total',required=True)
    product_name_id=fields.One2many('odoo.sales.billing','create_product_record_id',String='product_many_to_one')
   
    
    @api.onchange('name','grand_total','product_name_id')            
    def onchange_grand_total(self):
        for find_total in self:
            find_total.grand_total = 0
            for find_product_total in find_total.product_name_id :
                find_total.grand_total += find_product_total.total
                
                
