from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpRequest

from .models import List_Opps,Category, List_Opps_others, List_Opps_volon, List_Opps_program, List_Opps_intern, List_Opps_course, Training
from .serializer import OppsSerializer, OppsSerializerco, OppsSerializerin, OppsSerializerpr, OppsSerializervo, OppsSerializerot, OppsSerializertr


@api_view(['GET'])
def getRouts(request):
    return Response('opp')

@api_view(['GET'])
def getOpps(request):
    opps = List_Opps.objects.all()
    serializer = OppsSerializer(opps, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def opp_detaapi(request,  id):
    oppinfo1 = List_Opps.objects.get(pk=id)
    serializer = OppsSerializer(oppinfo1, many=False)
    return Response(serializer.data)



@api_view(['GET'])
def getOppsin(request):
    opps =  List_Opps_intern.objects.all()
    serializer = OppsSerializerin(opps, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOppsinid(request,  id):
    oppinfoid = List_Opps_intern.objects.get(pk=id)
    serializer = OppsSerializerin(oppinfoid, many=False)
    return Response(serializer.data)




@api_view(['GET'])
def getOppsco(request):
    opps =  List_Opps_course.objects.all()
    serializer = OppsSerializerco(opps, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOppscoid(request,  id):
    oppinfoid = List_Opps_course.objects.get(pk=id)
    serializer = OppsSerializerco(oppinfoid, many=False)
    return Response(serializer.data)




@api_view(['GET'])
def getOppstr(request):
    opps =  Training.objects.all()
    serializer = OppsSerializertr(opps, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOppstrid(request,  id):
    oppinfoid = Training.objects.get(pk=id)
    serializer = OppsSerializertr(oppinfoid, many=False)
    return Response(serializer.data)



@api_view(['GET'])
def getOppsvo(request):
    opps = List_Opps_volon.objects.all()
    serializer = OppsSerializervo(opps, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOppsvoid(request,  id):
    oppinfoid = List_Opps_volon.objects.get(pk=id)
    serializer = OppsSerializervo(oppinfoid, many=False)
    return Response(serializer.data)



@api_view(['GET'])
def getOppspr(request):
    opps = List_Opps_program.objects.all()
    serializer = OppsSerializerpr(opps, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOppsprid(request,  id):
    oppinfoid = List_Opps_program.objects.get(pk=id)
    serializer = OppsSerializerpr(oppinfoid, many=False)
    return Response(serializer.data)



@api_view(['GET'])
def getOppsot(request):
    opps = List_Opps_others.objects.all()
    serializer = OppsSerializerot(opps, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOppsotid(request,  id):
    oppinfoid = List_Opps_others.objects.get(pk=id)
    serializer = OppsSerializerot(oppinfoid, many=False)
    return Response(serializer.data)






def index(request):
    return render(request, "web/index1.html")

def opp(request):
    opps = List_Opps.objects.all()
    cate = Category.objects.all()
    return render(request, "web/opp.html",{
        "opps" : opps,
        "cates":cate,
    })

def new_opp(request):
    opps = List_Opps.objects.all()
    cate = Category.objects.all()
    return render(request, "web/thenewopp.html",{
        "opps" : opps,
        "cates":cate,
    })


def opp_deta(request,  id):
    oppinfo = List_Opps.objects.get(pk=id)
    return render(request, 'web/opp_deta.html', {
        "opp_deta":oppinfo
    })

def displaycate(request):
    if request.method == "POST":
        catefromform = request.POST['category']
        category = Category.objects.get(cate_name=catefromform )
        opps = List_Opps.objects.filter(category = category)
        cate = Category.objects.all()
        return render(request, "web/opp.html",{
            "opps" : opps,
            "cates":cate,
        })

def sub(request):
    return render(request, "web/sub.html")


def search(request):
    if request.method == 'POST':
        cate = Category.objects.all()
        searched = request.POST['searched']
        opps = List_Opps.objects.filter(title__contains=searched)
        return render(request, "web/entry.html", {
            "searched" : searched,
            "opps1":opps,
            "cates":cate,
        })
    else:
        return render(request, "web/entry.html")
    

def theopp(request):
    return render(request, 'web/opp.html')




#login
# views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'message': 'User not found'}, status=status.HTTP_401_UNAUTHORIZED)
                













