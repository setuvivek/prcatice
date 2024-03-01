{
    'name': 'School Management',
    'version': '16.0',
    'description': 'student managemnet module',
    'depends':[
        'contact',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/teacher_views.xml',
        'views/department_views.xml',
    ],
}
