from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale Order'

    total_commission = fields.Float(string="Commission", compute='_compute_commission')

    @api.depends('order_line', 'partner_id')
    def _compute_commission(self):
        tot_commission = 0
        for rec in self.order_line:
            commission = (rec.price_unit * rec.order_partner_id.commission) / 100
            commission = commission * rec.product_uom_qty
            tot_commission += commission
        self.total_commission = tot_commission


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    _description = 'Sale Order Line'

    commission = fields.Float(string="Commission (%)", required=False, )
    commission_cal = fields.Float(string="Commission", required=False, )

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id', 'order_partner_id')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty,
                                            product=line.product_id, partner=line.order_id.partner_shipping_id)
            commission = 0
            if line.order_partner_id.is_commission:
                commission = (line.price_unit * line.order_partner_id.commission) / 100
                commission = commission * line.product_uom_qty
            line.update({
                'price_tax': taxes['total_included'] - taxes['total_excluded'],
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'] + commission,
                'commission': line.order_partner_id.commission,
                'commission_cal': commission,
            })
            if self.env.context.get('import_file', False) and not self.env.user.user_has_groups(
                    'account.group_account_manager'):
                line.tax_id.invalidate_cache(['invoice_repartition_line_ids'], [line.tax_id.id])
