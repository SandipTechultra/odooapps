{
    'name': 'Hide Report Menu',
    'version': '15.0.1',
    'summary': 'Dynamic hide menu item',
    'sequence': 1,
    'author': "Success ERP",
    'description': """ Dynamic hide menu item """,
    'category': 'configuration',
    'depends': ['base'],
    'icon': '/hide_menu/static/description/hide_logo.png',
    'images': ['static/description/hide_logo.png'],
    'data': ['security/ir.model.access.csv',
             'views/active_menu.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
