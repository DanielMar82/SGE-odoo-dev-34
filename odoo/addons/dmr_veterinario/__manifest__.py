# -*- coding: utf-8 -*-
{
    'name': "dmr_veterinario",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'author': "Daniel Martín Ruiz",
    'website': "https://www.yourcompany.com",
    'icon': 'dmr_veterinario/static/description/IconModulo.png',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Applications',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/paciente.xml',
        'views/propietario.xml',
        'views/consulta.xml',
        'views/doctor.xml',
        'views/menus.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

