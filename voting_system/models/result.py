import resource
from odoo import fields,models

class party(models.Model):
    _name = 'voting.result.model'
    _description = "this is for voting party model"

    result =fields.One2many("voter.model","candidate_id",store=True)
