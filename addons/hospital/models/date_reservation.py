from odoo import models, fields, api


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

    @api.onchange('datetime')
    def _onchange_datetime(self):
        for record in self:
            if record.datetime:
                if record.datetime < record.today:
                    record.datetime = record.today

class DateReservationSpecialty(models.Model):
    _name = 'date.reservation.specialty'
    description = fields.Char('Especialidad')


class DateReservationSpecialist(models.Model):
    _name = 'date.reservation.specialist'
    name = fields.Char('Nombre', required = True)
    dni = fields.Char('dni', required=True)
    specialty = fields.Many2many('res.company',string="Especialidad", required=True)
    phone = fields.Char('numero', required=True)
    age = fields.Integer('Edad', required=True)
    city = fields.Char('Ciudad', required=True)
    address = fields.Char('Direccion')
    district = fields.Char('Distrito')
    province = fields.Char('Provincia')
    department = fields.Char('Departamento')

    # @api.onchange('specialty')
    # def _onchange_specialty(self):
    #     for record in self:
    #         if record.specialty:
    #             record.address = record.company_id.street










