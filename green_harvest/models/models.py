from odoo import models, fields

class GreenHarvestService(models.Model):
    _name = 'greenharvest.service'
    _description = 'Servicio'
    _rec_name = 'name'

    name = fields.Char('Nombre', required=True, help='Nombre del servicio')
    description = fields.Text('Descripción', help='Descripción del servicio')
    category = fields.Many2one('greenharvest.service.category', string='Categoría', help='Categoría del servicio')
    price = fields.Float('Precio', digits=(10, 2), help='Precio del servicio')
    duration = fields.Float('Duración', help='Duración del servicio en horas')
