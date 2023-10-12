{
    'name': "Estate",
    'depends': ['base'],
    'data': [
        'views/estate_property_tag_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_views.xml',

        'views/estate_menus.xml',
        
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}