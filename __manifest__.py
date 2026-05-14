{
    "name": "College ERP",
    "version": "1.0",
    "author": "Tejas",
    "category": "Education",
    "summary": "College Management System",
    "depends": ["base", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/student_views.xml",
        "views/course_views.xml",
        "views/menu.xml",
    ],
    "application": True,
    "installable": True,
}
