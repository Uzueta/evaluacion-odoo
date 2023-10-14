{
    'name': "Auditorias",
    'depends': ['base', 'sale'],
    'data': [
        'views/pao_auditorias_views.xml',
        'views/sale_cotizaciones_view.xml',
        'views/sale_menu_view.xml',

        'report/sale_report_auditorias.xml',
        
        'security/ir.model.access.csv',
    ],
}