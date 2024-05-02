# -*- coding: utf-8 -*-
from odoo import models,fields,api
import logging

_logger = logging.getLogger(__name__)

class SetuSchoolWizard(models.TransientModel):
    _name = 'setu.school.wizard'
    _description = 'Setu School Wizard'


    teacher_id = fields.Many2one('setu.teacher', string='Principle')


    def action_assign_principle(self):
        school_record = self.env['setu.school'].browse(self.env.context.get('active_id'))

        teacher = self.teacher_id
        _logger.warning('----------------->>>>Set School Principle in School')
        school_record.teacher_id = teacher

        teacher.school_id = school_record

        _logger.warning('----------------->>>>Set School Principle in Teacher')
        return {'type': 'ir.actions.act_window_close'}

    @api.model
    def default_get(self, fields):
        res = super(SetuSchoolWizard, self).default_get(fields)
        school_record = self.env['setu.school'].browse(self._context.get('active_id'))
        res['teacher_id'] = school_record.teacher_id.id
        return res


    #
    # @api.depends('product_id', 'product_uom_qty', 'product_uom')
    # def _compute_product_weight(self):
    #     for line in self:
    #         product = line.product_id
    #         if product:
    #             uom_factor = line.product_uom.factor_inv or 1.0
    #             line.product_weight = product.product_weight * line.product_uom_qty * uom_factor
    #         else:
    #             line.product_weight = 0.0


