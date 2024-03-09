# -*- coding: utf-8 -*-
{
    'name': "GreenHarvest",

    'summary': """   
    Bienvenido a GreenHarvestERP, tu solución integral para la gestión agrícola y la venta de productos orgánicos. 
    Optimiza tus operaciones y promueve prácticas agrícolas sostenibles con nuestra plataforma. 
    Desde la producción hasta la comercialización, GreenHarvestERP te ofrece todas las herramientas que necesitas para 
    cultivar con responsabilidad y llevar tus productos al mercado con éxito.
       """,


    'description': """
         GreenHarvestERP es la solución definitiva para la gestión eficiente de tu empresa agrícola. 
        Desde el control de inventario hasta la contabilidad, nuestro ERP está diseñado para satisfacer 
        todas las necesidades de tu negocio. Descubre una nueva forma de cultivar y vender productos orgánicos 
        con GreenHarvestERP.
    """,

    'author': "Dario Molina Valdes",
    'website': "https://www.youtube.com/watch?v=5yCsjASSd1M",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
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
