from odoo import models, fields, api

class Gastos(models.Model):
    _name = 'gastos'
    _description = 'gastos'

    descripcion = fields.Char('Descripcion', required=True)
    fecha_gasto = fields.Date(string='Fecha del Gasto', required=True)
    categoria_id = fields.Many2one(comodel_name='categoria', string='Categoría', required=True)
    gasto = fields.Monetary(string='Gasto', currency_field='currency_id', required=True)
    gasto_total = fields.Monetary('Gasto Total', compute='_compute_total_gastos', currency_field='currency_id', store=True)

    currency_id = fields.Many2one('res.currency', string='Moneda')

    @api.depends('gasto')
    def _compute_total_gastos(self):
        for record in self:
            record.gasto_total = sum(record.gasto for record in self)
    
    def name_get(self):
        result = []
        for record in self:
            name = record.descripcion or 'Sin descripción'
            result.append((record.id, name))
        return result

class Categoria(models.Model):
    _name = 'categoria'
    _description = 'categoria'

    name = fields.Char(string='Nombre de la Categoria', required=True)
    
    
    
    
    