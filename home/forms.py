from django import forms

class CourseNewForm(forms.Form):
    name = forms.CharField(label="name", max_length=100)
    year = forms.IntegerField(label="year", min_value=2005)
    start_date = forms.DateField(label="start_date")
    end_date = forms.DateField(label="end_date")
    active = forms.BooleanField(label="active", required=False)