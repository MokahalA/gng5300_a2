from django.shortcuts import render, get_object_or_404, redirect
from .models import Student


# List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# Display a single student's details
def student_details(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_details.html', {'student': student})

# Add a new student
def student_create(request):
    # Placeholder for adding a new student form logic
    if request.method == 'POST':
        # Form submission logic will be handled here
        pass
    return render(request, 'students/student_form.html')  # Template for adding a student

# Edit an existing student
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        # Form submission logic will be handled here
        pass
    return render(request, 'students/student_form.html', {'student': student})  # Pass the student object to the template