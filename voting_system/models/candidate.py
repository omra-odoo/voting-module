# -- coding: utf-8 --

from odoo import fields , models,api
from odoo.exceptions import UserError, ValidationError
import dateutil
import datetime

class candidates(models.Model):
    _name = "candidate.model"
    _description = "this is for candidate model"

    name=fields.Char('Candidate Name:')
    area_candidate_id = fields.Many2one("area.model", string="Select Area")
    dateofbirth=fields.Date('Date Of Birth')
    gender=fields.Selection(string="Gender",
        selection=[('male', 'Male'), ('female', 'Female'),('other','Other')])
    party_id=fields.Many2one("voting.party.model", string="Select Party")
    aadharno=fields.Char('Aadharcard Number')
    phoneno=fields.Integer('Phone Number')
    result_ids= fields.One2many('voter.model', 'candidate_id')
    vote_count= fields.Integer("Total Votes",compute="_count_votes")

    def _count_votes(self):
        for rec in self:
            rec.vote_count = len(rec.result_ids)
        # print (rec.vote_count)



    @api.constrains('aadharno')
    def _check_valid_aadharno(self):
        # length = len(self.adharno)
        for record in self:
            s = len(record.aadharno)
            if  s != 12:
                raise ValidationError(("your adhar number is not valid"))



    @api.constrains('dateofbirth')
    def _compute_age(self):
     # Get the current date
        now = datetime.datetime.utcnow()
        now = now.date()

    # Get the difference between the current date and the birthday
    
        age1 = dateutil.relativedelta.relativedelta(now, self.dateofbirth)
        age1 = age1.years
        if age1 <= 21 :
            raise ValidationError(("You are not eligible for Registration of candidate"))