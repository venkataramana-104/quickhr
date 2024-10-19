from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Employee(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('Prefer not to say', 'Prefer not to say'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    joining_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name']
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'



class Department(models.Model):
    Employee_CHOICES = [
        ('BioOne(EB-49)', 'BioOne(EB-49)'),
        ('ChikU(EN-1089)', 'ChikU(EN-1089)'),
        ('CVCV(EB-42)', 'CVCV(EB-42)'),
        ('Daily Allow(EB-39)', 'Daily Allow(EB-39)'),
        ('Daily Half(EB-52)', 'Daily Half(EB-52)'),
        ('Daily Mon(EB-3)', 'Daily Mon(EB-3)'),
        ('Day Count(EB-36)', 'Day Count(EB-36)'),
    ]
    
    image = models.ImageField(upload_to='path/to/upload', null=True, blank=True)
    Department_Name = models.CharField(max_length=100)
    Employees = models.CharField(max_length=20, choices=Employee_CHOICES)

    def __str__(self):
        return self.Department_Name


class leavef(models.Model):
    Employee = models.CharField(max_length=30)
    Leavetype = models.CharField(max_length=302)
    Balance_Leave = models.CharField(max_length=500)
    From_Date = models.CharField(max_length=30)
    To_Date = models.CharField(max_length=30)
    Session = models.CharField(max_length=300)
    No_ofdaysapplying = models.CharField(max_length=30)
    Remarks = models.CharField(max_length=300)
    Upload_Document = models.CharField(max_length=30)




class AddNewEmployees(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    alias_name = models.CharField(max_length=30)
    preferred_name = models.CharField(max_length=40, choices=[
        ('Alias-Name', 'Alias-Name'), ('First Name-LastName', 'First Name-LastName')
    ])
    gender = models.CharField(max_length=40, choices=[
        ('Male', 'Male'), ('Female', 'Female')
    ])
    marital_status = models.CharField(max_length=40, choices=[
        ('Divorced', 'Divorced'), ('Married', 'Married'), ('Separated', 'Separated'),
        ('Single', 'Single'), ('Widowed', 'Widowed')
    ])
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=40, choices=[
        ('Singaporean', 'Singaporean'), ('Indian', 'Indian'), ('Malaysian', 'Malaysian'), ('Bangladeshi', 'Bangladeshi')
    ])
    religion = models.CharField(max_length=40, choices=[
        ('Bahai', 'Bahai'), ('Buddhist', 'Buddhist'), ('Catholic', 'Catholic'),
        ('Christian', 'Christian'), ('Hindu', 'Hindu'), ('Jewish', 'Jewish'),
        ('Muslim', 'Muslim'), ('Not-Applicable', 'Not-Applicable'), ('Sikh', 'Sikh'),
        ('Taoist', 'Taoist'), ('Zoroastrian', 'Zoroastrian')
    ])
    race = models.CharField(max_length=40, choices=[
        ('African', 'African'), ('African-American', 'African-American'), ('Asian-American', 'Asian-American'),
        ('Caucasian', 'Caucasian'), ('Chinese', 'Chinese'), ('Eurasian', 'Eurasian'), ('Filipino', 'Filipino'),
        ('Indian', 'Indian'), ('Japanese', 'Japanese'), ('Korean', 'Korean'), ('Latino', 'Latino'), ('Malay', 'Malay'),
        ('Others', 'Others'), ('Pakistani', 'Pakistani'), ('Thai', 'Thai'), ('Vietnamese', 'Vietnamese')
    ])
    blood_group = models.CharField(max_length=3, choices=[
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')
    ])
    place_of_birth = models.CharField(max_length=30)
    identification = models.CharField(max_length=40, choices=[
        ('DependentPass', 'DependentPass'), ('EmploymentPass', 'EmploymentPass'), ('EntrepreneurPass', 'EntrepreneurPass'),
        ('LongTermVisitPass', 'LongTermVisitPass'), ('OnePass', 'OnePass'), ('Others', 'Others'), ('PEPPass', 'PEPPass'),
        ('SingaporeCitizen', 'SingaporeCitizen'), ('SingaporePR', 'SingaporePR'), ('StudentPass', 'StudentPass'),
        ('SPass', 'SPass'), ('TrainingEmploymentPass', 'TrainingEmploymentPass'), ('WorkPermit', 'WorkPermit')
    ])
    type = models.CharField(max_length=4, choices=[
        ('FIN', 'FIN'), ('NRIC', 'NRIC')
    ])
    ic_no = models.CharField(max_length=300)
    block_number = models.CharField(max_length=300)
    house_number = models.CharField(max_length=300)
    street_number = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    postal_code = models.CharField(max_length=300)
    mobile_no = models.CharField(max_length=300)
    emergency_contact_person = models.CharField(max_length=300)
    overseas_address = models.CharField(max_length=300)
    personal_email_address = models.CharField(max_length=300)
    photograph = models.ImageField(upload_to='employee_photographs/',null=True,blank=True)
    email = models.CharField(max_length=30)
    user_security = models.CharField(max_length=40, choices=[
        ('AManager', 'AManager'), ('abc', 'abc'), ('adminaccess', 'adminaccess'), ('AFEW', 'AFEW'),
        ('Cleaner', 'Cleaner'), ('Director', 'Director'), ('dummyHRD', 'dummyHRD'), ('dummyright', 'dummyright'),
        ('EMP', 'EMP'), ('EMPdup', 'EMPdup'), ('Employee', 'Employee'), ('FinanceManager', 'FinanceManager'),
        ('HRManager', 'HRManager'), ('HRManager1', 'HRManager1'), ('Jump', 'Jump'), ('Manager', 'Manager'),
        ('Newright', 'Newright'), ('NEWRTH', 'NEWRTH')
    ])
    custom_field_add = models.CharField(max_length=40, choices=[
        ('+AddNew', '+AddNew'), ('asdf', 'asdf'), ('Customi_-"', 'Customi_-"'), ('Sivatst', 'Sivatst'),
        ('tFA-sdfdsfe', 'tFA-sdfdsfe'), ('varana', 'varana')
    ])
    dfsf = models.CharField(max_length=100)
    email_outlook_access = models.CharField(max_length=40, choices=[
        ('+AddNew', '+AddNew'), ('No', 'No'), ('Yes', 'Yes')
    ])
    first_name_for_email_creation = models.CharField(max_length=100)
    jhbjhg = models.CharField(max_length=40, choices=[
        ('+AddNew', '+AddNew')
    ])
    laptop = models.CharField(max_length=40, choices=[
        ('+AddNew', '+AddNew'), ('No', 'No'), ('testsiv', 'testsiv'), ('Yes', 'Yes')
    ])
    last_name_for_email_creation = models.CharField(max_length=100)
    may_day = models.CharField(max_length=300)
    nameofvaccine_1stdose = models.CharField(max_length=300)
    new_year_event = models.CharField(max_length=40, choices=[
        ('+AddNew', '+AddNew'), ('AppleEvent', 'AppleEvent'), ('Dec31st', 'Dec31st'), ('jan1st', 'jan1st')
    ])
    physical_last_day = models.CharField(max_length=300)
    physical_last_working_day = models.CharField(max_length=300)
    sports = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    tests = models.CharField(max_length=300)
    id = models.AutoField(primary_key=True)
    joining_date = models.DateField()
    employment_type = models.CharField(max_length=40, choices=[
        ('Contract', 'Contract'), ('Full-Time', 'Full-Time'), ('Intern', 'Intern'), ('Part-time', 'Part-time')
    ])
    probation_period = models.DateField()
    confirmation_date = models.DateField()
    department = models.CharField(max_length=300, choices=[
        ('Desiger', 'Desiger'), ('Developer', 'Developer'), ('Finanace', 'Finanace')
    ])
    designation = models.CharField(max_length=300, choices=[
        ('DepartmentD', 'DepartmentD'), ('Developer', 'Developer'), ('MarkeingManager', 'MarkeingManager'),
        ('salesDirector', 'salesDirector')
    ])
    groups = models.CharField(max_length=300, choices=[
        ('1111', '1111'), ('222', '222'), ('Btech', 'Btech'), ('Btech1', 'Btech1'), ('Btech22', 'Btech22')
    ])
    supervisor_name = models.CharField(max_length=300, choices=[
        ('Adhocs', 'Adhocs'), ('Aihy', 'Aihy'), ('Aihyone', 'Aihyone'), ('AlanTest', 'AlanTest')
    ])
    appraisal_supervisor1 = models.CharField(max_length=300, choices=[
        ('Adhocs', 'Adhocs'), ('Aihy', 'Aihy'), ('Aihyone', 'Aihyone'), ('AlanTest', 'AlanTest')
    ])
    appraisal_supervisor2 = models.CharField(max_length=300, choices=[
        ('Adhocs', 'Adhocs'), ('Aihy', 'Aihy'), ('Aihyone', 'Aihyone'), ('AlanTest', 'AlanTest')
    ])
    academic_qualification = models.CharField(max_length=300, choices=[
        ('B.Tech', 'B.Tech'), ('MBA', 'MBA'), ('MCA', 'MCA'), ('MTech', 'MTech'), ('Mcom', 'Mcom'), ('UG', 'UG')
    ])
    skill_set = models.CharField(max_length=300)
    working_hours_per_day = models.CharField(max_length=300, choices=[
        ('8', '8')
    ])
    working_hours_per_day_breakdown = models.CharField(max_length=500)
    no_of_work_days_per_week = models.CharField(max_length=500, choices=[
        ('5', '5')
    ])
    leave_entitlement = models.CharField(max_length=300, choices=[
        ('12', '12')
    ])
    leave_description = models.CharField(max_length=300)
    no_of_leaves_taken = models.CharField(max_length=300, choices=[
        ('10', '10')
    ])
    no_of_leaves_remaining = models.CharField(max_length=300)
    leave_carryforward = models.CharField(max_length=300, choices=[
        ('No', 'No'), ('Yes', 'Yes')
    ])
    no_of_leaves_carryforward = models.CharField(max_length=300)
    joining_bonus = models.CharField(max_length=300)
    bonus_description = models.CharField(max_length=300)
    daily_wage = models.CharField(max_length=300)
    monthly_salary = models.CharField(max_length=300)
    performance_allowance = models.CharField(max_length=300)
    fixed_allowance = models.CharField(max_length=300)
    variable_allowance = models.CharField(max_length=300)
    company_car = models.CharField(max_length=300)
    company_phone = models.CharField(max_length=300)
    company_laptop = models.CharField(max_length=300)
    other_benefits = models.CharField(max_length=300)
    uniform = models.CharField(max_length=300)
    is_currently_employed = models.CharField(max_length=40, choices=[
        ('No', 'No'), ('Yes', 'Yes')
    ])
    resuming_job = models.CharField(max_length=300)
    last_working_day = models.DateField()
    email_verification_status = models.CharField(max_length=40, choices=[
        ('Verified', 'Verified'), ('Not-Verified', 'Not-Verified')
    ])
    remarks = models.CharField(max_length=300)
    emp_ref_no = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ClaimApplication(models.Model):  # Class name corrected to CamelCase
    employee = models.CharField(max_length=30)
    claim_type = models.CharField(max_length=302)  # Field names corrected to use snake_case
    from_date = models.DateField()  # DateField is suitable for calendar dates
    to_date = models.DateField()  # DateField is suitable for calendar dates
    project = models.CharField(max_length=500)
    custom_claim = models.CharField(max_length=500)
    receipt_id = models.CharField(max_length=500)
    attachment1 = models.FileField(upload_to='employee_documents/', null=True, blank=True)
    attachment2 = models.FileField(upload_to='employee_documents/', null=True, blank=True)
    description = models.TextField(max_length=600)

    def __str__(self):
        return self.employee  # String representation for better readability



class Project(models.Model):
    project_id = models.CharField(max_length=10, unique=True)  # Custom ID field
    photograph = models.ImageField(upload_to='photographs/', null=True, blank=True)
    project_name = models.CharField(max_length=100)  # Field to store the project name

    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
        ('Finance', 'Finance'),
        ('Marketing', 'Marketing'),
        ('Sales', 'Sales'),
        ('Operations', 'Operations'),
        ('Customer Service', 'Customer Service'),
        ('Legal', 'Legal'),
        ('R&D', 'Research and Development'),
        ('Admin', 'Administration'),
    ]
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)  # Department choices

    GROUP_CHOICES = [
        ('Tester', 'A'),
        ('B', 'Developer'),
        ('C', 'Manager'),
        ('D', 'Teamlead'),
        ('E', 'Employee'),
        ('F', 'Fresher'),
        ('G', 'Experienced'),
        ('H', 'Python'),
        ('I', 'Java'),
        ('J', 'Web Developing'),
    ]
    group = models.CharField(max_length=100, choices=GROUP_CHOICES)  # Group choices

    EMPLOYEE_CHOICES = [
        ('John Doe', 'John Doe'),
        ('Jane Smith', 'Jane Smith'),
        ('Alice Johnson', 'Alice Johnson'),
        ('Bob Brown', 'Bob Brown'),
        ('Charlie Davis', 'Charlie Davis'),
        ('Diana Evans', 'Diana Evans'),
        ('Frank Green', 'Frank Green'),
        ('Grace Harris', 'Grace Harris'),
        ('Henry Ives', 'Henry Ives'),
        ('Ivy Jones', 'Ivy Jones'),
    ]
    employee = models.CharField(max_length=100, choices=EMPLOYEE_CHOICES)  # Employee choices

    SHIFT_CHOICES = [
        ('Morning', 'Morning Shift'),
        ('Afternoon', 'Afternoon Shift'),
        ('Night', 'Night Shift'),
        ('Weekend', 'Weekend Shift'),
        ('Flexible', 'Flexible Shift'),
    ]
    shift = models.CharField(max_length=100, choices=SHIFT_CHOICES)  # Shift choices

    SUPERVISOR_CHOICES = [
        ('John Smith', 'John Smith'),
        ('Emily Johnson', 'Emily Johnson'),
        ('Michael Brown', 'Michael Brown'),
        ('Sarah Davis', 'Sarah Davis'),
        ('David Wilson', 'David Wilson'),
        ('Laura Moore', 'Laura Moore'),
        ('James Taylor', 'James Taylor'),
        ('Linda Anderson', 'Linda Anderson'),
        ('Robert Thomas', 'Robert Thomas'),
        ('Karen White', 'Karen White'),
    ]
    supervisor = models.CharField(max_length=100, choices=SUPERVISOR_CHOICES)  # Supervisor choices

   
    description = models.TextField(blank=True, null=True)  # Optional: Additional description

    PUBLIC_HOLIDAY_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    public_holiday = models.CharField(max_length=5, choices=PUBLIC_HOLIDAY_CHOICES)  # Public holiday choices

    REST_DAY_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    rest_day = models.CharField(max_length=5, choices=REST_DAY_CHOICES)  # Rest day choices

    def _str_(self):
        return self.project_name


