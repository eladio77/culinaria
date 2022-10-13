from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = "res.partner"
    
    c_nombre_fantasia = fields.Char(
        string='C_nombre_fantasia', 
        required=False)
