# -*- coding: utf-8 -*-
{
    'name': "ModuloDario",

    'summary': """
        Este es el resumen en el cual tenemos que escribir algo para rellenar este apartado
        """,

    'description': """
        Este es el modulo de Dario para hacer la actividad
    """,

    'author': "Dario Molina Valdés",
    'website': "https://www.ieshlanz.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
