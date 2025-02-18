# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Consulta(models.Model):
    _name = 'dmr_veterinario.consulta'
    _description = 'Consulta'

    motivo = fields.Char('Motivo')
    fecha = fields.Date('Fecha')
    diagnostico = fields.Char('Diagnostico')
    tratamiento = fields.Char('Tratamiento')
    precio = fields.Float('Precio')
    estado = fields.Selection([
        ('0', 'Pendiente'),
        ('0', 'Realizada'),
        ('0', 'Cancelada'),
    ], string='Estado')
    propietario_id = fields.Many2one('dmr_veterinario.propietario', string='Propietario')
    paciente_id = fields.Many2one('dmr_veterinario.paciente', string='Paciente')

    @api.onchange('paciente_id')
    def _onchange_paciente_id(self):
        if self.paciente_id:
            self.propietario_id = self.paciente_id.propietario_id
        else:
            self.propietario_id = false