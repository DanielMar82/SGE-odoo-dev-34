# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Catgoria(models.Model):
    _name = 'sge_libreria.categoria'
    _description = 'Categoria'

    name = fields.Char('Nombre', required=True, help="Introduzca nombre de categoria")
    description = fields.Char('Descripcion')
    