class Groups(models.Model):
    group_id = models.CharField(max_length=10, unique=True)  # Custom ID field
    photograph = models.ImageField(upload_to='photographs/', null=True, blank=True)
    group_name = models.CharField(max_length=100)  # Field to store the project name

    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
        ('Finance', 'Finance'),
        ('Marketing', 'Marketing'),
        ('Sales', 'Sales'),
        ('Operations', 'Operations'),
        ('Customer Service', 'Customer Service'),
        ('Legal', 'Legal'),
        ('R&D', 'Research and Development'),
        ('Admin', 'Administration'),
    ]
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)  # Department choices

    PROJECTS_CHOICES = [
        ('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
        ('Finance', 'Finance'),
        ('Marketing', 'Marketing'),
        ('Sales', 'Sales'),
        ('Operations', 'Operations'),
        ('Customer Service', 'Customer Service'),
        ('Legal', 'Legal'),
        ('R&D', 'Research and Development'),
        ('Admin', 'Administration'),
    ]
    projects = models.CharField(max_length=100, choices=PROJECTS_CHOICES)  # Projects choices

    EMPLOYEES_CHOICES = [
        ('John Doe', 'John Doe'),
        ('Jane Smith', 'Jane Smith'),
        ('Alice Johnson', 'Alice Johnson'),
        ('Bob Brown', 'Bob Brown'),
        ('Charlie Davis', 'Charlie Davis'),
        ('Diana Evans', 'Diana Evans'),
        ('Frank Green', 'Frank Green'),
        ('Grace Harris', 'Grace Harris'),
        ('Henry Ives', 'Henry Ives'),
        ('Ivy Jones', 'Ivy Jones'),
    ]
    employees = models.CharField(max_length=100, choices=EMPLOYEES_CHOICES)  # Employee choices

    def _str_(self):
        return self.group_name


class CostCenter(models.Model):
    cost_center = models.CharField(max_length=40, choices=[
        ('Demo cost center Testing-dc_123', 'Demo cost center Testing-dc_123'),
        ('Human Resources-HRs', 'Human Resources-HRs'),
        ('Project A s123@-PAs@85','Project A s123@-PAs@85'),
        ('Project B-PB','Project B-PB')
    ])
    description = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)  # Use DecimalField to store percentages

    def __str__(self):
        return self.cost_center



