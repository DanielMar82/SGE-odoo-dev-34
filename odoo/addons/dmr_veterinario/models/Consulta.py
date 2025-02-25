# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Consulta(models.Model):
    _name = 'dmr_veterinario.consulta'
    _description = 'Consulta'

    name = fields.Char('Nombre')
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


    #Esto hace que al poner el paciente automaticamente se pone el propietario relacionado a este
    @api.depends('paciente_id')
    def _compute_propietario(self):
        for record in self:
            record.propietario_id = record.paciente_id.propietario_id if record.paciente_id else False

    propietario_id = fields.Many2one('dmr_veterinario.propietario', string='Propietario', compute="_compute_propietario", store=True, readonly=True)

    @api.depends('estado')
    def _compute_readonly_fields(self):
        for record in self:
            readonly = record.estado != '1'
            record.diagnostico = False
            record.tratamiento = False
            record.precio = False


#ESTO NO FUNCIONA TODAVIA
    # @api.constrains('diagnostico', 'tratamiento', 'precio')
    # def _check_fields(self):
    #     for record in self:
    #         if record.estado != '1' and (record.diagnostico or record.tratamiento or record.precio):
    #             raise ValidationError("Los campos Diagnóstico, Tratamiento y Precio solo pueden ser llenados si el estado es 'Realizada'.")

    