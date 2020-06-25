import django
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bank.models import Branch, Department, Staff, Customer, Account, CheckingAccount, SavingsAccount, CustomerHasAccount, Loan, CustomerHasLoan, PayForLoan
from bank.serializers import BranchSerializer, DepartmentSerializer, StaffSerializer, CustomerSerializer, AccountSerializer, LoanSerializer
from django.http import Http404
from rest_framework.views import APIView

from django.http import HttpResponse
import json

# Create your views here.

# @api_view(['GET', 'POST'])
# def branch_list(request):
#     """
#     List all branches, or create a new branch.
#     """
#     if request.method == 'GET':
#         # branches = Branch.objects.all()
#         # serializer = BranchSerializer(branches, many=True)
#         # return Response(serializer.data)
#         response = HttpResponse(json.dumps({"key": "value", "key2": "value"}))
#         response["Access-Control-Allow-Origin"] = "*"
#         response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
#         response["Access-Control-Max-Age"] = "1000"
#         response["Access-Control-Allow-Headers"] = "*"
#         return response

#     elif request.method == 'POST':
#         serializer = BranchSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BranchList(APIView):
    """
    List all branches, or create a new branch.
    """
    def get(self, request, format=None):
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def department_list(request):
    """
    List all departments, or create a new department.
    """
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def staff_list(request):
    """
    List all staffs, or create a new staff.
    """
    if request.method == 'GET':
        staffs = Staff.objects.all()
        serializer = StaffSerializer(staffs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def customer_list(request):
    """
    List all customers, or create a new customer.
    """
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print('---------------------------------------------received POST method---------------------------------------------')
        serializer = CustomerSerializer(data=request.data)
        # request.data 是 dict
        if len(Customer.objects.filter(custom_id=request.data['custom_id'])) != 0:
            # 该客户号已存在
            # return Response({'msg': 'The custom_id already exists'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'errmsg': 'The custom_id already exists'})
        if serializer.is_valid():
            serializer.save()
            print('created')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print('---------------------------------------------over DELETE method---------------------------------------------')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        # 未修改身份证号：valid一下然后直接save
        # 修改了身份证号：若与其他人的重复则会报错：django.db.utils.IntegrityError
        # .clean_fields() 不会检测身份证号重复
        # .validate_unique() 可以检测unique约束，当与除自己外其他的元组有重复时会报错
        print('---------------------------------------------received PUT method---------------------------------------------')
        print('request.data = ' + str(request.data))
        
        resp = {}
        customer = Customer(**request.data) # 新建一个对象
        try:
            customer.clean_fields()
        except django.core.exceptions.ValidationError as e:
            print('clean_fields error:')
            print(e)
            resp = Response(e, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                customer.save()
            except django.db.utils.IntegrityError as e:
            # except django.core.exceptions.ValidationError as e:
                print('validate_unique error:')
                print(e)
                err = {'errmsg': 'err'}
                resp = Response(err, status=status.HTTP_400_BAD_REQUEST)
            else:   # no error
                resp = Response({'msg': 'Update successfully'}, status=status.HTTP_200_OK)

        print('---------------------------------------------over PUT method---------------------------------------------')
        return resp
    
    elif request.method == 'DELETE':
        print('---------------------------------------------received DELETE method---------------------------------------------')
        print('received data: ')
        print(request.data)
        print('type of received data: ' + str(type(request.data)))
        print('request.data.custom_id = ' + request.data['custom_id'])
        account_num = len(CustomerHasAccount.objects.filter(customer=request.data['id']))
        loan_num = len(CustomerHasLoan.objects.filter(customer=request.data['id']))
        if account_num > 0 or loan_num > 0:
            print('Cannot delete this customer because he has accounts or loans')
            return Response({'errmsg': 'Cannot delete this customer because he has accounts or loans'})
        cusDelete = Customer.objects.get(pk=request.data['id'])
        print('cusDelete: ' + str(cusDelete))
        cusDelete.delete()
        print('---------------------------------------------over DELETE method---------------------------------------------')
        return Response({'msg': 'Delete successful'})


@api_view(['GET', 'POST'])
def account_list(request):
    """
    List all accounts, or create a new account.
    """
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def loan_list(request):
    """
    List all loans, or create a new loan.
    """
    if request.method == 'GET':
        loans = Loan.objects.all()
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