class Expenses(models.Model):
    Amount = models.DecimalField(max_digits=65, decimal_places=5)
    Issue_Date = models.DateField()
    description = models.CharField(max_length=100) 

    def __str__(self):
        return f"{self.description} - {self.Amount}"


class Inventory(models.Model):
    Item_Name = models.CharField(max_length=100)
    Quantity = models.DecimalField(max_digits=10, decimal_places=2)
    Attachment = models.ImageField(upload_to='photographs/', null=True, blank=True)
    Description = models.CharField(max_length=255, null=True, blank=True)
    Date_Of_Issue = models.DateField()
    Date_Of_Collection = models.DateField()

    def __str__(self):
        return self.Item_Name


class Training(models.Model):
    Certification = models.CharField(max_length=100)
    Grade = models.DecimalField(max_digits=10, decimal_places=2)
    Attachment = models.ImageField(upload_to='photographs/', null=True, blank=True)
    Effective_Date = models.DateField()
    Projected_Date = models.DateField()
    Status = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.Certification


class Holiday(models.Model):
    Name = models.CharField(max_length=100)
    Date = models.DateField()

    def __str__(self):
        return f"{self.Name} on {self.Date}"

class Type(models.Model):
    Leave_type_title = models.CharField(max_length=100)
    Leave_code = models.CharField(max_length=100)
    Functionality = models.CharField(
        max_length=40, 
        choices=[
            ('Apply in days', 'Apply in days'),
            ('Apply in hours', 'Apply in hours'),
            ('Apply in minutes', 'Apply in minutes'),
            ('Off in lieu', 'Off in lieu'),
            ('No pay leave', 'No pay leave')
        ]
    )
    No_of_default_leave = models.IntegerField()  # Changed to IntegerField
    Full_day = models.BooleanField(default=False)
    Half_day = models.BooleanField(default=False)
    Employee_remarks = models.BooleanField(default=False)
    Upload_document = models.BooleanField(default=False)
    Approvers_remarks = models.BooleanField(default=False)
    Entitled_in_probation = models.BooleanField(default=False)
    Not_entitled_in_probation = models.BooleanField(default=False)
    Note = models.TextField(blank=True, null=True)
    Yes = models.BooleanField(default=False)
    No = models.BooleanField(default=False) 

    def __str__(self):
        return self.Leave_type_title


