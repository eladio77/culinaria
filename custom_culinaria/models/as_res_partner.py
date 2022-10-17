from odoo import fields, models, api


class ResPartnerExtend(models.Model):
    _inherit = "res.partner"
    
    c_nombre_fantasia = fields.Char(
        string='c_nombre_fantasia',
        required=False)
    
    email_alt = fields.Char(
        string='Email_alt', 
        required=False)