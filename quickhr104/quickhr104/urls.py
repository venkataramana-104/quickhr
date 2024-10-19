"""
URL configuration for quickhr104 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from uapp import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from uapp.views import login_view, otp_verify_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homeview, name='home'),
    path('dashboard/', views.dashboardview, name='dashboard'),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', login_view, name='login'),
    path('accounts/otp_verify/', otp_verify_view, name='otp_verify'),
    path('logout/', views.logout_view, name='logout'),
    path('thanks/', views.thanksview, name='thanks'),
    path('register/', views.signup_view, name='register'),
    path('employee/', views.employeeview, name='employee_list'),
    path('employeedetails/', views.employeedetailsview, name='employeedetails'),
    path('delete/<int:id>/', views.deleteview, name='delete'),
    path('update/<int:id>/', views.updateview, name='update'),
    path('Department/', views.Departmentview, name='Department'),
    path('Departments/', views.Departmentsview, name='Departments'),
    path('employees/', views.employeesview, name='employees'),
    path('leave/', views.leaveview, name='leave'),
    path('claim/', views.claimview, name='claim'),
    path('claimapplication/', views.claimapplicationview, name='claimapplication'),
    path('claimapplications/', views.claimapplicationsview, name='claimapplications'),
    path('leavef/', views.leavefview, name='leavef'),
    path('leaveapply/', views.leaveapplyview, name='leaveapply'),
    path('timesheet/', views.timesheetview, name='timesheet'),
    path('payroll/', views.payrollview, name='payroll'),
    path('report/', views.reportview, name='report'),
    path('setting/', views.settingview, name='setting'),
    path('expanses/', views.expansesview, name='expanses'),
    path('elearning/', views.elearningview, name='elearning'),
    path('appraisal/', views.appraisalview, name='appraisal'),
    path('security/', views.securityview, name='security'),
    path('status/', views.statusview, name='status'),
    path('addnewemployee/', views.addnewemployeeview, name='addnewemployee'),
    path('addnewemployees/', views.addnewemployeesview, name='addnewemployees'),
    path('project/', views.projectview, name='project'),
    path('projects/', views.projectsview, name='projects'),
    path('groups/', views.groupsview, name='groups'),
    path('group/', views.groupview, name='group'),
    path('timesheets/', views.timesheetsview, name='timesheets'),
    path('costcenter/', views.costcenterview, name='costcenter'),
    path('expense/', views.expenseview, name='expense'),
    path('expenses/', views.expensesview, name='expenses'),
    path('inventory/', views.inventoryview, name='inventorys'),
    path('training/', views.trainingview, name='training'),
    path('holidays/', views.holidaysview, name='holidays'),
    path('holiday/', views.holidayview, name='holiday'),
    path('type/', views.typeview, name='type'),
    path('types/', views.typesview, name='types'),
    path('pendingapproval/', views.pendingapprovalview, name='pendingapproval'),
    path('addtimesheet/', views.addtimesheetview, name='addtimesheet'),
    path('atimesheet/', views.atimesheetview, name='atimesheet'),
    path('bulkupload/', views.bulkuploadview, name='bulkupload'),
    path('bulkuploaddata/', views.bulkuploaddataview, name='bulkuploaddata'),
    path('offinlieuallocation/', views.offinlieuallocationview, name='offinlieuallocation'),
    path('offinlieuallocations/', views.offinlieuallocationsview, name='offinlieuallocations'),
    path('claimupload/', views.claimuploadview, name='claimupload'),
    path('createroster/', views.createrosterview, name='createroster'),
    path('viewroster/', views.viewrosterview, name='viewroster'),
    path('importanttimesheet/', views.importanttimesheetview, name='importanttimesheet'),
    path('ottimesheet/', views.ottimesheetview, name='ottimesheet'),
    path('projectattendance/', views.projectattendanceview, name='projectattendance'),
    path('approvetimesheet/', views.approvetimesheetview, name='approvetimesheet'),
    path('dailytimesheet/', views.dailytimesheetview, name='dailytimesheetsheet'),
    path('addnewshifts/', views.addnewshiftsview, name='addnewshifts'),
    path('manageshifts/', views.manageshiftsview, name='manageshifts'),
    path('overtimehourse/', views.overtimehourseview, name='overtimehourse'),
    path('monthlytimesheet/', views.monthlytimesheetview, name='monthlytimesheet'),
    path('biometric/', views.biometricview, name='biometric'),
    path('addnewworkflow/', views.addnewworkflowview, name='addnewworkflow'),
    path('manageworkflow/', views.manageworkflowview, name='manageworkflow'),
    path('dashboard1/', views.dashboard1view, name='dashboard1'),
 ]
    