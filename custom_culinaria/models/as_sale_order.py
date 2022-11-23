from odoo import fields, models, api




class saleorder(models.Model):
    _inherit = 'sale.order'
    
    
    rut = fields.Char(
        string='rut', related='partner_id.vat'
    )
    

    

