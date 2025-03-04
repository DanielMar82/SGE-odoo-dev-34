# -*- coding: utf-8 -*-
{
    'name': "dmr_veterinario",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
    Este es un módulo gestor de veterinario donde podremos gestionar a los pacientes (Los animales), los propietarios (Los dueños), los doctores y las consultas.
    Pudiendo crear, borrar y cambiar los distintos datos que se guarden en el veterinario.
    """,

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'author': "Daniel Martín Ruiz",
    'website': "https://www.Veterinario.com",
    'icon': 'dmr_veterinario/static/description/IconModulo.png',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Applications',
    'version': '0.1',

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
        'reports/report_paciente.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

