"""
    Import Packages, Class
"""
from odoo.http import request
from odoo import api, models


class IrHttp(models.AbstractModel):
    """
        Inherit ir.http class
    """
    _inherit = 'ir.http'

    def session_info(self):
        """
            This method to use odoo session information prepare.
        """
        result = super(IrHttp, self).session_info()
        result['is_access_key'] = False
        if request.env.user.has_group('tus_remove_hotkey.group_user_access'):
            result['is_access_key'] = True
        return result
