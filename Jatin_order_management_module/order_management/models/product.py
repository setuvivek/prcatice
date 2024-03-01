from odoo import fields, models

class Product(models.Model):
    _name = "product"
    _description = "Product"
    _rec_name = "name" #je rakhir te file upar setting ni bajuma show kare as a description
    # _order = 'name desc'
    name = fields.Char(string='Product Name' , required = True ,copy=False)
    number_of_product = fields.Integer(string='Number Of Product')
    mfg_date = fields.Date(string='Mfg Date')
    expr_date = fields.Date(string='Expr Date')
    order_id = fields.Many2one("order", string="order")
    # order_pro_ids = fields.Many2many("order","product_prd_tab","product_id","order_id",string="Orderrrr Name")
    #//"product_prd_tab" this table is created for many2many relation