class ATimesheet(models.Model):
    Project = models.CharField(max_length=100)
    Shift = models.CharField(max_length=100)
    Employee = models.CharField(max_length=100)
    Date = models.DateField()
    In_Time = models.TimeField()
    Out_Time = models.TimeField()

    def __str__(self):
        return f"{self.Employee} - {self.Project} ({self.Date})"



class BulkUpload(models.Model):
    TEMPLATE_CHOICES = [
        ('Employees Leave Information', 'Employees Leave Information'),
        ('Employees Annual Earned Leave Information', 'Employees Annual Earned Leave Information'),
    ]
    
    FORMAT_CHOICES = [
        ('Excel', 'Excel'),
    ]

    Template = models.CharField(max_length=100, choices=TEMPLATE_CHOICES)
    Format = models.CharField(max_length=100, choices=FORMAT_CHOICES)
    Upload_document = models.FileField(upload_to='uploads/',blank=True, null=True)

    def __str__(self):
        return f"{self.Template} - {self.Format}"



class OffinLieuAllocation(models.Model):
    TEMPLATE_CHOICES = [
        ('Template', 'Template'),
        ]
    
    FORMAT_CHOICES = [
        ('Excel', 'Excel'),
    ]

    Template = models.CharField(max_length=100, choices=TEMPLATE_CHOICES)
    Format = models.CharField(max_length=100, choices=FORMAT_CHOICES)
    Upload_document = models.FileField(upload_to='uploads/',blank=True, null=True)

    def __str__(self):
        return f"{self.Template} - {self.Format}"

        

