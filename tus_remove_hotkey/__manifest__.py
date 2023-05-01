# -*- coding: utf-8 -*-
{
    'name': "HotKey Remove",
    'summary': "Remove shortcut key",
    'author': "TechUltra Solutions",
    'website': "www.techultrasolutions.com",
    'category': 'Hidden',
    'version': '16.0.1',
    "price": 20,
    "currency": "USD",
    'description': """
        Remove a hotkey by a specific user.
        **************************************************************************************************************
        List of Odoo Shortcut Keys
        
        Odoo Record Edit	Alt + ‘A’	Ctrl + Alt + ‘A’
        Odoo Previous Breadcrumb	Alt + ‘B’	Ctrl + Alt + ‘B’
        Odoo Record Create	Alt + ‘C’	Ctrl + Alt + ‘C’
        chrome does not support ‘D’ access key –> go to address bar	Alt + ‘D’	Ctrl + Alt + ‘D’
        chrome does not support ‘E’ access key –> go to address bar to search google	Alt + ‘E’	Ctrl + Alt + ‘E’
        chrome does not support ‘F’ access key –> go to menu	Alt + ‘F’	Ctrl + Alt + ‘F’
        Vacant for Odoo other operation like in sale order task button, Go to website	Alt + ‘G’	Ctrl + Alt + ‘G’
        Odoo Home Page	Alt + ‘H’	Ctrl + Alt + ‘H’
        Odoo Discard Button	Alt + ‘J’	Ctrl + Alt + ‘J’
        Odoo Kanban View	Alt + ‘K’	Ctrl + Alt + ‘K’
        Odoo List View	Alt + ‘L’	Ctrl + Alt + ‘L’
        Odoo pager Next	Alt + ‘N’	Ctrl + Alt + ‘N’
        Odoo pager Previous	Alt + ‘P’	Ctrl + Alt + ‘P’
        Odoo Search	Alt + ‘Q’	Ctrl + Alt + ‘Q’
        Odoo Save Record	Alt + ‘S’	Ctrl + Alt + ‘S’
        Odoo Menus	Alt + {1-9}	Ctrl + Alt + {1-9}
        ****************************************************************************************************************
    """,
    'depends': ['base', 'web'],
    'data': [
        'data/assets.xml'
    ],
    'assets': {
            'web.assets_backend': ['tus_remove_hotkey/static/src/js/remove_hotkey.js'],
    },
    'license': 'LGPL-3',
    'application': False,
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
}
