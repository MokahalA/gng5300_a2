from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'enrollment_date', 'grade']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    # Custom validation for email field
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email field is required.")
        if '@' not in email:
            raise forms.ValidationError("Invalid email format.")
        return email

    # Custom validation for grade
    def clean_grade(self):
        grade = self.cleaned_data.get('grade')
        if grade is None or grade < 1 or grade > 12:
            raise forms.ValidationError("Grade must be between 1 and 12.")
        return grade