# -*- coding: utf-8 -*-
{
    'name': "my_library",
    'summary': """Modulo de prueba para iniciar en Odoo 14""",
    'description': """
        Este modulo esta hecho para iniciar en el desarrollo de modulos en Odoo 14
    """,
    'author': "Francis",
    'website': "http://www.google.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/library_book.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

}
