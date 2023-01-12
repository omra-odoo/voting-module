from odoo import fields,models

class party(models.Model):
    _name = 'voting.party.model'
    _description = "this is for voting party model"

    name=fields.Char('Party Name:')
    leadearname = fields.Char('Parties Leader Name:')
    members=fields.Integer('Total Membbers:')
