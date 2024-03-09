from odoo import models, fields

class compania_cinematografica(models.Model):
    #_name = 'res.partner' --no hace falta
    _inherit = 'res.partner'
    premiada = fields.Boolean(default=False)
    is_cine=fields.Boolean()

class videoclub_categorias(models.Model):
    #Atributos
    _name= "videoclub.categorias"
    _description= "Categoria de Peliculas"
    _rec_name = 'nombre'
    #Campos
    nombre= fields.Char('Nombre', size=30, required=True, help='Nombre de la peli')
    descripcion= fields.Text('Descripcion')

class videoclubdario_pelis(models.Model):
#atributos
    _name = 'videoclubdario.peli'
    _description = 'Película'
    _rec_name = 'titulo'
    #campos
    titulo = fields.Char('Titulo', size=30, required=True, help='Nombre de la peli')
    director = fields.Char('Director', size=30, required=False, help='Director de la peli', default='')
    clasificacion = fields.Selection([('TP','Todos los Públicos'),('men12','Menores de 12 años'),('may18','Mayores 18 años')], string='Clasificación', default='TP')
    presupuesto = fields.Integer()
    fechaestreno = fields.Date()
    imagen = fields.Binary(string='Imagen')
    categoria = fields.Many2one('videoclub.categorias', string='Categoría')
    subvencionado = fields.Float(compute='_valor_subvencion', store=True)
    invertido = fields.Float(compute='_valor_inversion', store=True)
    millonario = fields.Boolean(string='Millonario', compute='_compute_millonario', readonly=True)
    compania = fields.Many2one('res.partner')