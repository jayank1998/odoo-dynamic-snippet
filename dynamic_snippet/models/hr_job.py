from odoo import models, fields


class HrJob(models.Model):
    _inherit = 'hr.job'

    image_1920 = fields.Image('Image', attachment=True)
