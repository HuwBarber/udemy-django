from django.shortcuts import render

def render_template(request):
    data = {
        "name":"Huw"
    }
    return render(request, 'templatesApp/firstTemplate.html', data)

def render_employee(request):
    data = {
        "id":123,
        "name":"John",
        "salary":10000
    }
    return render(request, 'templatesApp/employeeTemplate.html', data)
