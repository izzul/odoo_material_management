# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class material_mgt(models.Model):
    _name = 'material_mgt.material'
    _description = 'material_mgt.material'

    code = fields.Char(string='Code', required=True)
    name = fields.Char(string='Name', required=True)
    buy_price = fields.Float(string='Buy Price', required=True)
    mtype = fields.Selection(string='Type', selection=[('fabric', 'Fabric'),('jeans', 'Jeans'),('cotton','Cotton')], required=True)
    supplier_id = fields.Many2one('material_mgt.supplier', string="Supplier", ondelete='cascade', required=True)

    # Enforce buy price minimum 100
    @api.constrains('buy_price')
    def _min_price(self):
        for record in self:
            if record.buy_price < 100: 
                raise exceptions.ValidationError('Buy Price cannot be less than 100')
    
    @api.constrains('name')
    def _validate_name(self):
        for record in self:
            if len(record.name) < 1: 
                raise exceptions.ValidationError('Name cannot be empty')
    
    @api.constrains('code')
    def _validate_code(self):
        for record in self:
            if len(record.code) < 1: 
                raise exceptions.ValidationError('Code cannot be empty')

