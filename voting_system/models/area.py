
from odoo import fields,models

class area(models.Model):
    _name = 'area.model'
    _description = "this is for voting area model"

    name= fields.Char('Area name')