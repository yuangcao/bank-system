from rest_framework import serializers
from bank.models import Branch, Department, Staff, Customer, Account, CheckingAccount, SavingsAccount, CustomerHasAccount, Loan, CustomerHasLoan, PayForLoan

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['branch_name', 'branch_assets', 'branch_city']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['department_id', 'department_name', 'department_type', 'manager_id', 'branch_branch_name']


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['staff_id', 'staff_name', 'staff_phone', 'staff_address', 'staff_starttime', 'staff_ismanager', 'department_department']  # 注意 department_department 这里没有 id


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['custom_id', 'custom_name', 'custom_phone', 'custom_address', 'contact_name', 'contact_phone', 'contact_email', 'contact_custom_relation']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['account_id', 'account_balance', 'account_opendate', 'account_type', 'staff_staff', 'branch_branch_name']


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['loan_id', 'loan_money', 'loan_state', 'staff_staff', 'branch_branch_name']

