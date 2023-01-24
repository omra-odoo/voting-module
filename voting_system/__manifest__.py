# -- coding: utf-8 --
{
    'name':'voting_system',
    'author':'om rabara',
    'data':[
        'security/ir.model.access.csv',
        'views/voter_view.xml',
        'views/voting_menu.xml',
        'views/candidate_view.xml',
        'views/party_view.xml',
        # 'views/result_view.xml',
        
    ],
    'depends': ['mail','base'],
    'demo':[
        'demo/voter_demo_data.xml',
    ],
    'application':True,
    'installable':True,
}