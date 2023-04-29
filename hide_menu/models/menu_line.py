# -*- coding: utf-8 -*-
"""
    import api, fields and models
"""
from odoo import api, fields, models


class Menuline(models.Model):
    """
    it's for menu line
    """
    _name = "menu.line"
    _description = "Active Menu Line"

    model_id = fields.Many2one('ir.model', string='Model ID')
    menu_id = fields.Many2one('active.menu', string='Menu ID')
    report_id = fields.Many2one('ir.actions.report', string='Report ID')
    is_active = fields.Boolean(string="Is Active")

    @api.onchange('model_id')
    def onchange_model_id(self):
        """This onchange for if we click on the model_id. model_id shows the models and base on model
        show the reports"""
        return {'domain': {
            'report_id': [
                ('id', 'in', self.env['ir.actions.report'].search([('model', '=', self.model_id.model)]).ids)]}}

    def active_menu(self):
        """ This method for the Active button. it's called on active model, it's a print menu.it shows the reports."""
        if self.report_id:
            self.report_id.create_action()
            self.is_active = False

    def deactive_menu(self):
        """This method for the Deactive button. click on print menu. it hide the reports."""
        if self.report_id:
            self.report_id.unlink_action()
            self.is_active = True
