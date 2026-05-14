from odoo import models, fields


class CollegeCourse(models.Model):
    _name = "college.course"
    _description = "College Course"

    name = fields.Char(string="Course Name", required=True)
    code = fields.Char(string="Course Code")
    duration = fields.Integer(string="Duration (Months)")

    student_ids = fields.One2many(
        "college.student",
        "course_id",
        string="Students"
    )

    active = fields.Boolean(default=True)