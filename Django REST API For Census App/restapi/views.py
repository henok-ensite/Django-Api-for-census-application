# import http
# from math import e
import random
import string
# from urllib import request
# from xml.dom.minidom import CharacterData
# from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import Datacollectors, Kahnat, Memenan
from django.utils.timezone import now
from rest_framework.permissions import IsAuthenticated


class Test(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        try:
            queryset = Memenan.objects.all()[:4]
            serializer = MemenanSerializer(queryset,many=True)
            data={
                'issuccess':True,
                'data':serializer.data
                }
            return Response(data)
        except:
            data={
                'issuccess':False,
                'data':serializer.data
                }
            return Response(data)
            
class Auth(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):    
        try:
            data={
                'issuccess':True,
                }
            return Response(data)
        except Exception as e:
            data={
                'issuccess':False,
                'data':"Some thing went wrong, Please try again",
                'error':str(e)
                }
            return Response(data)

class CustomeAuth():
    
    def auth(self,request,*args,**kwargs):
        if not request.headers.__contains__ ('Authorization') and not request.data.__contains__('apptoken'): 
            data={
                'issuccess':False,
                'data':'not auth1'
                }
            return Response(data)
        elif request.data.__contains__('apptoken'):
            if request.data['apptoken']!=2:
                data={
                    'issuccess':False,
                    'data':'not auth2'
                    }
                return Response(data)
            else:
                data={
                    'issuccess':True,
                    'data':'pass'
                    }
                return Response(data)
        elif request.headers.__contains__ ('Authorization'):
                data={
                    'issuccess':True,
                    'data':'not auth2'
                    }
                return Response(data)

class LoginAdmin(APIView):
    
    def post(self,request,*args,**kwargs):
        try:
            serializer= AdminSerializer(data=request.data)
            print(serializer.is_valid());
            phonenum=serializer.data["phonenum"]
            password=serializer.data["password"]
            print(serializer.data)
            # it is better to do the .count() on the next line like numrows=numrows.count() 
            # and rename the numrows query var with qs
            numrows=Admin.objects.filter(password=password,phonenum=phonenum).count()
            print(numrows);
        except:
            data={
                'issuccess':False,
                'data':'Server Error, Please Try Again',
                }
            return Response(data)

        if numrows==1:
        #idont need this qs to query again rather use numrows.first or the renamed qs on the top
            qs=Admin.objects.filter(phonenum=phonenum).first()
            serializer=AdminSerializer(qs)
            data={
                'issuccess':True,
                'data':serializer.data
                }
            return Response(data)
        else:
            data={
                'issuccess':False,
                'data':'Wrong Email Or Password',
                }
            return Response(data)

class CreateDatacollectors(APIView):

    def post(self,request,*args,**kwargs):
        generatedpassword=[]
        characters= list(string.digits)
        random.shuffle(characters)
        for i in range (6):
            generatedpassword.append(random.choice(characters))
        random.shuffle(generatedpassword)
        generatedpassword="".join(generatedpassword)
        print(generatedpassword)
        try:
            request.data["password"]=generatedpassword
            serializer= DatacollectorsSerializer(data=request.data)
            print(serializer.is_valid());
        except Exception as e:
            #print(serializer.is_valid());
            data={
                'issuccess':False,
                'data':'Server Error, Please Try Again',
                'serializer':serializer.errors,
                'exception':str(e)
                }
            return Response(data)
        if serializer.is_valid():
            try:
                serializer.save()
                data={
                'issuccess':True,
                'data':'Data collector accounnt created successfully',
                }
                return Response(data) 
            except Exception as e:
                data={
                'issuccess':False,
                'data':'Server Error, Please Try Again',
                'exception':str(e)
                }
                return Response(data)
        phonenumdup=''   
        try: 
            serializer.errors['phonenum'][0]
            phonenumdup=serializer.errors['phonenum'][0].replace('phonenum','phone number')
            phonenumdup=phonenumdup.replace('datacollectors','Data Collector')
        except:
            phonenumdup=None
        data={
                'issuccess':False,
                'data':'Invalid data in your request, PleaseTry Again',
                'phonenum dup':phonenumdup,
                'error':serializer.errors
                }
        return Response(data)

class LoginDatacollectors(APIView):

    def post(self,request,*args,**kwargs):
        try:
            serializer= DatacollectorsSerializer(data=request.data)
            print(serializer.is_valid());
            phonenum=serializer.data["phonenum"]
            password=serializer.data["password"]
            print(serializer.data)
            # it is better to do the .count() on the next line like numrows=numrows.count() 
            # and rename the numrows query var with qs
            numrows=Datacollectors.objects.filter(password=password,phonenum=phonenum).count()
            print(numrows);
        except:
            data={
                'issuccess':False,
                'data':'Server Error, Please Try Again',
                }
            return Response(data)

        if numrows==1:
        #idont need this qs to query again rather use numrows.first or the renamed qs on the top
            qs=Datacollectors.objects.filter(phonenum=phonenum).first()
            serializer=DatacollectorsSerializer(qs)
            data={
                'issuccess':True,
                'data':serializer.data
                }
            return Response(data)
        else:
            data={
                'issuccess':False,
                'data':'Wrong Email Or Password',
                }
            return Response(data)

class GetDatacollectors(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        try:
            serializer= DatacollectorsSerializer(data=request.data)
            id=serializer.initial_data["id"]
            numrows=Datacollectors.objects.filter(id=id).count()
        except:
            data={
                'issuccess':False,
                'data':'Some Error, Please Try Again',
                }
            return Response(data)

        if numrows==1:
            qs=Datacollectors.objects.filter(id=id).first()
            serializer=DatacollectorsSerializer(qs)
            data={
                'issuccess':True,
                'data':serializer.data
                }
            return Response(data)
        else:
            data={
                'issuccess':False,
                'data':'User Data Not Found'
                }
            return Response(data)

class GetAllDatacollectors(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        try:
            pagination_id=request.data['id']
            is_previous=request.data['is_previous']
            if pagination_id==0:
                pagination_id=Datacollectors.objects.first().__dict__['id']
            if (is_previous):
                print(f'is p true pid {pagination_id}')
                qs=Datacollectors.objects.filter(id__lt=pagination_id).order_by('-id')[:10][::-1]
            else:
                qs=Datacollectors.objects.filter(id__gte=pagination_id).order_by('id')[:10]
            
            serializer=DatacollectorsSerializer(qs,many=True)

            data={
                'issuccess':True,
                'data':serializer.data,

                }
            return Response(data)
        except Exception as e:
            print(e);
            data={
                'issuccess':False,
                'data':'Some Error, Please Try Again',
                'error':str(e)
                }
            return Response(data)

class GetAllDatacollectorsByFilter(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        try:
            serializer= DatacollectorsSerializer(data=request.data)
            filterdata=serializer.initial_data
            pagination_id=request.data['id']
            is_previous=request.data['is_previous']
            filterdata={k:v for k,v in filterdata.items() 
            if v is not None and v!='' and k!='id' and k!='is_previous'}
            if pagination_id==0:
                pagination_id=Datacollectors.objects.first().__dict__['id']
            print('filter data')
            print(filterdata)
            if (is_previous):
                print(f'is p true pid {pagination_id}')
                qs=Datacollectors.objects.filter(id__lt=pagination_id,**filterdata).order_by('-id')[:10][::-1]
            else:
                qs=Datacollectors.objects.filter(id__gte=pagination_id,**filterdata).order_by('id')[:10]
            
            serializer=DatacollectorsSerializer(qs,many=True)

            data={

                'issuccess':True,
                'data':serializer.data,

                }
            return Response(data)
        except Exception as e:
            print(e)
            data={
                'issuccess':False,
                'data':'Some Error, Please Try Again',
                }
            return Response(data)

class UpdateDatacollectors(APIView):
    
    def post(self,request,*args,**kwargs):
        
        if CustomeAuth.auth(self,request,*args,**kwargs).__dict__['data']['issuccess']:
            try:
                serializer= DatacollectorsUpdateSerializer(data=request.data)
                print(serializer.is_valid())
                id=serializer.initial_data["id"]
                checking=serializer.initial_data["checking"]
                numrows=Datacollectors.objects.filter(id=id,password=checking).count()
                updatedata=serializer.initial_data
                updatedata={k:v for k,v in updatedata.items() 
                if v is not None and k!='checking' and k!='id' and k!='apptoken'}
                print(serializer.initial_data)
                print(updatedata)
                print(numrows) 
            except:
                data={
                    'issuccess':False,
                    'data':'Some fields are required',
                    # 'error':serializer.errors
                    }
                return Response(data)
            if numrows==1:
                
                try:
                    print("dddddddddddddddddd"+str(now()))
                    Datacollectors.objects.filter(id=id).update(updatedat=now(),**updatedata)
                    qs=Datacollectors.objects.filter(id=id).first()
                    serializerr=DatacollectorsSerializer(qs)
                    data={
                        'issuccess':True,
                        'data':serializerr.data
                        }
                    return Response(data)
                except Exception as e:
                    phonenumdup=''   
                    try: 
                        serializer.errors['phonenum'][0]
                        phonenumdup=serializer.errors['phonenum'][0].replace('phonenum','phone number')
                        phonenumdup=phonenumdup.replace('datacollectors','Data Collector')
                    except:
                        phonenumdup=None
                    data={
                            'issuccess':False,
                            'data':'Invalid data in your request, PleaseTry Again',
                            'phonenum dup':phonenumdup,
                            'error':serializer.errors,
                            'exception':str(e)
                            }
                    return Response(data)
    
            else:
                print(numrows)
                data={
                    'issuccess':False,
                    'data':'User Data Not Found'
                    }
                return Response(data)
        else:
            data={
                    'issuccess':False,
                    'data':'Not Auth'
                    }
            return Response(data)

class UpdateDatacollectorsByAdmin(APIView):
    
    def post(self,request,*args,**kwargs):
        
        if CustomeAuth.auth(self,request,*args,**kwargs).__dict__['data']['issuccess']:
            try:
                try:
                    serializer= DatacollectorsUpdateSerializer(data=request.data)
                    print(serializer.is_valid())
                    id=serializer.initial_data["id"]
                    updatedata=serializer.initial_data
                    updatedata={k:v for k,v in updatedata.items() 
                    if v is not None and k!='id'}
                    print(serializer.initial_data)
                    print(updatedata)
                    print("dddddddddddddddddd"+str(now()))
                    Datacollectors.objects.filter(id=id).update(updatedat=now(),**updatedata)
                    qs=Datacollectors.objects.filter(id=id).first()
                    serializerr=DatacollectorsSerializer(qs)
                    data={
                        'issuccess':True,
                        'data':serializerr.data
                        }
                    return Response(data)
                except Exception as e:
                    phonenumdup=''   
                    try: 
                        serializer.errors['phonenum'][0]
                        phonenumdup=serializer.errors['phonenum'][0].replace('phonenum','phone number')
                        phonenumdup=phonenumdup.replace('datacollectors','Data Collector')
                    except:
                        phonenumdup=None
                    data={
                            'issuccess':False,
                            'data':'Invalid data in your request, PleaseTry Again',
                            'phonenum dup':phonenumdup,
                            'error':serializer.errors,
                            'exception':str(e)
                            }
                    return Response(data)
            except:
                data={
                    'issuccess':False,
                    'data':'Something went wrong, PleaseTry Again',
                    # 'error':serializer.errors
                    }
                return Response(data)
        else:
            data={
                    'issuccess':False,
                    'data':'Not Auth'
                    }
            return Response(data)

class CreateMemenan(APIView):
    def post(self ,request,*args,**kwargs):
                    
        try:
            fammembervalid=True
            request_data=request.data
            fammember=request_data["memenan"][0]["fammember"]
            fammemberlen=len(fammember)
            i=1
            print("bf while")
            print(len(fammember))
            while i<=fammemberlen and fammembervalid:
                print("in while##################")
                print(fammemberlen)
                print(i)
                
                serializerfammember=FammemberSerializer(data=fammember[i-1])
                print(fammember[i-1])
    
                if not serializerfammember.is_valid():
                    print("****************breaked************")
                    fammembervalid=False
                    break
                print("serializerfam data")
                print(serializerfammember.validated_data)
                i=i+1
        except:
            print("error parsing")
            data={
                'issuccess':False,
                'data':'Invalid data in your request, PleaseTry Again',
                }
            return Response(data)

        if fammembervalid:
            try:

                serializer= MemenanSerializer(data=request_data["memenan"][0])
                print(request_data["memenan"][0]);
                print(len(fammember));
                print("is valid")
                print(serializer.is_valid())
                print(serializer.errors)

                if serializer.is_valid():
                    serializer.save()
                    datamemen={
                            'issuccess':True,
                            'data':'Memen Data Created Successfully',
                            'errors':serializer.errors
                            }
                    print("qsssssssssssssssss" )
                    print(serializer.data['id'])
                    parentid= serializer.data['id']
                    print("parenttttt id ")
                    print(parentid)
                else:
                    data={
                        'issuccess':False,
                        'data':'Memen Data error, PleaseTry Again',
                        'errors':serializer.errors
                        }
                    return Response(data)
                fammemberlen=len(fammember)
                if fammemberlen>0:
                    print("lennnn**********************: ")
                    print(fammemberlen)

                    try:
                        count=1
                        print("bf while")
                        print(fammemberlen)
                        while count<=fammemberlen:
                            print("in while##################")
                            print(fammemberlen)
                            print(count)
                            serializerfammember=FammemberSerializer(data=fammember[count-1])
                            print(fammember[count-1])
                            print(serializerfammember.is_valid())
                            print("qffffffffffffffffffff")
                            serializerfammember.validated_data['parentid']=parentid
                            print(serializerfammember.validated_data['parentid'])
                            print("serializerfam data")
                            print(serializerfammember.validated_data)
                            serializerfammember.save()
                            print("in while*****************")
                            count=count+1
                    except Exception as e:
                        data={
                            'issuccess':False,
                            "data":"Fammember registration failed due to server error",
                            "exception":str(e),
                            "memen res":datamemen,
                            "fammember error":serializerfammember.errors,
                            "serialzer fammember":serializerfammember.data
                        }
                        return Response(data)
                    data={
                    'issuccess':True,
                    'data':f'Registered with {fammemberlen} fammember',
                    'errors':serializerfammember.errors,
                    'obj':Fammember.objects.all().count(),
                    "fammembers":fammember
                    }
                    return Response(data)
                data={
                    'issuccess':True,
                    'data':'Registered with no fammember',
                    #'errors':serializer.errors
                    "fammembers":fammember
                    }
                print(len(fammember))
                return Response(data)

            except:
                print("bottom")
                #print(serializerfammember.is_valid())
                #print(serializerfammember.data)
                data={
                    'issuccess':False,
                    'data':'Server Error, PleaseTry Again',
                    #'errors':serializer.errors,
                    #'famerrors':serializerfammember.errors
                    }
                return Response(data)
        data={
            'issuccess':False,
            'data':'Fammember data error, PleaseTry Again',
            #'errors':serializer.errors,
            #'famerrors':serializerfammember.errors
            }
        return Response(data)

class UpdateMemenan(APIView):

   def post(self,request,*args,**kwargs):

    if CustomeAuth.auth(self,request,*args,**kwargs).__dict__['data']['issuccess']:
        try:
            serializer= MemenanSerializer(data=request.data)
            id=serializer.initial_data["id"]
            sothertitle=serializer.initial_data["sothertitle"]
            sfname=serializer.initial_data["sfname"]
            othertitle=serializer.initial_data["othertitle"]
            if sothertitle=='':
                sothertitle=None
            if sfname=='':
                sfname=None
            if othertitle=='':
                othertitle=None
            numrows=Memenan.objects.filter(id=id).count()
            updatedata=serializer.initial_data
            updatedata={k:v for k,v in updatedata.items() 
            if v is not None and v!=''
                and k!='othertitle'
                and k!='sothertitle'
                and k!='sfname'
                and k!='apptoken'
                and k!='id'}
            print(serializer.initial_data)
            print(updatedata)
            print(numrows) 
        except Exception as e:
            data={
                'issuccess':False,
                'data':'Invalid data in your request, PleaseTry Again',
                'error':str(e)
                }
            return Response(data)

        if numrows==1:
            try:
                print("dddddddddddddddddd"+str(now()))
                Memenan.objects.filter(id=id).update(updatedat=now(),othertitle=othertitle,
                sothertitle=sothertitle,sfname=sfname,**updatedata)
                qs=Memenan.objects.filter(id=id).first()
                serializer=MemenanSerializer(qs)
                data={
                    'issuccess':True,
                    'data':serializer.data
                    }
                return Response(data)
            except Exception as e:
                phonenumdup=''
                print(serializer.is_valid()) 
                print(e)  
                try: 
                    serializer.errors['phonenum'][0]
                    phonenumdup=serializer.errors['phonenum'][0].replace('phonenum','phone number')
                    phonenumdup=phonenumdup.replace('datacollectors','Data Collector')
                except Exception as e:
                    phonenumdup=None
                    data={
                            'issuccess':False,
                            'data':'Invalid data in your request, PleaseTry Again'+str(e),
                            'phonenum dup':phonenumdup,
                            'error':serializer.errors
                            }
                return Response(data)
        else:
            print(numrows)
            data={
                'issuccess':False,
                'data':'User Data Not Found'
                }
            return Response(data)
    else:
        data={
            'issuccess':False,
            'data':'Not Auth'
            }
        return Response(data)



class CreateKahnat(APIView):
    def post(self ,request,*args,**kwargs):
                    
        try:
            fammembervalid=True
            request_data=request.data
            fammember=request_data["kahnat"][0]["fammember"]
            fammemberlen=len(fammember)
            i=1
            print("bf while")
            print(len(fammember))
            while i<=fammemberlen and fammembervalid:
                print("in while##################")
                print(fammemberlen)
                print(i)
                
                serializerfammember=FammemberSerializer(data=fammember[i-1])
                print(fammember[i-1])
    
                if not serializerfammember.is_valid():
                    print("****************breaked************")
                    fammembervalid=False
                    break
                print("serializerfam data")
                print(serializerfammember.validated_data)
                i=i+1
        except:
            print("error parsing")
            data={
                'issuccess':False,
                'data':'Invalid data in your request, PleaseTry Again',
                }
            return Response(data)

        if fammembervalid:
            try:

                serializer= KahnatSerializer(data=request_data["kahnat"][0])
                print(request_data["kahnat"][0]);
                print(len(fammember));
                print("is valid")
                print(serializer.is_valid())
                print(serializer.errors)

                if serializer.is_valid():
                    serializer.save()
                    datakahn={
                            'issuccess':True,
                            'data':'Kahn Data Created Successfully',
                            'errors':serializer.errors
                            }
                    print("qsssssssssssssssss" )
                    print(serializer.data['id'])
                    parentid= serializer.data['id']
                    print("parenttttt id ")
                    print(parentid)
                else:
                    data={
                        'issuccess':False,
                        'data':'Kahn Data error, PleaseTry Again',
                        'errors':serializer.errors
                        }
                    return Response(data)
                fammemberlen=len(fammember)
                if fammemberlen>0:
                    print("lennnn**********************: ")
                    print(fammemberlen)

                    try:
                        count=1
                        print("bf while")
                        print(fammemberlen)
                        while count<=fammemberlen:
                            print("in while##################")
                            print(fammemberlen)
                            print(count)
                            serializerfammember=FammemberSerializer(data=fammember[count-1])
                            print(fammember[count-1])
                            print(serializerfammember.is_valid())
                            print("qffffffffffffffffffff")
                            serializerfammember.validated_data['parentid']=parentid
                            print(serializerfammember.validated_data['parentid'])
                            print("serializerfam data")
                            print(serializerfammember.validated_data)
                            serializerfammember.save()
                            print("in while*****************")
                            count=count+1
                    except Exception as e:
                        data={
                            'issuccess':False,
                            "data":"Fammember registration failed due to server error",
                            "exception":str(e),
                            "kahn res":datakahn,
                            "fammember error":serializerfammember.errors,
                            "serialzer fammember":serializerfammember.data
                        }
                        return Response(data)
                    data={
                    'issuccess':True,
                    'data':f'Registered with {fammemberlen} fammember',
                    'errors':serializerfammember.errors,
                    'obj':Fammember.objects.all().count(),
                    "fammembers":fammember
                    }
                    return Response(data)
                data={
                    'issuccess':True,
                    'data':'Registered with no fammember',
                    #'errors':serializer.errors
                    "fammembers":fammember
                    }
                print(len(fammember))
                return Response(data)

            except Exception as e:
                print("bottom")
                #print(serializerfammember.is_valid())
                #print(serializerfammember.data)
                data={
                    'issuccess':False,
                    'data':'Server Error, PleaseTry Again',
                    'exception':str(e)
                    #'errors':serializer.errors,
                    #'famerrors':serializerfammember.errors
                    }
                return Response(data)
        data={
            'issuccess':False,
            'data':'Fammember data error, PleaseTry Again',
            #'errors':serializer.errors,
            'famerrors':serializerfammember.errors
            }
        return Response(data)

class UpdateKahnat(APIView):

    def post(self,request,*args,**kwargs):
        if CustomeAuth.auth(self,request,*args,**kwargs).__dict__['data']['issuccess']:
            try:
                serializer= KahnatSerializer(data=request.data)
                id=serializer.initial_data["id"]
                sothertitle=serializer.initial_data["sothertitle"]
                sfname=serializer.initial_data["sfname"]
                othertitle=serializer.initial_data["othertitle"]
                yenshaljochnum=serializer.initial_data["yenshaljochnum"]
                numrows=Kahnat.objects.filter(id=id).count()
                updatedata=serializer.initial_data
                updatedata={k:v for k,v in updatedata.items() 
                if v is not None and v!=''
                    and k!='othertitle'
                    and k!='sothertitle'
                    and k!='yenshaljochnum'
                    and k!='sfname'
                    and k!='apptoken'
                    and k!='id'}
                print(serializer.initial_data)
                print(updatedata)
                print(numrows) 
            except Exception as e:
                #print(serializer.is_valid())
                data={
                    'issuccess':False,
                    'data':'Invalid data in your request, PleaseTry Again',
                    'error':str(e)
                    }
                return Response(data)
            if numrows==1:
                if sothertitle=='':
                    sothertitle=None
                if sfname=='':
                    sfname=None
                if othertitle=='':
                    othertitle=None
                if yenshaljochnum=='':
                    yenshaljochnum=None
                try:
                    print("date time now "+str(now()))
                    Kahnat.objects.filter(id=id).update(updatedat=now(),othertitle=othertitle,
                    sothertitle=sothertitle,sfname=sfname,yenshaljochnum=yenshaljochnum,**updatedata)
                    qs=Kahnat.objects.filter(id=id).first()
                    serializer=KahnatSerializer(qs)
                    data={
                        'issuccess':True,
                        'data':serializer.data
                        }
                    return Response(data)
                except Exception as e:
                    phonenumdup=''
                    print(serializer.is_valid()) 
                    print(e)
                    ee=" got u "+str(e)
                    try: 
                        serializer.errors['phonenum'][0]
                        phonenumdup=serializer.errors['phonenum'][0].replace('phonenum','phone number')
                        phonenumdup=phonenumdup.replace('datacollectors','Data Collector')
                        data={
                                'issuccess':False,
                                'data':"error related to phone number error top try " + ee,
                                'phonenum dup':phonenumdup,
                                }
                        return Response(data)
                    except Exception as e:
                        phonenumdup=None
                        data={
                                'issuccess':False,
                                'data':'error top try '+ee +" error bottom try "+str(e),
                                'phonenum dup':phonenumdup,
                                'error':serializer.errors
                                }
                        return Response(data)
            else:
                print(numrows)
                data={
                    'issuccess':False,
                    'data':'User Data Not Found'
                    }
                return Response(data)
        else:
            data={
                    'issuccess':False,
                    'data':'Not Auth'
                    }
            return Response(data)

class UpdateFammember(APIView):
    
    def post(self,request,*args,**kwargs):
        if CustomeAuth.auth(self,request,*args,**kwargs).__dict__['data']['issuccess']:
            try:
                serializer= FammemberSerializer(data=request.data)
                print(serializer.is_valid())
                id=serializer.initial_data["id"]
                numrows=Fammember.objects.filter(id=id).count()
                updatedata=serializer.initial_data
                updatedata={k:v for k,v in updatedata.items() 
                if v is not None and k!='id' and k!='apptoken'}
                print(serializer.initial_data)
                print(updatedata)
                print(numrows) 
            except:
               # print(serializer.is_valid())
                data={
                    'issuccess':False,
                    'data':'Invalid data in your request, PleaseTry Again',
                #    'error':serializer.errors
                    }
                return Response(data)
            if numrows==1:
                
                try:
                    print("dddddddddddddddddd"+str(now()))
                    Fammember.objects.filter(id=id).update(updatedat=now(),**updatedata)
                    qs=Fammember.objects.filter(id=id).first()
                    serializerr=FammemberSerializer(qs)
                    data={
                        'issuccess':True,
                        'data':serializerr.data
                        }
                    return Response(data)
                except Exception as e:
                    phonenumdup=''   
                    try: 
                        serializer.errors['phonenum'][0]
                        phonenumdup=serializer.errors['phonenum'][0].replace('phonenum','phone number')
                        phonenumdup=phonenumdup.replace('datacollectors','Data Collector')
                    except:
                            phonenumdup=None
                    data={
                        'issuccess':False,
                        'data':'Invalid data in your request, PleaseTry Again',
                        'phonenum dup':phonenumdup,
                        'error':serializer.errors,
                        'exception':str(e)
                        }
                    return Response(data)
    
            else:
                print(numrows)
                data={
                    'issuccess':False,
                    'data':'User Data Not Found'
                    }
                return Response(data)
        else:
            data={
                    'issuccess':False,
                    'data':'Not Auth'
                    }
            return Response(data)

class FammemberAddKahnat(APIView):
    def post(self ,request,*args,**kwargs):
                    
        try:
            fammembervalid=True
            request_data=request.data
            fammember=request_data["kahnat"][0]["fammember"]
            familynum=request_data["kahnat"][0]["familynum"]
            id=request_data["kahnat"][0]["id"]
            fammemberlen=len(fammember)
            i=1
            print("bf while")
            print(len(fammember))
            while i<=fammemberlen and fammembervalid:
                print("in while##################")
                print(fammemberlen)
                print(i)
                serializerfammember=FammemberSerializer(data=fammember[i-1])
                print(fammember[i-1])
    
                if not serializerfammember.is_valid():
                    print("****************breaked************")
                    fammembervalid=False
                    break
                print("serializerfam data")
                print(serializerfammember.validated_data)
                i=i+1
        except Exception as e:
            print("error parsing")
            data={
                'issuccess':False,
                'data':'Invalid data in your request, PleaseTry Again ' + str(e),
                }
            return Response(data)

        if fammembervalid:

            try:
                Kahnat.objects.filter(id=id).update(updatedat=now(),familynum=familynum,)
                fammemberlen=len(fammember)
                if fammemberlen>0:
                    print("lennnn**********************: ")
                    print(fammemberlen)

                    try:
                        count=1
                        print("bf while")
                        print(fammemberlen)
                        while count<=fammemberlen:
                            print("in while##################")
                            print(fammemberlen)
                            print(count)
                            serializerfammember=FammemberSerializer(data=fammember[count-1])
                            print(fammember[count-1])
                            print(serializerfammember.is_valid())
                            print("serializerfam data")
                            print(serializerfammember.validated_data)
                            serializerfammember.save()
                            print("in while*****************")
                            count=count+1
                    except:
                        data={
                            'issuccess':False,
                            "data":"Fammember registration failed due to server error",
                            "fammember error":serializerfammember.errors,
                            "serialzer fammember":serializerfammember.data
                        }
                        return Response(data)
                    data={
                    'issuccess':True,
                    'data':f'Registered with {fammemberlen} fammember',
                    'errors':serializerfammember.errors,
                    'obj':Fammember.objects.all().count(),
                    "fammembers":fammember
                    }
                    return Response(data)
                data={
                    'issuccess':True,
                    'data':'Registered with no fammember',
                    #'errors':serializer.errors
                    "fammembers":fammember
                    }
                print(len(fammember))
                return Response(data)

            except:
                print("bottom")
                #print(serializerfammember.is_valid())
                #print(serializerfammember.data)
                data={
                    'issuccess':False,
                    'data':'Server Error, PleaseTry Again',
                    #'errors':serializer.errors,
                    #'famerrors':serializerfammember.errors
                    }
                return Response(data)
        data={
            'issuccess':False,
            'data':'Fammember data error, PleaseTry Again',
            #'errors':serializer.errors,
            'famerrors':serializerfammember.errors
            }
        return Response(data)


class FammemberAddMemenan(APIView):
    def post(self ,request,*args,**kwargs):
                    
        try:
            fammembervalid=True
            request_data=request.data
            fammember=request_data["memenan"][0]["fammember"]
            familynum=request_data["memenan"][0]["familynum"]
            id=request_data["memenan"][0]["id"]
            fammemberlen=len(fammember)
            i=1
            print("bf while")
            print(len(fammember))
            while i<=fammemberlen and fammembervalid:
                print("in while##################")
                print(fammemberlen)
                print(i)
                serializerfammember=FammemberSerializer(data=fammember[i-1])
                print(fammember[i-1])
    
                if not serializerfammember.is_valid():
                    print("****************breaked************")
                    fammembervalid=False
                    break
                print("serializerfam data")
                print(serializerfammember.validated_data)
                i=i+1
        except:
            print("error parsing")
            data={
                'issuccess':False,
                'data':'Invalid data in your request, PleaseTry Again',
                }
            return Response(data)

        if fammembervalid:

            try:
                Memenan.objects.filter(id=id).update(updatedat=now(),familynum=familynum,)
                fammemberlen=len(fammember)
                if fammemberlen>0:
                    print("lennnn**********************: ")
                    print(fammemberlen)

                    try:
                        count=1
                        print("bf while")
                        print(fammemberlen)
                        while count<=fammemberlen:
                            print("in while##################")
                            print(fammemberlen)
                            print(count)
                            serializerfammember=FammemberSerializer(data=fammember[count-1])
                            print(fammember[count-1])
                            print(serializerfammember.is_valid())
                            print("serializerfam data")
                            print(serializerfammember.validated_data)
                            serializerfammember.save()
                            print("in while*****************")
                            count=count+1
                    except:
                        data={
                            'issuccess':False,
                            "data":"Fammember registration failed due to server error",
                            "fammember error":serializerfammember.errors,
                            "serialzer fammember":serializerfammember.data
                        }
                        return Response(data)
                    data={
                    'issuccess':True,
                    'data':f'Registered with {fammemberlen} fammember',
                    'errors':serializerfammember.errors,
                    'obj':Fammember.objects.all().count(),
                    "fammembers":fammember
                    }
                    return Response(data)
                data={
                    'issuccess':True,
                    'data':'Registered with no fammember',
                    #'errors':serializer.errors
                    "fammembers":fammember
                    }
                print(len(fammember))
                return Response(data)

            except:
                print("bottom")
                #print(serializerfammember.is_valid())
                #print(serializerfammember.data)
                data={
                    'issuccess':False,
                    'data':'Server Error, PleaseTry Again',
                    #'errors':serializer.errors,
                    #'famerrors':serializerfammember.errors
                    }
                return Response(data)
        data={
            'issuccess':False,
            'data':'Fammember data error, PleaseTry Again',
            #'errors':serializer.errors,
            'famerrors':serializerfammember.errors
            }
        return Response(data)


class GetMemen(APIView):

    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        try:
            serializer= MemenanSerializer(data=request.data)
            id=serializer.initial_data["id"]
            numrows=Memenan.objects.filter(id=id).count()
        except:
            data={
                'issuccess':False,
                'data':'Some Error, Please Try Again',
                }
            return Response(data)

        if numrows==1:
            qs=Memenan.objects.filter(id=id).first()
            serializer=MemenanSerializer(qs)
            data={
                'issuccess':True,
                'data':serializer.data
                }
            return Response(data)
        else:
            data={
                'issuccess':False,
                'data':'User Data Not Found'
                }
            return Response(data)


class GetKahn(APIView):

    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        try:
            serializer= KahnatSerializer(data=request.data)
            id=serializer.initial_data["id"]
            numrows=Kahnat.objects.filter(id=id).count()
        except:
            data={
                'issuccess':False,
                'data':'Some Error, Please Try Again',
                }
            return Response(data)

        if numrows==1:
            qs=Kahnat.objects.filter(id=id).first()
            serializer=KahnatSerializer(qs)
            data={
                'issuccess':True,
                'data':serializer.data
                }
            return Response(data)
        else:
            data={
                'issuccess':False,
                'data':'User Data Not Found'
                }
            return Response(data)


class GetFammember(APIView):
    def post(self,request,*args,**kwargs):
        try:
            serializer= FammemberSerializer(data=request.data)
            # print(serializer.is_valid());
            id=serializer.initial_data["id"]
            # print(serializer.data)
            numrows=Fammember.objects.filter(id=id).count()
            print(numrows);
        except:
            data={
                'issuccess':False,
                'data':'Some Error, Please Try Again',
                # 'er':serializer.errors
                }
            return Response(data)

        if numrows==1:
            qs=Fammember.objects.filter(id=id).first()
            serializer=FammemberSerializer(qs)
            data={
                'issuccess':True,
                'data':serializer.data
                }
            return Response(data)
        else:
            data={
                'issuccess':False,
                'data':'User Data Not Found'
                }
            return Response(data)

class GetAllMemenanByDC(APIView):
    def post(self,request,*args,**kwargs):
        try:
            dcid=request.data["dcid"]
            pagination_id=request.data['id']
            if pagination_id==0:
                pagination_id=Memenan.objects.last().__dict__['id']
            qs=Memenan.objects.filter(id__lte=pagination_id,datacollectorid=dcid).order_by('-id')[:4]
            serializer=MemenanSerializer(qs,many=True)
            data={
                'issuccess':True,
                'data':serializer.data
                }
            return Response(data)
        except:
            data={
                'issuccess':False,
                'data':'Some Error, Please Try Again',
                }
            return Response(data)

class GetAllKahnatByDC(APIView):
    
    def post(self,request,*args,**kwargs):
        try:
            dcid=request.data["dcid"]
            pagination_id=request.data['id']
            if pagination_id==0:
                pagination_id=Kahnat.objects.last().__dict__['id']
            qs=Kahnat.objects.filter(id__lte=pagination_id,datacollectorid=dcid).order_by('-id')[:4]
            serializer=KahnatSerializer(qs,many=True)
            data={
                'issuccess':True,
                'data':serializer.data
                }
            return Response(data)
        except:
            data={
                'issuccess':False,
                'data':'Some Error, Please Try Again',
                }
            return Response(data)

class GetAllFammembersByParent(APIView):

    def post(self,request,*args,**kwargs):
        if CustomeAuth.auth(self,request,*args,**kwargs).__dict__['data']['issuccess']:
            try:
                pt_pi={
                    "parenttype":request.data["parenttype"],
                    "parentid":request.data["parentid"],
                    }
                qs=Fammember.objects.filter(**pt_pi)
                serializer=FammemberSerializer(qs,many=True)
                data={
                    'issuccess':True,
                    'data':serializer.data
                    }
                return Response(data)
            except Exception as e:
                data={
                    'issuccess':False,
                    'data':'Some Error, Please Try Again',
                    'error':str(e),
                    }
                return Response(data)
        else:
            data={
                'issuccess':False,
                'data':'Not Auth'
                }
            return Response(data)

class GetAllMemenan(APIView):
    
    def post(self,request,*args,**kwargs):
        if CustomeAuth.auth(self,request,*args,**kwargs).__dict__['data']['issuccess']:
            try:
                pagination_id=request.data['id']
                is_previous=request.data['is_previous']
                if pagination_id==0:
                    pagination_id=Memenan.objects.first().__dict__['id']
                
                if (is_previous):
                    print(f'is p true pid {pagination_id}')
                    qs=Memenan.objects.filter(id__lt=pagination_id).order_by('-id')[:10][::-1]
                else:
                    qs=Memenan.objects.filter(id__gte=pagination_id).order_by('id')[:10]
                
                serializer=MemenanSerializer(qs,many=True)
    
                data={
                    'issuccess':True,
                    'data':serializer.data,
    
                    }
                return Response(data)
            except Exception as e:
                data={
                    'issuccess':False,
                    'data':'Some Error, Please Try Again',
                    'serializer error':serializer.errors,
                    'error':str(e)
                    }
                return Response(data)
        else:
            data={
                'issuccess':False,
                'data':'Not Auth'
                }
            return Response(data)

class GetAllKahnat(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        try:    
            pagination_id=request.data['id']
            is_previous=request.data['is_previous']
            if pagination_id==0:
                pagination_id=Kahnat.objects.first().__dict__['id']

            if (is_previous):
                print(f'is p true pid {pagination_id}')
                qs=Kahnat.objects.filter(id__lt=pagination_id).order_by('-id')[:10][::-1]
            else:
                qs=Kahnat.objects.filter(id__gte=pagination_id).order_by('id')[:10]
            
            serializer=KahnatSerializer(qs,many=True)

            data={
                'issuccess':True,
                'data':serializer.data,

                }
            return Response(data)
        except Exception as e:
            print(e);
            data={
                'issuccess':False,
                'data':'Some Error, Please Try Again',
                'error':str(e)
                }
            return Response(data)

class GetAllMemenanByFilter(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        try:
            serializer= MemenanSerializer(data=request.data)
            filterdata=serializer.initial_data
            is_previous=request.data['is_previous']
            pagination_id=request.data['id']
            filterdata={k:v for k,v in filterdata.items() 
            if v is not None and v!='' and k!='id' and k!='is_previous'}
            print('filter data')
            print(filterdata)
            if pagination_id==0:
                pagination_id=Memenan.objects.first().__dict__['id']
            
            if (is_previous):
                print(f'is p true pid {pagination_id}')
                qs=Memenan.objects.filter(id__lt=pagination_id,**filterdata).order_by('-id')[:10][::-1]
            else:
                qs=Memenan.objects.filter(id__gte=pagination_id,**filterdata).order_by('id')[:10]
            
            serializer=MemenanSerializer(qs,many=True)

            data={
                'issuccess':True,
                'data':serializer.data,

                }
            return Response(data)
        except Exception as e:
            print('exception')
            print(e)
            data={
                'issuccess':False,
                'data':'Some Error, Please Try Again',
                }
            return Response(data)


class GetAllKahnatByFilter(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        try:
            serializer= KahnatSerializer(data=request.data)
            filterdata=serializer.initial_data
            pagination_id=request.data['id']
            is_previous=request.data['is_previous']
            filterdata={k:v for k,v in filterdata.items() 
            if v is not None and v!='' and k!='id' and k!='is_previous'}
            if pagination_id==0:
                pagination_id=Kahnat.objects.first().__dict__['id']
            print('filter data')
            print(filterdata)
            if (is_previous):
                print(f'is p true pid {pagination_id}')
                qs=Kahnat.objects.filter(id__lt=pagination_id,**filterdata).order_by('-id')[:10][::-1]
            else:
                qs=Kahnat.objects.filter(id__gte=pagination_id,**filterdata).order_by('id')[:10]
            
            serializer=KahnatSerializer(qs,many=True)

            data={
                'issuccess':True,
                'data':serializer.data,

                }
            return Response(data)
        except Exception as e:
            print(e)
            data={
                'issuccess':False,
                'data':'Some Error, Please Try Again',
                }
            return Response(data)
