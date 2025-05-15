from odoo import models, fields, _
from datetime import datetime, date, timedelta
from odoo.exceptions import UserError,ValidationError
class ApprovalRequest(models.Model):
    _inherit = "approval.request"

    type_request = fields.Selection([
        ('reserve', 'Reserve for sirin'),
        ('project', 'Use in Project')
    ], string="Request type", tracking=True)
    date_request = fields.Datetime(string="Request Date", default=fields.Datetime.now)
    dis_request = fields.Text(string="Request Description")
    project_id = fields.Many2one(
        'project.project',
        string="Select Project",
    )
