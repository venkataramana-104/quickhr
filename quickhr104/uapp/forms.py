
from django import forms
from django.contrib.auth.models import User
from .models import Employee , Department ,leavef,AddNewEmployees,ClaimApplication,Project,Groups,CostCenter,Expenses,Inventory,Training,Holiday,Type,ATimesheet,BulkUpload,OffinLieuAllocation,ClaimUpload,CreateRoster,Importanttimesheet,AddNewShifts,AddNewWorkflow

class SignupForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','password','email','first_name','last_name']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' 

        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'Date'}),
            }
        

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__' 

class leavefForm(forms.ModelForm):
    class Meta:
        model = leavef
        fields = '__all__' 



class AddNewEmployeesForm(forms.ModelForm):
    class Meta:
        model = AddNewEmployees
        fields = '__all__'

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'Date'}),
            'joining_date': forms.DateInput(attrs={'type': 'Date'}),
            'probation_period': forms.DateInput(attrs={'type': 'Date'}),
            'confirmation_date': forms.DateInput(attrs={'type': 'Date'}),
            'last_working_day': forms.DateInput(attrs={'type': 'Date'}),
            'created_at': forms.DateInput(attrs={'type': 'Date'}),
            'updated_at': forms.DateInput(attrs={'type': 'Date'}),
        }



class ClaimApplicationForm(forms.ModelForm):
    class Meta:
        model = ClaimApplication
        fields = '__all__'

        widgets = {
            'from_date': forms.DateInput(attrs={'type': 'Date'}),
            'to_date': forms.DateInput(attrs={'type': 'Date'}),
            }



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'



class GroupsForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = '__all__'


class CostCenterForm(forms.ModelForm):
    class Meta:
        model = CostCenter
        fields = '__all__'


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__' 


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'

       


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = '__all__' 

        widgets = {
            'Effective_Date': forms.DateInput(attrs={'type': 'Date'}),
            'Projected_Date': forms.DateInput(attrs={'type': 'Date'}),
            } 



class HolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = '__all__'

        widgets = {
            'Date': forms.DateInput(attrs={'type': 'Date'}),
            }  


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__' 



class ATimesheetForm(forms.ModelForm):
    class Meta:
        model = ATimesheet
        fields = '__all__'
        
        # Optionally, you can add widgets for better UI control
        widgets = {
            'Date': forms.DateInput(attrs={'type': 'Date'}),
            'In_Time': forms.TimeInput(attrs={'type': 'Time'}),
            'Out_Time': forms.TimeInput(attrs={'type': 'Time'}),
        }


class BulkUploadForm(forms.ModelForm):
    class Meta:
        model = BulkUpload
        fields = '__all__'


class OffinLieuAllocationForm(forms.ModelForm):
    class Meta:
        model = OffinLieuAllocation
        fields = '__all__'



class ClaimUploadForm(forms.ModelForm):
    class Meta:
        model = ClaimUpload
        fields = '__all__'




class CreateRosterForm(forms.ModelForm):
    class Meta:
        model = CreateRoster
        fields = '__all__'
        widgets = {
            'Roster_From_Period': forms.DateInput(attrs={'type': 'date'}),  # 'date' in lowercase
            'Roster_To_Period': forms.DateInput(attrs={'type': 'date'}),
            'In_Time': forms.TimeInput(attrs={'type': 'time'}),  # 'time' in lowercase
            'Out_Time': forms.TimeInput(attrs={'type': 'time'}),
            'Earliest_Clock_In_Time': forms.TimeInput(attrs={'type': 'time'}),
            'Last_Clock_Out_Time': forms.TimeInput(attrs={'type': 'time'}),
            'Late_In_From': forms.TimeInput(attrs={'type': 'time'}),
        }



class ImportanttimesheetForm(forms.ModelForm):
    class Meta:
        model = Importanttimesheet
        fields = '__all__'

        

class AddNewShiftsForm(forms.ModelForm):
    class Meta:
        model = AddNewShifts
        fields = '__all__'
        widgets = {
            'In_Time': forms.TimeInput(attrs={'type': 'time'}),
            'Out_Time': forms.TimeInput(attrs={'type': 'time'}),
            'Earliest_Clock_In_Time': forms.TimeInput(attrs={'type': 'time'}),
            'Last_Clock_Out_Time': forms.TimeInput(attrs={'type': 'time'}),
            'Late_In_From': forms.TimeInput(attrs={'type': 'time'}),
        }

        

class AddNewWorkflowForm(forms.ModelForm):
    class Meta:
        model = AddNewWorkflow
        fields = '__all__'