# -*- coding: utf-8 -*-
from odoo import models,fields,api

class SetuSchool(models.TransientModel):
    _name = 'setu.school.wizard'
    _description = 'Setu School Wizard'



    teacher_id = fields.Many2one('setu.teacher', string='Principle')


    def action_assign_principle(self):
        return







