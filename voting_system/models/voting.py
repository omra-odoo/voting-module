# -- coding: utf-8 --

import datetime
from odoo import fields , models,api
from odoo.exceptions import UserError, ValidationError
import dateutil

class votingSystem(models.Model):
    _name="voter.model"
    _description="voting model"
    _inherit = ["mail.thread","mail.activity.mixin"]


    name=fields.Char('Name', required=True)
    address=fields.Text('Address')
    adharno=fields.Char('Adharcard Number',required=True)
    voterid=fields.Boolean('Voterid Card')
    pancard=fields.Boolean('PAN Card')
    date=fields.Datetime('Date',default=lambda self: fields.Datetime.now(),readonly=True)
    gender=fields.Selection(string="Gender",
        selection=[('male', 'Male'), ('female', 'Female'),('other','Other')])
    candidate_id=fields.Many2one("candidate.model",string="Select Candidate",required=True)
    parties_id=fields.Many2one("voting.party.model", string="Select Party", related='candidate_id.party_id', required=True)
    dateofbirth=fields.Date('Date Of Birth',required = True)
    state = fields.Selection(selection= [('new','New'),('done','Done')],default="new",tracking=True)

    _sql_constraints = [
        ("check_adharno", "UNIQUE(adharno)", "The adharno is unvalid"), 
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]
    # def _compute_length_adharno(self):
    #     for record in self:
    #         record.adharlencount = len(record.adharno)

    # @api.depends('adharno')
    # def _compute_valid_adharno(self):
    #     for record in self:
    #         s = len(record.adharno)
    #         if  s != 16:
    #             raise ValidationError(("your adhar number is not valid"))

    @api.constrains('adharno')
    def _check_valid_adharno(self):
        # length = len(self.adharno)
        for record in self:
            s = len(record.adharno)
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
        if age1 <= 18 :
            raise ValidationError(("You are not eligible for voting"))

    def submit_action(self):
        for record in self:
            if record.state=='new':
                record.state='done'
            