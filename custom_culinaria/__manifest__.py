{ 
    'name': 'Custom_culinaria',
    'summary': "Personalizaciones generales de Odoo Culinaria",
#    'description': """
#    Personalizaciones Varias del Cliente
#            ===============
#        Se agrega campo de nombre fantasia a contactos
#        """,
    'author': "Eladio Garcia",
    'website': "http://www.ti-eg.com",
    'license': 'LGPL-3',
    'category': "extra",
    'version': '1.1',
    'depends': ['base','sale_management','purchase','stock','contacts',],
    'data': [
        'views/as_res_partner_view.xml',
        'views/as_product_view.xml',
        'views/as_sale_order_view.xml',
    ],
    'auto-install': 'False',
    'installable': 'True',
}