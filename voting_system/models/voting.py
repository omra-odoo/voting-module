# -- coding: utf-8 --

from odoo import fields , models

class votingSystem(models.Model):
    _name="voter.model"
    _description="voting model"

    name=fields.Char('Name', required=True)
    age=fields.Integer('Age', required=True)
    address=fields.Text('Address')
    adharno=fields.Char('Adharcard Number',required=True)
    voterid=fields.Boolean('Voterid Card')
    pancard=fields.Boolean('PAN Card')
    date=fields.Datetime('Date',default=lambda self: fields.Datetime.now(),readonly=True)
    gender=fields.Selection(string="Gender",
        selection=[('male', 'Male'), ('female', 'Female'),('other','Other')])
    candidate=fields.Selection(string="Select Candidate",
        selection=[('narendramodi', 'Narendra modi'), ('rahulgandhi', 'Rahul Gandhi'),('arvindkejriwal','Arvind Kejriwal')])
    parties=fields.Selection(string="Select Party Name",
        selection=[('bjp', 'Bjp'), ('congress', 'Congress'),('aap','AAP')])
