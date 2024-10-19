
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate, login
from uapp.forms import SignupForm ,EmployeeForm, DepartmentForm,leavefForm,AddNewEmployeesForm,ClaimApplicationForm,ProjectForm,GroupsForm,CostCenterForm,ExpensesForm,InventoryForm,TrainingForm,HolidayForm,TypeForm,ATimesheetForm,BulkUploadForm,OffinLieuAllocationForm,ClaimUploadForm,CreateRosterForm,ImportanttimesheetForm,AddNewShiftsForm,AddNewWorkflowForm
from uapp.models import Employee,Department , leavef ,AddNewEmployees,ClaimApplication,Project,Groups,CostCenter,Expenses,Inventory,Training,Holiday,Type,ATimesheet,BulkUpload,OffinLieuAllocation,ClaimUpload,CreateRoster,Importanttimesheet,AddNewShifts,AddNewWorkflow
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django import forms
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm

from django.utils.timezone import now


# Create your views here.

@login_required
def homeview(request):
    emp = Employee.objects.all()
    dep = Department.objects.all()
    add = AddNewEmployees.objects.all()
    cc = CostCenter.objects.all()
    exp = Expenses.objects.all()
    inv = Inventory.objects.all()
    training =Training.objects.all()
    context = {
         'emp' : emp,
         'dep' : dep,
         'add' : add,
         'cc'  : cc,
         'exp' : exp,
         'inv' : inv,
         'training':training
        
    }
    return render(request,'uapp/home.html',context)


@login_required
def dashboardview(request):
    add = AddNewEmployees.objects.all()
    inv =Inventory.objects.all()

    context = {
        'add': add,
        'inv' : inv
    }
    return render(request, 'uapp/dashboard.html', context)


#logout
@login_required
def logout_view(request):
	logout(request)
	return redirect('/thanks')

def thanksview(request):
	return render(request,'uapp/thanks.html')


