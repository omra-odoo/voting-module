# -- coding: utf-8 --

from odoo import fields , models

class candidates(models.Model):
    _name = "candidate.model"
    _description = "this is for candidate model"

    name=fields.Char('Candidate Name:')
    area=fields.Text('Area')
    dateofbirth=fields.Date('Date Of Birth')
    gender=fields.Selection(string="Gender",
        selection=[('male', 'Male'), ('female', 'Female'),('other','Other')])
    parties=fields.Selection(string="Select Your Party",
        selection=[('bjp', 'Bjp'), ('congress', 'Congress'),('aap','AAP')])
    aadharno=fields.Char('Aadharcard Number')
