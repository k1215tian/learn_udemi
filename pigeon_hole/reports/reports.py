from odoo import fields, models, api


class ModelName(models.TransactionalModel):
    _name = 'ProjectName.TableName'
    _description = 'Description'

    name = fields.Char()
