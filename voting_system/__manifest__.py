# -- coding: utf-8 --
{
    'name':'voting_system',
    'category': 'Voting System/election',
    'author':'om rabara',
    'data':[
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/voter_view.xml',
        'views/voting_menu.xml',
        'views/candidate_view.xml',
        'views/party_view.xml',
        'views/area_view.xml',
        'report/voter_model_report.xml',
        'report/voter_model_templates.xml',
        
    ],
    'depends': ['mail','base'],
    'demo':[
        'demo/voter_demo_data.xml',
    ],
    'application':True,
    'installable':True,
}