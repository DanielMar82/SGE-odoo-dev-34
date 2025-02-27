# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Paciente(models.Model):
    _name = 'dmr_veterinario.paciente'
    _description = 'Paciente'

    name = fields.Char('Nombre', required=True)
    fecha_nacimiento = fields.Date('Fecha_nacimiento')
    sexo = fields.Selection([
        ('0', 'Hembra'),
        ('1', 'Macho'),
        ('2', 'Neutro'),
    ], string='Sexo')
    tipo = fields.Selection([
        ('0', 'Domestico'),
        ('1', 'Exotico'),
        ('2', 'Granja'),
        ('3', 'Acuatico'),
        ('4', 'Otro'),
    ], string='Tipo')
    especie = fields.Char('Especie')
    raza = fields.Char('Raza')
    peso = fields.Float('Peso')
    imagen = fields.Binary('Imagen')
    propietario_id = fields.Many2one('dmr_veterinario.propietario', string='Propietario')
