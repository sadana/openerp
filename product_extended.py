from openerp.osv import osv, fields

class product_extended(osv.osv):
    _inherit = "product.product"
    _columns = {
        'life_time': fields.integer('Life time', help="Number of day(s) the product can use before expired.")
        }
    _defaulds = {
        'life_time': 0
    }

product_extended()
