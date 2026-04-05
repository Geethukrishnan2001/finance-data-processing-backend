from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User, Record
from .serializers import UserSerializer, RecordSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .permissions import RecordPermission

# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [RecordPermission]

@api_view(['GET'])
def dashboard(request):
    records = Record.objects.all()

    total_income = sum(r.amount for r in records if r.type == 'income')
    total_expense = sum(r.amount for r in records if r.type == 'expense')

    return Response({
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": total_income - total_expense
    })