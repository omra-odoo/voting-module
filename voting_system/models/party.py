from odoo import fields,models

class party(models.Model):
    _name = 'voting.party.model'
    _description = "this is for voting party model"

    name=fields.Char('Party Name:')
    leadearname = fields.Char('Parties Leader Name:')
    members=fields.Integer('Total Membbers:')
    image = fields.Binary("Party Logo:", attachment=True, store=True,
                                help="This field holds the image used for as party icon")
