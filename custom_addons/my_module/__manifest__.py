{
    'name': 'My Custom Module',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Custom module for managing products',
    'description': 'This module adds a new menu item and form view to manage products.',
    'author': 'Your Name',
    'depends': ['base', 'product'],
    'data': [
        'views/product_view.xml',
    ],
    'installable': True,
}
