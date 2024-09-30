from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Custom login view to redirect after login
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('student_list')


# Custom logout view
def custom_logout(request):
    logout(request)
    return redirect('login')


# List all students
def student_list(request):
    query = request.GET.get('q', '')
    
    # Start with all students, then filter based on the search query
    students = Student.objects.all()

    # Filter students based on the search query
    if query:
        students = students.filter(
            first_name__icontains=query
        ) | students.filter(
            last_name__icontains=query
        )

    # Order the students by first name for consistency
    students = students.order_by('first_name')

    # Implement pagination
    paginator = Paginator(students, 10)  # Show 10 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'students': page_obj,
        'query': query,
    }
    return render(request, 'students/student_list.html', context)

# Display a single student's details
def student_details(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_details.html', {'student': student})


# Add a new student (only for logged-in users)
@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})


# Edit an existing student (only for logged-in users)
@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})


# Delete an existing student (only for logged-in users)
@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})