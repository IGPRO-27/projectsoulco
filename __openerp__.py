# -*- coding: utf-8 -*-
{
    'name': "Projet Soulco",

    'summary': """Design Odoo for Soulco Client""",

    'description': """
        Project erp-Soulco
    """,

    'author': "IGPRO",
    'website': "http://igpro-online.com",

    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','stock'],

    # always loaded
    'data': [
        'project_soulco_view.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
