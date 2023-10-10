  {
    'name': 'School Management',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Custom module for managing schools',
    'description': 'This module adds a new menu item and form view to manage products.',
    'author': 'Uzueta',
    'depends': ['base', 'contacts', 'hr', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/school.xml',
    ],
    'demo:':[],

    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
