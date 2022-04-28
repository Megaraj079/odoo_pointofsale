# -*- coding: utf-8 -*-

from odoo import api,fields,models


class Odoosales(models.Model):
    _name = "odoo.sales.billing"
    _description = "Odoo Sales"
    
   
    product_name=fields.Many2one(comodel_name='odoo.sales.inventory.detail',required=True)
    quantity=fields.Integer(String='quantity',required=True,default=1)
    price=fields.Integer(String='Price',required=True,related='product_name.price')
    gst=fields.Integer(String='GST',required=True,default='', related='product_name.gst')
    total=fields.Float(String='Total',compute='onchange_total',required=True,readonly=True)
    discount=fields.Selection([('0','None'),('5','5%'),('10','10%'),('15','15%')],default='0')
    create_product_record_id=fields.Many2one('odoo.sales.productdetails','product_name_id',String='product_id')
    product_image=fields.Binary(related='product_name.set_product_image',String="order image")
                
    #@api.onchange('product_name','quantity','price','gst','discount','total')             
    def onchange_total(self):
        
        for os_total in self:
            os_total.total = (os_total.price * os_total.quantity * (100 + os_total.gst ) * 0.01) * (100 - int(os_total.discount)) * 0.01
