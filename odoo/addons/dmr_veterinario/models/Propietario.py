# -*- coding: utf-8 -*-

# Este es el modelo de propietario con sus respectivas propiedades

from odoo import models, fields, api
class Propietario(models.Model):
    _name = 'dmr_veterinario.propietario'
    _description = 'Propietario'

    name = fields.Char('Nombre', required=True)
    dni = fields.Char('DNI')
    telefono = fields.Integer('Telefono')
    correo = fields.Char('Correo')
    direccion = fields.Char('Direccion')
    paciente_ids = fields.One2many('dmr_veterinario.paciente', 'propietario_id', string='Pacientes asociados')