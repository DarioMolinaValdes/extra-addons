# -*- coding: utf-8 -*-
{
    'name': "videoclubDario",

    'summary': """   
    Bienvenido a Videoclub_Dario, tu destino cinematográfico ideal. Sumérgete en un mundo de 
    emocionantes historias y grandes éxitos cinematográficos. Desde clásicos atemporales hasta los 
    últimos lanzamientos, en Videoclub_Dario encontrarás la mejor selección para satisfacer todos tus gustos. 
    Descubre la magia del cine con nosotros y disfruta de una experiencia única en cada película. 
    ¡Videoclub_Dario, donde la diversión y el entretenimiento se encuentran en cada alquiler!
       """,

    'description': """
        Videoclub_Dario es tu refugio cinematográfico, ofreciendo una amplia 
        gama de películas desde clásicos atemporales hasta los últimos éxitos. 
        Con un catálogo diverso y servicio excepcional, estamos aquí para hacer 
        que cada noche sea una experiencia inolvidable.
        "Vive la magia del cine en cada alquiler. Videoclub_Dario, donde cada película es una nueva aventura."
    """,

    'author': "Dario Molina Valdes",
    "license": "AGPL-3",
    'website': "https://www.youtube.com/watch?v=9bZkp7q19f0",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/videoclubdario_security.xml',
        'security/ir.model.access.csv',
        'views/videoclubdario.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'application':True,
}
