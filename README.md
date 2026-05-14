# College ERP

![Version](https://img.shields.io/badge/version-1.0-blue)
![Category](https://img.shields.io/badge/category-Education-green)
![License](https://img.shields.io/badge/license-LGPL-3-orange)
![Type](https://img.shields.io/badge/type-Application-purple)

| | |
|---|---|
| **Name** | College ERP |
| **Version** | 1.0 |
| **Category** | Education |
| **Author** | Tejas |
| **License** | LGPL-3 |
| **Application** | Yes |

## Description

College Management System

## Functionality

### Models & Fields

#### `college.course` — College Course

**File:** `models/course.py`

**Fields:**

| Field | Type |
|-------|------|
| `name` | `Char` |
| `code` | `Char` |
| `duration` | `Integer` |
| `student_ids` | `One2many` |
| `active` | `Boolean` |

#### `college.student` — College Student

**File:** `models/student.py`

**Inherits:** `mail.thread`, `mail.activity.mixin`

**Fields:**

| Field | Type |
|-------|------|
| `name` | `Char` |
| `student_id` | `Char` |
| `phone` | `Char` |
| `email` | `Char` |
| `admission_date` | `Date` |
| `course_id` | `Many2one` |
| `active` | `Boolean` |

### Views & UI

**Form Views:** `course_views.xml`, `student_views.xml`

**List/Tree Views:** `course_views.xml`, `student_views.xml`

**Menus:** `menu.xml`

### Security

**Access Rights:** 2 model access rules defined

| Model |
|-------|
| `college.student` |
| `college.course` |

## Dependencies

| Module | Type |
|--------|------|
| `base` | Odoo Core |
| `mail` | Odoo Core |

## File Structure

```
college_erp/
├── LICENSE
├── README.md
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── course.py
│   └── student.py
├── security/
│   └── ir.model.access.csv
├── static/
│   └── description/
│       └── icon.png
└── views/
    ├── course_views.xml
    ├── menu.xml
    └── student_views.xml
```

## Installation

This module is part of the **[odoo-hr-education-finance-suite](https://github.com/tejas7287/odoo-hr-education-finance-suite)** suite.

1. Place this module in your Odoo addons directory
2. Update the apps list: **Settings** → **Apps** → **Update Apps List**
3. Search for **"College ERP"** and click **Install**

## License

LGPL-3
