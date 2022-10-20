# -*- coding: utf-8 -*-
from odoo import http

class MaterialMgt(http.Controller):

    def create_supplier(self, supplier_obj, name):
        return supplier_obj.create({
            'name': name
        })

    def create_material(self, material_obj, code, name, mtype, buy_price, supplier_id):
        return material_obj.create({
            'code': code,
            'name': name,
            'mtype': mtype,
            'buy_price': buy_price,
            'supplier_id': supplier_id,
        })
    
    def read_supplier(self, supplier_obj, supplier_id = None):
        if supplier_id == None:
            return supplier_obj.search([])
        else:
            return supplier_obj.search([('id','=',supplier_id)])
    
    def read_material(self, material_obj, material_id = None):
        if material_id == None:
            return material_obj.search([])
        else:
            return material_obj.search([('id','=',material_id)])
    
    def update_supplier(self, supplier_obj, supplier_id, data):
        supplier = supplier_obj.search([('id','=',supplier_id)])
        supplier[0].write(data)
        return supplier

    def update_material(self, material_obj, material_id, data):
        material = material_obj.search([('id','=',material_id)])
        material[0].write(data)
        return material
    
    def delete_supplier(self, supplier_obj, supplier_id):
        supplier = supplier_obj.search([('id','=',supplier_id)])
        supplier[0].unlink()
        return 0

    def delete_material(self, material_obj, material_id):
        material = material_obj.search([('id','=',material_id)])
        material[0].unlink()
        return 0

    @http.route('/material_mgt/test', auth='public')
    def index(self, **kw):
        material_1 = self.read_material(http.request.env['material_mgt.material'], 1)
        data = []
        for field in material_1[0]._fields:
            data.append({field: material_1[field]})
        return http.request.make_json_response(data)
    
    # Create Record

    # Read Record
    @http.route('/material_mgt/material/objects', auth='public')
    def material_list(self, **kw):
        return http.request.render('material_mgt.listing', {
            'root': '/material_mgt/material',
            'objects': http.request.env['material_mgt.material'].search([]),
        })

    @http.route('/material_mgt/material/objects/<model("material_mgt.material"):obj>', auth='public')
    def material_object(self, obj, **kw):
        return http.request.render('material_mgt.object', {
            'object': obj
        })

    @http.route('/material_mgt/supplier/objects', auth='public')
    def supplier_list(self, **kw):
        return http.request.render('material_mgt.listing', {
            'root': '/material_mgt/supplier',
            'objects': http.request.env['material_mgt.supplier'].search([]),
        })

    @http.route('/material_mgt/supplier/objects/<model("material_mgt.supplier"):obj>', auth='public')
    def supplier_object(self, obj, **kw):
        return http.request.render('material_mgt.object', {
            'object': obj
        })
    # Update Record
    # Delete Record