class ClaimUpload(models.Model):
    upload_xls_file = models.FileField(upload_to='uploads/', blank=True, null=True)




class CreateRoster(models.Model):
    Roster_Name = models.CharField(max_length=100)
    
    # Select days of the week
    Select_Days = models.CharField(max_length=10, choices=[
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday')
    ])
    
    # Period fields
    Roster_From_Period = models.DateField()  # Assuming this is a date field
    Roster_To_Period = models.DateField()    # Assuming this is also a date field
    
    # Foreign keys or related fields
    Department = models.ForeignKey('Department', on_delete=models.CASCADE)  # Assuming a Department model exists
    Groups = models.ForeignKey('Groups', on_delete=models.CASCADE)          # Assuming a Groups model exists
    Project = models.ForeignKey('Project', on_delete=models.CASCADE)        # Assuming a Project model exists
    Employee = models.ForeignKey('Employee', on_delete=models.CASCADE)      # Assuming an Employee model exists
    
    # Time-related fields
    In_Time = models.TimeField()         # Assuming these are time fields
    Out_Time = models.TimeField()
    Earliest_Clock_In_Time = models.TimeField()
    Last_Clock_Out_Time = models.TimeField()
    Auto_Clock_Out = models.BooleanField(default=False)  # Example, boolean to indicate if auto clock-out is enabled
    
    # Break and overtime fields
    Break_Time_Normal_Hours = models.DurationField()  # Example, stores duration of break
    OT_Break_Time_Normal_Hours = models.DurationField()
    OT_To_Only_Start_After = models.DurationField()
    OT_Break_Takes_Effect_After = models.DurationField()
    
    # Late clock-in and other related fields
    Late_In_From = models.TimeField()
    Apply_Days = models.CharField(max_length=100)  # Example, may want to improve this field
    
    # Pay and fine-related fields
    Basic_Pay = models.DecimalField(max_digits=10, decimal_places=2)
    Custom_Fine = models.DecimalField(max_digits=10, decimal_places=2)
    Fixed = models.BooleanField(default=False)
    
    # Overtime-related fields
    Common_OT = models.BooleanField(default=False)
    Hourly_OT = models.DecimalField(max_digits=10, decimal_places=2)  # Example, for storing hourly OT rates
    Total_OT_Hours = models.DecimalField(max_digits=5, decimal_places=2)
    Off_in_Lieu = models.BooleanField(default=False)
    
    # Additional fields related to OT, MOM Regulation, etc.
    Default = models.BooleanField(default=False)
    MOM_Regulation = models.BooleanField(default=False)  # Example, compliance with MOM regulations
    OT_By_Minutes = models.IntegerField()  # Assuming this field is an integer value
    OT_By_Block_30mins = models.BooleanField(default=False)  # Example, block OT by 30 mins
    OT_By_Block_15mins = models.BooleanField(default=False)  # Example, block OT by 15 mins

    def __str__(self):
        return self.Roster_Name


