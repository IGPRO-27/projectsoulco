# -*- coding: utf-8 -*-
#from datetime import timedelta
from openerp import models, fields, api, exceptions

class projectsoulco(models.Model):
    _inherit = 'product.template'

    num_serie = fields.Char(string ="Numéro de Série" ,  required=True)

    ean13 = fields.Char(string ="Réference S" ,  required=True)
    default_code = fields.Char(string ="Réference L" ,  required=True)

    _sql_constraints=[('num_serie','unique(num_serie)',"Num serie must be unique")]


class projectsoulcoproduct(models.Model):
    _inherit = 'product.product'

    def _check_ean_key(self, cr, uid, ids, context=None):
        return True

    _constraints = [(_check_ean_key, 'override function', ['ean13'])]













    # user_id = fields.Many2one('res.users', 'user', required=True)
    # sheet_id =  fields.Many2one("hr_timesheet_sheet.sheet", string="Sheets", required=True)
    #
    # Task_ids = fields.Many2one("project.task", string="Tache", required=True)
    # hour = fields.Float(string="Time Spent" , required=True)
    # work_ids =  fields.Many2one("project.task.work", string="Works")

    # def create(self,cr, uid, context=None, user_id)

    # if context is None:context ={}
    # model_name=context.get('active_model')
    #     emp_obj = self.pool.get('hr.employee')
    #     emp_id = emp_obj.search(cr, uid, [('user_id', '=', user_id)])
        # print "L'UTILISATEUR EST %s " %(emp_id.name)
