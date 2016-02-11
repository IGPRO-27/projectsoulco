# -*- coding: utf-8 -*-
#from datetime import timedelta
from openerp import models, fields, api, exceptions

class ProjectSoulcoTemplate(models.Model):
    _inherit = 'product.template'

    ean13 = fields.Char(string ="Réference S" ,  required=True)
    default_code = fields.Char(string ="Réference L" ,  required=True)
    num_serie = fields.Boolean(string="Seriable")

class ProjectSoulcoProduct(models.Model):
    _inherit = 'product.product'

    def _check_ean_key(self, cr, uid, ids, context=None):
        return True

    _constraints = [(_check_ean_key, 'override function', ['ean13'])]

class ProjectSoulcoStock(models.Model):
    _inherit = 'stock.transfer_details_items'

    #quantity = fields.Float(string ="Quantity")

    # @api.one
    # @api.constrains('quantity')
    # def _check_quantity(self):
    #     if self.product_id.track_all == True:
    #         print "PASSSSEEE TRACKKKKKKKKKKKKKKKKK"
    #         if self.quantity > 1:
    #             print "PASSSSSEEE QUANTITTTTTYYYYY"
    #             raise ValidationError("Quantity must be one")
