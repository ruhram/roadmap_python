emp_details = {'Employee': {'Dave': {'ID': '001',
                                     'Salary': 2000,
                                     'Designation':'Python Developer'},
                            'Ava': {'ID':'002',
                                    'Salary': 2300,
                                    'Designation': 'Java Developer'},
                            'Joe': {'ID': '003',
                                    'Salary': 1843,
                                    'Designation': 'Hadoop Developer'}}}

print(emp_details['Employee'])

for karyawan in emp_details['Employee'].items() :
    print(karyawan)