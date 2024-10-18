{
    'name': 'Custom Invoice Report',
    'version': '17.0.1.0',
    'category': 'Accounting',
    'summary': 'Customized invoice report',
    'description': """
        This module provides a customized invoice report template.
    """,
    'depends': ['account'],
    'data': [
        'report/custom_invoice_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}