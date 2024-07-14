
{
    'name': 'Login as Guest',
    'version': '17.0.0.0.0',
    'category': 'Extra Tools',
    'summary': 'Users can login as guest',
    'description': '',
    'author': 'Solvex',
    'company': 'Solvex',
    'maintainer': 'Solvex',
    'website': 'https://solvex.top',
    'data': [
            'security/ir.model.access.csv',
            'data/data.xml',
            'views/login_templates.xml',
            'views/configuration_login.xml',
    ],
    "depends": ["web"],

    'assets': {
        'web.assets_frontend': [
            'user_login_guest/static/src/js/login.js',
            'user_login_guest/static/src/css/login.css',
           ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
