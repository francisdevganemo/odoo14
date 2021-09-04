from odoo import models, fields


class DateReservation(models.Model):
    _name = 'date.reservation'
    specialty = fields.Many2one('res.partner', String="Especialidad", required=True) #fields.Char('Especialidad',required=True)
    specialist = fields.Many2one('res.partner', String="Especialista")
    dni = fields.Many2one('res.partner', String="DNI", required=True)
    address = fields.Char('Direccion')
    phone = fields.Char('Numero de celular')
    datetime = fields.Datetime('Fecha de la cita')
    today = fields.Datetime('Fecha de hoy',default=fields.Datetime.now, )
    city = fields.Char('Ciudad')  # fields.Many2one('ubigeo','Ciudad')
    attention_mode = fields.Selection(
        [('virtual', 'Remota'),
         ('onsite', 'Presencial')],
        'Modo de atencion')
