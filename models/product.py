# -*- coding: utf-8 -*-

from odoo import models, fields, api
class WeAddonProduct(models.Model):
    _inherit = ['product.template']
    _description = 'Product Erp extensions'
    # valtec = fields.Boolean( default=True, help="If unchecked, it will allow you to disable launch manufacturing")
    state = fields.Selection(selection=[
        ('new','New'),
        ('active', 'Confirmed'),
        ('under_lifecycle_change','Under Lifecycle Change'),
         ('inactive', 'Deactivated')
    ],string='State',required=True,store=True,readonly=True,default='draft')
    # @api.onchange('purchase_ok')
    # def _onchange_purchase_ok(self):
        # if not self.purchase_ok :
        #     self.valtec=True
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
