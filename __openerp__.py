# -*- coding: utf-8 -*-
{
    'name': "Projet Soulco",

    'summary': """Design Odoo for Soulco Client""",

    'description': """
        Link Tasks to projects:
    """,

    'author': "IGPRO",
    'website': "http://igpro-online.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['project','sale','stock','purchase'],

    # always loaded
    'data': [
        'project_soulco.xml',
        'project_soulco_report.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
