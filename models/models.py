# -*- coding: utf-8 -*-

from odoo import models, fields, api

   class Course(models.Model)
     _name = 'open_academy.course'
     _description= "OpenAcademy Courses"
     name = fields.Char(string="Title",reqquired=True)
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
