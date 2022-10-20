from odoo.tests.common import Form, TransactionCase

class PositiveTestCase(TransactionCase):
    def test_create_material(self):
        f = Form(self.env['material_mgt.material'])
        f.code = '#Mtest01'
        f.name = 'Test Material 01'
        f.mtype = 'jeans'
        f.buy_price = 200
        f.supplier_id = self.env['material_mgt.supplier'].search([('id','=',1)])
        so = f.save()
        self.assertIsInstance(so, type(self.env['material_mgt.material'])) and self.assertEqual(so.code, f.code) and self.assertEqual(so.name, f.name) and self.assertEqual(so.mtype, f.mtype) and self.assertEqual(so.buy_price, f.buy_price)
    
    def test_read_material(self):
        materials = self.env['material_mgt.material'].search([])
        self.assertIsInstance(materials[0], type(self.env['material_mgt.material'])) and self.assertIsInstance(materials[len(materials)-1], type(self.env['material_mgt.material']))
    
    def test_update_material(self):
        materials = self.env['material_mgt.material'].search([])
        update = {
            'code': '#Mtest02',
            'name': 'Test Material 02',
            'mtype': 'fabric',
            'buy_price': 110,
            'supplier_id': self.env['material_mgt.supplier'].search([('id','=',2)]),
        }
        materials[0].write(update)
        self.assertIsInstance(materials[0], type(self.env['material_mgt.material'])) and self.assertEqual(materials[0].code, update.code) and self.assertEqual(materials[0].name, update.name) and self.assertEqual(materials[0].mtype, update.mtype) and self.assertEqual(materials[0].buy_price, update.buy_price)

    def test_delete_material(self):
        materials = self.env['material_mgt.material'].search([])
        original_len = len(materials)
        materials[0].unlink()
        new_materials = self.env['material_mgt.material'].search([])
        new_len = len(new_materials)
        self.assertTrue(new_len < original_len)


class NegativeTestCase(TransactionCase):
    def test_create_empty(self):
        f = Form(self.env['material_mgt.material'])
        success = False
        try:
            so = f.save()
            success = True
        except (Exception):
            success = False
        self.assertFalse(success)
    
    def test_create_out_type(self):
        f = Form(self.env['material_mgt.material'])
        f.code = '#Mtest01'
        f.name = 'Test Material 01'
        f.mtype = 'velvet'
        f.buy_price = 200
        f.supplier_id = self.env['material_mgt.supplier'].search([('id','=',1)])
        success = False
        try:
            so = f.save()
            success = True
        except (Exception):
            success = False
        self.assertFalse(success)
    
    def test_create_cheap_price(self):
        f = Form(self.env['material_mgt.material'])
        f.code = '#Mtest01'
        f.name = 'Test Material 01'
        f.mtype = 'cotton'
        f.buy_price = 10
        f.supplier_id = self.env['material_mgt.supplier'].search([('id','=',1)])
        success = False
        try:
            so = f.save()
            success = True
        except (Exception):
            success = False
        self.assertFalse(success)
    
    def test_read_notexist(self):
        materials = self.env['material_mgt.material'].search([('id','=',9999)])
        self.assertEqual(len(materials), 0)
    
    def test_update_noname(self):
        materials = self.env['material_mgt.material'].search([])
        update = {
            'name': None,
        }
        success = False
        try:
            materials[0].write(update)
            success = True
        except (Exception):
            success = False
        self.assertFalse(success)
    
    def test_update_nocode(self):
        materials = self.env['material_mgt.material'].search([])
        update = {
            'code': None,
        }
        success = False
        try:
            materials[0].write(update)
            success = True
        except (Exception):
            success = False
        self.assertFalse(success)
        
    def test_delete_notexist(self):
        materials = self.env['material_mgt.material'].search([('id','=',9999)])
        try:
            materials[0].unlink()
            success = True
        except (Exception):
            success = False
        self.assertFalse(success)