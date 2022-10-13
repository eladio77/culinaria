{ 
    'name': 'Custom_culinaria',
    'summary': "Personalizaciones generales de Odoo Culinaria",
    'description':
        """Personalizaciones Varias del Cliente
            ===============
        Se agrega campo de nombre fantasia a contactos
        """,
    'author': "Eladio Garcia",
    'website': "http://eladiogarcia.com",
    'category': "sin categoría",
    'version': '1.1',
    'depends': ['base'],
    'data': [
        'views/as_res_partner_view.xml',
    ],
    'license': 'LGPL-3',
    }