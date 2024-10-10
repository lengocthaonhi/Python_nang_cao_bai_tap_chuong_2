#Lê Ngọc Thảo Nhi - DHKL17A2HN
#Lập trình Python nâng cao - chương 2
#Bài 2.3

from xml.dom import minidom

# Tải và phân tích tệp XML
doc = minidom.parse('sample.xml')

# Lấy tên công ty
company_name = doc.getElementsByTagName('name')[0].firstChild.nodeValue
print("Company Name:", company_name)

# Lấy danh sách nhân viên
staff_list = doc.getElementsByTagName('staff')

print("\nStaff Details:")
for staff in staff_list:
    staff_id = staff.getAttribute('id')
    staff_name = staff.getElementsByTagName('name')[0].firstChild.nodeValue
    staff_salary = staff.getElementsByTagName('salary')[0].firstChild.nodeValue
    print(f"ID: {staff_id}, Name: {staff_name}, Salary: {staff_salary}")
