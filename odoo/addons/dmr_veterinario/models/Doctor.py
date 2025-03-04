# -*- coding: utf-8 -*-

# Este es el modelo de doctor con sus respectivas propiedades

from odoo import models, fields, api
class Doctor(models.Model):
    _name = 'dmr_veterinario.doctor'
    _description = 'Doctor'

    name = fields.Char('Nombre', required=True)
    dni = fields.Char('DNI')
    telefono = fields.Integer('Telefono')
    correo = fields.Char('Correo')
    especialidad = fields.Selection([
        ('0', 'Domestico'),
        ('1', 'Exotico'),
        ('2', 'Granja'),
        ('3', 'Acuatico'),
        ('4', 'Otro'),
    ], string='Especialidad')
    consulta_ids = fields.Many2many('dmr_veterinario.consulta', 'consulta_doctor_rel', 'doctor_id', 'consulta_id', string='Consultas asociadas')