# -*- coding: utf-8 -*-
#from datetime import timedelta
from openerp import models, fields, api, exceptions
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp
from datetime import datetime

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

class stock_transfer_details(models.TransientModel):
    _inherit = 'stock.transfer_details'

    def default_get(self, cr, uid, fields, context=None):
        print "DOOOOOOOOOOOOOOO TRANSFERRRRRRRRRRRRRRRRRRRRRTTTTTT"
        if context is None: context = {}
        res = super(stock_transfer_details, self).default_get(cr, uid, fields, context=context)
        picking_ids = context.get('active_ids', [])
        active_model = context.get('active_model')

        if not picking_ids or len(picking_ids) != 1:
            # Partial Picking Processing may only be done for one picking at a time
            return res
        assert active_model in ('stock.picking'), 'Bad context propagation'
        picking_id, = picking_ids
        picking = self.pool.get('stock.picking').browse(cr, uid, picking_id, context=context)
        print picking
        items = []
        packs = []
        if not picking.pack_operation_ids:
            picking.do_prepare_partial()
        for op in picking.pack_operation_ids:
            for n in range(1, int(op.product_qty)+1):
                print n
                item = {
                    'packop_id': op.id,
                    'product_id': op.product_id.id,
                    'product_uom_id': op.product_uom_id.id,
                    'quantity': 1,
                    'package_id': op.package_id.id,
                    'lot_id': op.lot_id.id,
                    'sourceloc_id': op.location_id.id,
                    'destinationloc_id': op.location_dest_id.id,
                    'result_package_id': op.result_package_id.id,
                    'date': op.date,
                    'owner_id': op.owner_id.id,
                }
                if op.product_id:
                    items.append(item)
                elif op.package_id:
                    packs.append(item)
        res.update(item_ids=items)
        res.update(packop_ids=packs)
        return res

    @api.one
    def do_detailed_transfer(self):
        processed_ids = []
        # Create new and update existing pack operations
        for lstits in [self.item_ids, self.packop_ids]:
            for prod in lstits:
                pack_datas = {
                    'product_id': prod.product_id.id,
                    'product_uom_id': prod.product_uom_id.id,
                    'product_qty': prod.quantity,
                    'package_id': prod.package_id.id,
                    'lot_id': prod.lot_id.id,
                    'location_id': prod.sourceloc_id.id,
                    'location_dest_id': prod.destinationloc_id.id,
                    'result_package_id': prod.result_package_id.id,
                    'date': prod.date if prod.date else datetime.now(),
                    'owner_id': prod.owner_id.id,
                }
                if prod.packop_id:
                    prod.packop_id.with_context(no_recompute=True).write(pack_datas)
                    processed_ids.append(prod.packop_id.id)
                else:
                    pack_datas['picking_id'] = self.picking_id.id
                    packop_id = self.env['stock.pack.operation'].create(pack_datas)
                    processed_ids.append(packop_id.id)
        # Delete the others
        # packops = self.env['stock.pack.operation'].search(['&', ('picking_id', '=', self.picking_id.id), '!', ('id', 'in', processed_ids)])
        # packops.unlink()
        self.picking_id.do_transfer()

        return True
