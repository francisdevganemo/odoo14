from odoo import models, fields
class LibraryBook(models.Model):
    _name = 'library.book'
    name = fields.Char('Title', required=True)
    description = fields.Html('Description')
    city = fields.Text('City')
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')
    pages = fields.Integer('Number of Pages')
    state = fields.Selection(
        [('draft','Not Available'),
          ('available', 'Available'),
          ('lost', 'Lost')],
        'State')