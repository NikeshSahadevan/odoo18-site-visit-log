{
    'name': 'Site Visit Log',
    'version': '18.0.1.0.0',
    'summary': 'Track customer site visits and field logs',
    'description': """
        Manage and log customer site visits, visit dates, purposes, and status updates.
    """,
    'category': 'Sales/CRM',
    'author': 'Nikesh',
    'depends': ['base', 'contacts', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/site_visit_security.xml',
        'data/sequence_data.xml',
        'reports/site_visit_report.xml',
        'views/site_visit_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}