
from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'


    direccion_entrega = fields.Char('Dirección de entrega')

    l10n_latam_document_number = fields.Char('Guía de Despacho Número')



    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'invoice_origin' in vals:
                stock = self.env['stock.picking'].search([('origin','=',vals.get('invoice_origin'))], limit=1)
                for record in stock:
                    if record.l10n_latam_document_number:
                        vals['l10n_latam_document_number'] = record.l10n_latam_document_number
                    vals['direccion_entrega'] = record.partner_id.street
        return super(AccountGroup, self).create(vals_list)
    