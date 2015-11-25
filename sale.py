# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Id, If, Eval, Bool

__all__ = ['Sale']


class Sale:
    __name__ = 'sale.sale'
    __metaclass__ = PoolMeta
    suggested_quotations = fields.Function(fields.Char(
            'Suggested Quotations'), 'on_change_with_suggested_quotations')

    @fields.depends('party')
    def on_change_with_suggested_quotations(self, name=None):
        res = self.search([
                ('party', '=', self.party),
                ('state', '=', 'quotation'),
                ('id', '!=', self.id),
                ])
        return ', '.join([x.rec_name for x in res])
