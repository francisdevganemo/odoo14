from odoo import models, fields


class DateReservation(models.Model):
    _name = 'date.reservation'
    specialty = fields.Many2one('res.partner', String="Especialidad", required=True) #fields.Char('Especialidad',required=True)
    specialist = fields.Many2one('res.partner', String="Especialista")
    dni = fields.Char("DNI", required=True)
    address = fields.Char('Direccion')
    phone = fields.Char('Numero de celular')
    datetime = fields.Datetime('Fecha de la cita')
    today = fields.Datetime('Fecha de hoy', default=fields.Datetime.now, readonly=True)
    city = fields.Char('Ciudad')  # fields.Many2one('ubigeo','Ciudad')
    attention_mode = fields.Selection(
        [('virtual', 'Remota'),
         ('onsite', 'Presencial')],
        'Modo de atencion')


class DateReservationSpecialty(models.Model):
    _name = 'date.reservation.specialty'
    description = fields.Char('Especialidad')


class DateReservationSpecialist(models.Model):
    _name = 'date.reservation.specialist'
    name = fields.Char('Nombre', required = True)
    dni = fields.Char('dni', required=True)
    specialty = fields.Many2many('res.partner',string="Especialidad", required=True)
    phone = fields.Char('numero', required=True)
    age = fields.Char('Edad', required=True)
    city = fields.Char('Ciudad', required=True)
    address = fields.Char('Direccion')




