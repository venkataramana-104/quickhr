from django.contrib import admin
from uapp.models import Employee, Department, leavef, AddNewEmployees ,ClaimApplication,Project,Groups,CostCenter,Expenses,Inventory,Training,Holiday,Type,ATimesheet,BulkUpload,OffinLieuAllocation,ClaimUpload,CreateRoster,Importanttimesheet,AddNewShifts,AddNewWorkflow

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'role', 'position', 'gender', 'joining_date')

admin.site.register(Employee, EmployeeAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('image', 'Department_Name', 'Employees')

admin.site.register(Department, DepartmentAdmin)

class leavefAdmin(admin.ModelAdmin):
    list_display = ('Employee', 'Leavetype', 'Balance_Leave', 'From_Date', 'To_Date', 'Session', 'No_ofdaysapplying', 'Remarks', 'Upload_Document')

admin.site.register(leavef, leavefAdmin)


class AddNewEmployeesAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'alias_name', 'preferred_name', 'gender',
        'marital_status', 'date_of_birth', 'nationality', 'religion', 'race',
        'blood_group', 'place_of_birth', 'identification', 'type', 'ic_no',
        'block_number', 'house_number', 'street_number', 'country', 'postal_code',
        'mobile_no', 'emergency_contact_person', 'overseas_address',
        'personal_email_address', 'photograph', 'email', 'user_security',
        'custom_field_add', 'dfsf', 'email_outlook_access', 'first_name_for_email_creation',
        'jhbjhg', 'laptop', 'last_name_for_email_creation', 'may_day',
        'nameofvaccine_1stdose', 'new_year_event', 'physical_last_day',
        'physical_last_working_day', 'sports', 'surname', 'tests', 'id',
        'joining_date', 'employment_type', 'probation_period', 'confirmation_date',
        'department', 'designation', 'groups', 'supervisor_name', 'appraisal_supervisor1',
        'appraisal_supervisor2', 'academic_qualification', 'skill_set',
        'working_hours_per_day', 'working_hours_per_day_breakdown',
        'no_of_work_days_per_week', 'leave_entitlement', 'leave_description',
        'no_of_leaves_taken', 'no_of_leaves_remaining', 'leave_carryforward',
        'no_of_leaves_carryforward', 'joining_bonus', 'bonus_description',
        'daily_wage', 'monthly_salary', 'performance_allowance',
        'fixed_allowance', 'variable_allowance', 'company_car', 'company_phone',
        'company_laptop', 'other_benefits', 'uniform', 'is_currently_employed',
        'resuming_job', 'last_working_day', 'email_verification_status', 'remarks',
        'emp_ref_no', 'created_at', 'updated_at'
    )
    list_display_links = ('first_name', 'last_name')  # Optional: make names clickable
    search_fields = ('first_name', 'last_name', 'email')  # Fields to be searchable

admin.site.register(AddNewEmployees, AddNewEmployeesAdmin)

class ClaimApplicationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'claim_type', 'from_date', 'to_date', 'project', 'custom_claim', 'receipt_id', 'attachment1', 'attachment2', 'description')

admin.site.register(ClaimApplication, ClaimApplicationAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'project_id', 'photograph', 'project_name', 'department', 'group', 'employee', 'shift', 'supervisor',
        'description', 'public_holiday', 'rest_day'
    )

admin.site.register(Project, ProjectAdmin)

class GroupsAdmin(admin.ModelAdmin):
    list_display = (
        'group_id', 'photograph', 'group_name', 'department', 'projects', 'employees'
    )
    
admin.site.register(Groups, GroupsAdmin)



class CostCenterAdmin(admin.ModelAdmin):
    list_display = ('cost_center', 'description', 'percentage')
    
admin.site.register(CostCenter, CostCenterAdmin)


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('Amount', 'Issue_Date', 'description')
    
admin.site.register(Expenses, ExpensesAdmin)


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('Item_Name', 'Quantity', 'Attachment', 'Description', 'Date_Of_Issue', 'Date_Of_Collection')
    
admin.site.register(Inventory, InventoryAdmin)



class TrainingAdmin(admin.ModelAdmin):
    list_display = ('Certification', 'Grade', 'Attachment', 'Effective_Date', 'Projected_Date', 'Status')
    
admin.site.register(Training, TrainingAdmin)


class HolidayAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Date')
    
admin.site.register(Holiday, HolidayAdmin)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('Leave_type_title', 'Leave_code','Functionality','No_of_default_leave','Full_day',
         'Half_day','Employee_remarks','Upload_document','Approvers_remarks','Entitled_in_probation',
         'Not_entitled_in_probation','Note','Yes','No')
    
admin.site.register(Type, TypeAdmin)



class ATimesheetAdmin(admin.ModelAdmin):
    list_display = ('Project', 'Shift', 'Employee', 'Date', 'In_Time', 'Out_Time')

admin.site.register(ATimesheet, ATimesheetAdmin)



class BulkUploadAdmin(admin.ModelAdmin):
    list_display = ('Template', 'Format', 'Upload_document')

admin.site.register(BulkUpload, BulkUploadAdmin)


class OffinLieuAllocationAdmin(admin.ModelAdmin):
    list_display = ('Template', 'Format', 'Upload_document')

admin.site.register(OffinLieuAllocation, OffinLieuAllocationAdmin)



class ClaimUploadAdmin(admin.ModelAdmin):
    list_display = ('upload_xls_file',)

admin.site.register(ClaimUpload, ClaimUploadAdmin)




class CreateRosterAdmin(admin.ModelAdmin):
    list_display = ('Roster_Name','Select_Days','Roster_From_Period','Roster_To_Period',
        'Department','Groups','Project','Employee','In_Time','Out_Time','Earliest_Clock_In_Time',
        'Last_Clock_Out_Time','Auto_Clock_Out','Break_Time_Normal_Hours','OT_Break_Time_Normal_Hours',
        'OT_To_Only_Start_After','OT_Break_Takes_Effect_After','Late_In_From','Apply_Days',
        'Basic_Pay','Custom_Fine','Fixed','Common_OT','Hourly_OT','Total_OT_Hours',
        'Off_in_Lieu','Default','MOM_Regulation','OT_By_Minutes','OT_By_Block_30mins','OT_By_Block_15mins')

admin.site.register(CreateRoster, CreateRosterAdmin)


class ImportanttimesheetAdmin(admin.ModelAdmin):
    list_display = ('Template','Format','Upload_Document')

admin.site.register(Importanttimesheet, ImportanttimesheetAdmin)



class AddNewShiftsAdmin(admin.ModelAdmin):
    list_display = ('Shift_ID','Shift_Name','Pick_Color','In_Time','Out_Time',
        'Earliest_Clock_In_Time','Last_Clock_Out_Time','Auto_Clock_Out','Break_Time_Normal_Hours',
        'OT_Break_Time_Normal_Hours','OT_To_Only_Start_After','OT_Break_Takes_Effect_After',
        'Late_In_From','Apply_Days','Basic_Pay','Custom_Fine','Fixed','Roster_Settings','Amount',
        'Postal_Code','Supervisor_Name')

admin.site.register(AddNewShifts, AddNewShiftsAdmin)


class AddNewWorkflowAdmin(admin.ModelAdmin):
    list_display = ('Workflow_Type','Default','Specific','Workflow_Name','Departments','Groups','Project','Employee','Levels')

admin.site.register(AddNewWorkflow, AddNewWorkflowAdmin)
