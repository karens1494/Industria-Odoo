# -*- coding: utf-8 -*-

from odoo import models, fields, api

   class Course(models.Model)
     _name = 'open_academy.course'
     _description= "OpenAcademy Courses"
     responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
     name = fields.Char(string="Title",reqquired=True)
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class Session(models.Model):
    _name = 'open_academy.session'
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('open_academy.course',
        ondelete='cascade', string="Course", required=True)
       attendee_ids = fields.Many2many('res.partner', string="Attendees")
