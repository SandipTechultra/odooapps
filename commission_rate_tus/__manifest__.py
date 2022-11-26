# -*- coding: utf-8 -*-
{
    'name': 'Commission Rate',
    'category': 'sale',
    'summary': 'Commission Rate',
    'version': '15.0.0',
    'author': "TechUltra Solutions",
    'website': "https://www.techultrasolutions.com/",
    'description': """ Sale Commission Rate on Sale order line and invoice line and sale order report and invoice report.""",
    'icon': '/commission_rate_tus/static/description/logo.png',
    'images': ['static/description/logo.png'],
    'depends': ['sale_management', 'account'],
    'data': [
        'views/res_partner_view.xml',
        'views/sale_order_line_view.xml',
        'views/account_move_view.xml',
        'report/sale_report_templates.xml',
        'report/report_invoice.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'OPL-1',
}
