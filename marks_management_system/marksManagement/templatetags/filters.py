from django import template
from marksManagement.models import Student ,Subject , Faculty

register = template.Library()

def searchName(value):
    st = Student.objects.get(roll_no=value)
    return st.name