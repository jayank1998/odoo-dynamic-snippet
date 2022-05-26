{
    'name': "Bitcoin Track",
    'summary': """Bitcoin""",
    'category': 'Uncategorized',
    'version': '14.0.0.1',
    'depends': ['base', 'web', 'website'],
    'data': [
        'views/btc_report.xml',
        'views/assets.xml',
        'menu/menu_file.xml',
    ],
    'qweb': ['static/src/xml/bitcoin_report.xml', ],
    'installable': True,
    'auto_install': False,
}
