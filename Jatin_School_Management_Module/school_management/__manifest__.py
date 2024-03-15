{
    'name' : 'School Management',
    'version' : '16.1',
    # 'summary': 'school_management',
    'depends' : ['Contact'],
    # 'depends': ['Contact'],
    'data': ['security/ir.model.access.csv',
             'views/teacher_views.xml',
            'views/student_views.xml',
            'views/department_views.xml',
             ],
}