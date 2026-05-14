from odoo import models, fields, api


class CollegeStudent(models.Model):
    _name = "college.student"
    _description = "College Student"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Student Name", required=True, tracking=True)
    student_id = fields.Char(string="Student ID", required=True)
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    admission_date = fields.Date(string="Admission Date")

    course_id = fields.Many2one(
        "college.course",
        string="Course"
    )

    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("student_id_unique",
         "unique(student_id)",
         "Student ID must be unique.")
    ]