# OTP verification view
def otp_verify_view(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        username = request.session.get('username')
        
        if entered_otp == stored_otp:
            # OTP is correct, log the user in and redirect to dashboard
            user = User.objects.get(username=username)
            login(request, user)
            return HttpResponseRedirect('/dashboard1/')
        else:
            # OTP is incorrect
            return render(request, 'uapp/otp_verify.html', {'error': 'Invalid OTP'})
    
    return render(request, 'uapp/otp_verify.html')


# Function to generate OTP
def generate_otp():
    return str(random.randint(100000, 999999))



def login_view(request):
    form = AuthenticationForm()  # Use Django's built-in authentication form
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                otp = generate_otp()
                request.session['otp'] = otp  # store OTP in session
                request.session['username'] = username  # store username
                send_mail(
                    'Your OTP for Login',
                    f'Your OTP is: {otp}',
                    settings.DEFAULT_FROM_EMAIL,
                    [user.email],  # send OTP to the user's registered email
                )
                return redirect('otp_verify')  # Redirect to OTP verification page
            else:
                return render(request, 'uapp/login.html', {'form': form, 'error': 'Invalid credentials'})
    
    return render(request, 'uapp/login.html', {'form': form})


def test_email(request):
    send_mail(
        'Test Subject',
        'This is a test message.',
        'chekkavenkataramana7@gmail.com',
        ['chekkavenkataramana7@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse("Test email sent successfully")

'''
#signup form
def signup_view(request):
	form=SignupForm()
	if request.method=="POST":
		form=SignupForm(request.POST)
		user=form.save(commit=False)
		user.set_password(user.password)
		user.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request,'uapp/register.html',{'form':form})
'''
def signup_view(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
        else:
            # Debugging: Print form errors to console
            print(form.errors)
    return render(request, 'uapp/register.html', {'form': form})

#employees
@login_required
def employeesview(request):
    emp=AddNewEmployees.objects.all()
    return render(request,'uapp/employees.html',{'f':emp})


#employee form
@login_required
def employeeview(request):
    f = EmployeeForm()
    if request.method == "POST":
        f = EmployeeForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/employees')
    return render(request, 'uapp/employee.html', {'form': f})

#employeedetails
@login_required
def employeedetailsview(request):
	f=Employee.objects.all()
	return render(request,'uapp/employeedetails.html',{'f':f})

#delete
def deleteview(request, id):
	e=Employee.objects.get(id=id)
	e.delete()
	return redirect('/employeedetails')
'''
#update
def updateview(request, id):
    f = Employee.objects.get(id=id)
    if request.method == "POST":
        f = EmployeeForm(request.POST, instance=f)
        if f.is_valid():
            f.save()
            return redirect('/employeedetails')
    return render(request, 'uapp/update.html', {'g': f})
'''
#update
@login_required
def updateview(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/employeedetails')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'uapp/update.html', {'form': form})

#department
@login_required
def Departmentview(request):
    f = DepartmentForm()
    if request.method == "POST":
        f = DepartmentForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/Departments')
    return render(request, 'uapp/Department.html', {'form': f})

@login_required
def Departmentsview(request):
    f = Department.objects.all()
    return render(request, 'uapp/Departments.html', {'f': f})
'''
#delete
def deleteview(request, id):
    f=Department.objects.get(id=id)
    f.delete()
    return redirect('/departments')
'''





@login_required
def leaveview(request):
    return render(request,'uapp/leave.html')



@login_required
def claimview(request):
    return render(request,'uapp/claim.html')

'''
@login_required
def claimapplicationview(request):
    f=ClaimApplicationForm()
    if request.method=="POST":
        form=ClaimApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/claimapplications')
    return render(request,'uapp/claimapplication.html',{'form':f})
'''
@login_required
def claimapplicationview(request):
    f = ClaimApplicationForm()
    if request.method == "POST":
        f = ClaimApplicationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/claimapplications')
    return render(request, 'uapp/claimapplication.html', {'form': f})

@login_required
def claimapplicationsview(request):
    cl=ClaimApplication.objects.all()
    return render(request,"uapp/claimapplications.html",{'f':cl})


def leavefview(request):
    f=leavefForm()
    if request.method=="POST":
        form=leavefForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leaveapply')
    return render(request,'uapp/leavef.html',{'form':f})

def leaveapplyview(request):
    emp=leavef.objects.all()
    return render(request,"uapp/leaveapply.html",{'f':emp})


@login_required
def timesheetview(request):
    return render(request,'uapp/timesheet.html')


@login_required
def payrollview(request):
    return render(request,'uapp/payroll.html')

@login_required
def reportview(request):
    return render(request,'uapp/report.html')


@login_required
def settingview(request):
    return render(request,'uapp/setting.html')


@login_required
def expansesview(request):
    return render(request,'uapp/expanses.html')


@login_required
def elearningview(request):
    return render(request,'uapp/elearning.html')


@login_required
def appraisalview(request):
    return render(request,'uapp/appraisal.html')


@login_required
def securityview(request):
    return render(request,'uapp/security.html')


@login_required
def statusview(request):
    return render(request,'uapp/status.html')




#addnewemployee form
@login_required
def addnewemployeesview(request):
    f = AddNewEmployeesForm()
    if request.method == "POST":
        f = AddNewEmployeesForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/home')
    return render(request, 'uapp/addnewemployees.html', {'form': f})


@login_required
def addnewemployeeview(request):
    emp=AddNewEmployees.objects.all()
    return render(request,'uapp/addnewemployee.html',{'f':emp})


#delete
def deleteview(request, id):
    e=AddNewEmployees.objects.get(id=id)
    e.delete()
    return redirect('/addnewemployee')

#update
@login_required
def updateview(request, id):
    addnewemployee = AddNewEmployees.objects.get(id=id)  # Corrected variable name
    if request.method == "POST":
        form = AddNewEmployeesForm(request.POST, instance=addnewemployee)
        if form.is_valid():
            form.save()
            return redirect('/addnewemployee')
    else:
        form = AddNewEmployeesForm(instance=addnewemployee)  # Use the correct variable name
    return render(request, 'uapp/update.html', {'form': form})  # Pass the form to the template


#project
@login_required
def projectview(request):
    f = ProjectForm()
    if request.method == "POST":
        f = ProjectForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/projects')
    return render(request, 'uapp/project.html', {'form': f})


@login_required
def projectsview(request):
    pjt=Project.objects.all()
    return render(request,'uapp/projects.html',{'f':pjt})

@login_required
def groupsview(request):
    f =  GroupsForm()
    if request.method == "POST":
        f =  GroupsForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/group')
    return render(request, 'uapp/groups.html', {'form': f})



@login_required
def groupview(request):
    group = Groups.objects.all()
    return render(request,'uapp/group.html',{'f':group})



@login_required
def timesheetsview(request):
    return render(request,'uapp/timesheets.html')

      

@login_required
def costcenterview(request):
    f =  CostCenterForm()
    if request.method == "POST":
        f =  CostCenterForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/home')
    return render(request, 'uapp/costcenter.html', {'form': f})



@login_required
def expensesview(request):
    f =  ExpensesForm()
    if request.method == "POST":
        f =  ExpensesForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/home')
    return render(request, 'uapp/expenses.html', {'form': f})

@login_required
def expenseview(request):
    return render(request,'uapp/expense.html')


@login_required
def inventoryview(request):
    f =  InventoryForm()
    if request.method == "POST":
        f =  InventoryForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/home')
    return render(request, 'uapp/inventory.html', {'form': f})




@login_required
def trainingview(request):
    f =  TrainingForm()
    if request.method == "POST":
        f =  TrainingForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/home')
    return render(request, 'uapp/training.html', {'form': f})





@login_required
def holidayview(request):
    f = HolidayForm()
    if request.method == "POST":
        f = HolidayForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/holidays')
    return render(request, 'uapp/holiday.html', {'form': f})


@login_required
def holidaysview(request):
    hol=Holiday.objects.all()
    return render(request,'uapp/holidays.html',{'f':hol})



@login_required
def typeview(request):
    f = TypeForm()
    if request.method == "POST":
        f = TypeForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/types')
    return render(request, 'uapp/type.html', {'form': f})


@login_required
def typesview(request):
    ty=Type.objects.all()
    return render(request,'uapp/types.html',{'f':ty})




def pendingapprovalview(request):
    emp=leavef.objects.all()
    return render(request,"uapp/pendingapproval.html",{'f':emp})



@login_required
def atimesheetview(request):
    f = ATimesheetForm()
    if request.method == "POST":
        f = ATimesheetForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/addtimesheet')
    return render(request, 'uapp/atimesheet.html', {'form': f})


@login_required
def addtimesheetview(request):
    time=ATimesheet.objects.all()
    return render(request,'uapp/addtimesheet.html',{'f':time})



@login_required
def bulkuploadview(request):
    f = BulkUploadForm()
    if request.method == "POST":
        f = BulkUploadForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/bulkuploaddata')
    return render(request, 'uapp/bulkupload.html', {'form': f})


@login_required
def bulkuploaddataview(request):
    bulk=BulkUpload.objects.all()
    return render(request,'uapp/bulkuploaddata.html',{'f':bulk})




@login_required
def offinlieuallocationview(request):
    f = OffinLieuAllocationForm()
    if request.method == "POST":
        f = OffinLieuAllocationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/offinlieuallocations')
    return render(request, 'uapp/offinlieuallocation.html', {'form': f})


@login_required
def offinlieuallocationsview(request):
    lieu=OffinLieuAllocation.objects.all()
    return render(request,'uapp/offinlieuallocations.html',{'f':lieu})



@login_required
def claimuploadview(request):
    return render(request,'uapp/claimupload.html')



@login_required
def claimuploadview(request):
    f =ClaimUploadForm()
    if request.method == "POST":
        f = ClaimUploadForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/claim')
    return render(request, 'uapp/claimupload.html', {'form': f})




@login_required
def createrosterview(request):
    f =CreateRosterForm()
    if request.method == "POST":
        f = CreateRosterForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/timesheet')
    return render(request, 'uapp/createroster.html', {'form': f})




@login_required
def viewrosterview(request):
    CR=CreateRoster.objects.all()
    return render(request,'uapp/viewroster.html',{'f':CR})











@login_required
def importanttimesheetview(request):
    return render(request,'uapp/importanttimesheet.html')


@login_required
def importanttimesheetview(request):
    f =ImportanttimesheetForm()
    if request.method == "POST":
        f =ImportanttimesheetForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/timesheet')
    return render(request, 'uapp/importanttimesheet.html', {'form': f})




@login_required
def ottimesheetview(request):
    ot=CreateRoster.objects.all()
    return render(request,'uapp/ottimesheet.html',{'f':ot})



@login_required
def projectattendanceview(request):
    pja=Project.objects.all()
    return render(request,'uapp/projectattendance.html',{'f':pja})





@login_required
def approvetimesheetview(request):
    appr=CreateRoster.objects.all()
    return render(request,'uapp/approvetimesheet.html',{'f':appr})



@login_required
def dailytimesheetview(request):
    daily=CreateRoster.objects.all()
    return render(request,'uapp/dailytimesheet.html',{'f':daily})




@login_required
def addnewshiftsview(request):
    f =AddNewShiftsForm()
    if request.method == "POST":
        f =AddNewShiftsForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/manageshifts')
    return render(request, 'uapp/addnewshifts.html', {'form': f})

'''
@login_required
def manageshiftsview(request):
    MS=AddNewShifts.objects.all()
    return render(request,'uapp/manageshifts.html',{'f':MS})
'''
@login_required
def manageshiftsview(request):
    shifts = AddNewShifts.objects.all()
    return render(request, 'uapp/manageshifts.html', {'shifts': shifts})


@login_required
def overtimehourseview(request):
    overtime=CreateRoster.objects.all()
    return render(request,'uapp/overtimehourse.html',{'f':overtime})


@login_required
def monthlytimesheetview(request):
    MTS=CreateRoster.objects.all()
    return render(request,'uapp/monthlytimesheet.html',{'f':MTS})


@login_required
def biometricview(request):
    bio=CreateRoster.objects.all()
    return render(request,'uapp/biometric.html',{'f':bio})




@login_required
def addnewworkflowview(request):
    f =AddNewWorkflowForm()
    if request.method == "POST":
        f = AddNewWorkflowForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/manageworkflow')
    return render(request, 'uapp/addnewworkflow.html', {'form': f})



@login_required
def manageworkflowview(request):
    work=AddNewWorkflow.objects.all()
    return render(request,'uapp/manageworkflow.html',{'f':work})




@login_required
def dashboard1view(request):
    today = now().date()
    total_users = User.objects.count()
    logged_in_today = User.objects.filter(last_login__date=today).count()
    
    context = {
        'total_users': total_users,
        'logged_in_today': logged_in_today,
    }
    return render(request,'uapp/dashboard1.html', context)

