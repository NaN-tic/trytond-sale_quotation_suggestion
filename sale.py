# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Sale']


class Sale:
    __name__ = 'sale.sale'
    __metaclass__ = PoolMeta
    suggested_quotations = fields.Function(fields.Char(
            'Suggested Quotations'), 'on_change_with_suggested_quotations')
    suggested_for = fields.Many2Many

    @fields.depends('party')
    def on_change_with_suggested_quotations(self, name=None):
        res = self.search([
                ('party', '=', self.party),
                ('state', '=', 'quotation'),
                ('id', '!=', self.id),
                ])
        return ', '.join([x.rec_name for x in res])