class Importanttimesheet(models.Model):
    TEMPLATE_CHOICES = [
        ('Template1', 'Template1'),
        ('Template2', 'Template2'),
        ('Template3', 'Template3'),
    ]

    FORMAT_CHOICES = [
        ('Excel', 'Excel'),
        ('CSV', 'CSV'),
    ]

    Template = models.CharField(max_length=10, choices=TEMPLATE_CHOICES)
    Format = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    Upload_Document = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return f"{self.Template} - {self.Format}"




class AddNewShifts(models.Model):
    Shift_ID = models.AutoField(primary_key=True)  
    Shift_Name = models.CharField(max_length=100)  
    Pick_Color = models.CharField(max_length=7) 
    In_Time = models.TimeField() 
    Out_Time = models.TimeField() 
    Earliest_Clock_In_Time = models.TimeField()  
    Last_Clock_Out_Time = models.TimeField()  
    Auto_Clock_Out = models.BooleanField(default=False) 
    Break_Time_Normal_Hours = models.DurationField()
    OT_Break_Time_Normal_Hours = models.DurationField()  
    OT_To_Only_Start_After = models.DurationField()  
    OT_Break_Takes_Effect_After = models.DurationField()
    Late_In_From = models.TimeField() 
    Apply_Days = models.CharField(max_length=100)  
    Basic_Pay = models.BooleanField(default=False) 
    Custom_Fine = models.BooleanField(default=False)  
    Fixed = models.BooleanField(default=False)
    Roster_Settings = models.BooleanField(default=False) 
    Amount = models.DecimalField(max_digits=10, decimal_places=2)  
    Postal_Code = models.CharField(max_length=10)  
    Supervisor_Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Shift_Name




class AddNewWorkflow(models.Model):
    Workflow_Type = models.CharField(max_length=150)
    Default = models.BooleanField(default=False)
    Specific = models.BooleanField(default=False)
    Workflow_Name = models.CharField(max_length=100)
    Departments = models.ForeignKey('Department', on_delete=models.CASCADE)
    Groups = models.ForeignKey('Groups', on_delete=models.CASCADE)
    Project = models.ForeignKey('Project', on_delete=models.CASCADE)
    Employee = models.ForeignKey('Employee', on_delete=models.CASCADE)        
    Levels = models.IntegerField()

    def __str__(self):
        return self.Workflow_Name
