# -*- coding: utf-8 -*-

from odoo import exceptions, models, fields, api

class material_mgt(models.Model):
    _name = 'material_mgt.supplier'
    _description = 'material_mgt.supplier'

    name = fields.Char(string='Name', required=True)

    @api.constrains('name')
    def _validate_name(self):
        for record in self:
            if len(record.name) < 1: 
                raise exceptions.ValidationError('Name cannot be empty')
