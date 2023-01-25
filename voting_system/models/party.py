
from odoo import fields,models, api

class party(models.Model):
    _name = 'voting.party.model'
    _description = "this is for voting party model"

    name=fields.Char('Party Name:')
    leadearname = fields.Char('Parties Leader Name:')
    members=fields.Integer('Total Membbers:' ,compute="_count_members" )
    image_small = fields.Binary("Party Logo:", attachment=True, store=True)

    candidate_id = fields.One2many('candidate.model', 'party_id')


    # @api.depends('')
    def _count_members(self):
        for rec in self:
            rec.members = len(rec.candidate_id)

   

