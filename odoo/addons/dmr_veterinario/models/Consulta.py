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
        ('1', 'Realizada'),
        ('2', 'Cancelada'),
    ], string='Estado')
    paciente_id = fields.Many2one('dmr_veterinario.paciente', string='Paciente')


    #Esto hace que al poner el paciente automaticamente se pone el propietario relacionado a este
    @api.depends('paciente_id')
    def _compute_propietario(self):
        for record in self:
            record.propietario_id = record.paciente_id.propietario_id if record.paciente_id else False

    propietario_id = fields.Many2one('dmr_veterinario.propietario', string='Propietario', compute="_compute_propietario", store=True, readonly=True)
    