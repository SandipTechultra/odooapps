# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_commission = fields.Boolean(string="Is Commission")
    commission = fields.Float(string="Commission", required=False, )
