# -*- coding: utf-8 -*-
"""
    import fields and models
"""
from odoo import fields, models


class ActiveMenu(models.Model):
    """
    it's for Active Menu
    """
    _name = "active.menu"
    _description = "Active Menu"

    menu_line_ids = fields.One2many('menu.line', 'menu_id', string='Order Lines')
    name = fields.Char(default="Hide Menu List", string="Name")
