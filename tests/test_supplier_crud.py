from odoo.tests.common import Form, TransactionCase

class PositiveTestCase(TransactionCase):
    def test_create_supplier(self):
        f = Form(self.env['material_mgt.supplier'])
        f.name = 'Supplier Test'
        so = f.save()
        self.assertIsInstance(so, type(self.env['material_mgt.supplier'])) and self.assertEqual(so.name, f.name)
    
    def test_read_supplier(self):
        suppliers = self.env['material_mgt.supplier'].search([])
        self.assertIsInstance(suppliers[0], type(self.env['material_mgt.supplier'])) and self.assertIsInstance(suppliers[len(suppliers)-1], type(self.env['material_mgt.supplier']))
    
    def test_update_supplier(self):
        suppliers = self.env['material_mgt.supplier'].search([])
        update = {
            'name': 'Supplier Test 02',
        }
        suppliers[0].write(update)
        self.assertIsInstance(suppliers[0], type(self.env['material_mgt.supplier'])) and self.assertEqual(suppliers[0].name, update.name)

    def test_delete_supplier(self):
        suppliers = self.env['material_mgt.supplier'].search([])
        original_len = len(suppliers)
        suppliers[0].unlink()
        new_suppliers = self.env['material_mgt.supplier'].search([])
        new_len = len(new_suppliers)
        self.assertTrue(new_len < original_len)

class NegativeTestCase(TransactionCase):
    def test_create_noname(self):
        f = Form(self.env['material_mgt.supplier'])
        success = False
        try:
            so = f.save()
            success = True
        except (Exception):
            success = False
        self.assertFalse(success)
    
    def test_read_notexist(self):
        suppliers = self.env['material_mgt.supplier'].search([('id','=',9999)])
        self.assertEqual(len(suppliers), 0)
    
    def test_update_noname(self):
        suppliers = self.env['material_mgt.supplier'].search([])
        update = {
            'name': None,
        }
        success = False
        try:
            suppliers[0].write(update)
            success = True
        except (Exception):
            success = False
        self.assertFalse(success)
        
    def test_delete_notexist(self):
        suppliers = self.env['material_mgt.supplier'].search([('id','=',9999)])
        try:
            suppliers[0].unlink()
            success = True
        except (Exception):
            success = False
        self.assertFalse(success)