# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Doctor(models.Model):
    _name = 'dmr_veterinario.doctor'
    _description = 'Doctor'

    name = fields.Char('Nombre', required=True)
    especialidad = fields.Char('Especialidad')