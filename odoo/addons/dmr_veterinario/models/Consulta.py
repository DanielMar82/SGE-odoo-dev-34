# -*- coding: utf-8 -*-

# Este es el modelo de consulta con sus respectivas propiedades

from odoo import models, fields, api
class Consulta(models.Model):
    _name = 'dmr_veterinario.consulta'
    _description = 'Consulta'

    name = fields.Char('Nombre', required=True)
    motivo = fields.Char('Motivo')
    fecha = fields.Date('Fecha')
    estado = fields.Selection([
        ('0', 'Pendiente'),
        ('1', 'Realizada'),
        ('2', 'Cancelada'),
    ], string='Estado')
    diagnostico = fields.Char('Diagnostico')
    tratamiento = fields.Char('Tratamiento')
    precio = fields.Float('Precio')
    paciente_id = fields.Many2one('dmr_veterinario.paciente', string='Paciente')
    doctor_ids = fields.Many2many('dmr_veterinario.doctor', 'consulta_doctor_rel', 'consulta_id', 'doctor_id', string='Doctores asociados')


    # Esta es una función la cual hace que cuando se rellene una consulta con un paciente se ponga automaticamente el propietario de ese paciente
    @api.depends('paciente_id')
    def _compute_propietario(self):
        for record in self:
            record.propietario_id = record.paciente_id.propietario_id if record.paciente_id else False

    propietario_id = fields.Many2one('dmr_veterinario.propietario', string='Propietario', compute="_compute_propietario", store=True, readonly=True)
    