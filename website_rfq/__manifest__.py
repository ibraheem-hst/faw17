{
    'name': 'Website RFQ',
    'version': '17.0.1.0.0',
    'category': 'Website/Website',
    'summary': 'Website RFQ',
    'author': 'DevMRM.com',
    'depends': ['website_sale', 'approvals'],
    'data': [
        'data/data.xml',

        'views/templates.xml',
        'views/approval_request.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}