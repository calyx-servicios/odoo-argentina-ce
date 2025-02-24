##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import fields, models, api, _


class AfipResponsabilityType(models.Model):

    _inherit = "l10n_ar.afip.responsibility.type"

    iva_condition_receptor = fields.Selection(
        [
            ("1", "IVA Responsable Inscripto"),
            ("6", "Responsable Monotributo"),
            ("13", "Monotributista Social"),
            ("16", "Monotributo Trabajador Independiente Promovido"),
            ("4", "IVA Sujeto Exento"),
            ("5", "Consumidor Final"),
            ("7", "Sujeto No Categorizado"),
            ("8", "Proveedor del Exterior"),
            ("9", "Cliente del Exterior"),
            ("10", "IVA Liberado – Ley N° 19.640"),
            ("15", "IVA No Alcanzado"),
        ],
        string="Condición del IVA del Receptor",
        help="Condición del IVA del sujeto receptor según RG 5616",
    )
