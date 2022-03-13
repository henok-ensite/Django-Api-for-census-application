from django.db.models import fields
from django.utils.text import phone2numeric
from rest_framework import serializers
from .models import Datacollectors, Fammember, Kahnat, Memenan, Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields=[
            'id',
            'fname',
            'phonenum',
            'password',
            'updatedat',
            'createdat',
            'status',
        ]
        extra_kwargs={'id':{'required':False,}}

class DatacollectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Datacollectors
        fields=[
            'id',
            'fname',
            'gender',
            'phonenum',
            'password',
            'weredabetekhnet',
            'status',
            'updatedat',
            'createdat',
            'updatedby',
        ]
        extra_kwargs={'id':{'required':False,}}

class DatacollectorsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Datacollectors
        fname=serializers.CharField(allow_null=True,allow_blank=True)
        phonenum=serializers.CharField(allow_null=True,allow_blank=True)
        password=serializers.CharField(allow_null=True,allow_blank=True)
        weredabetekhnet=serializers.CharField(allow_null=True,allow_blank=True)
        # id=serializers.IntegerField()
        fields=[
            'id',
            # 'fname',
            # 'phonenum',
            # 'password',
            # 'weredabetekhnet'
            
        ]
        # extra_kwargs={'fname':{'allow_null':True,'allow_blank':True,'required':False},
        #               'phonenum':{'allow_null':True,'allow_blank':True,'required':False},
        #               'password':{'allow_null':True,'allow_blank':True,'required':False},
        #               'weredabetekhnet':{'allow_null':True,'allow_blank':True,'required':False}
        # }
        
class FammemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fammember
        fields=[
                    'id',
                    "fname",
                    "mname",
                    "bdate",
                    "gender",
                    "yekrstnasm",
                    "education",
                    "jobtype",
                    "phonenum",
                    "relationtoparent",
                    "parentid",
                    "parenttype",
                    "datacollectorid",
                    "updatedat",
                    "createdat",
                    "updatedby",
        ]
extra_kwargs={
	'updatedat':{'allow_null':True,'allow_blank':True,'required':False},
	'createdat':{'allow_null':True,'allow_blank':True,'required':False},
    'parentid':{'allow_blank':True,'required':False},
    'updatedby':{'allow_null':True,'allow_blank':True,'required':False},
    	}
	
class MemenanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Memenan
        fields=[
            'id',
            "title",
            "othertitle",
            "fname",
            "gender",
            "phonenum",
            "bdate",
            "sfname",
            "stitle",
            "sothertitle",
            "jobtype",
            "education",
            "region",
            "zone",
            "wereda",
            "city",
            "subcity",
            "weredabetekhnet",
            "atbiya",
            "atbiyayegebubetzemen",
            "yekrstnasm",
            "sebekagubayeabal",
            "mothertongue",
            "economystatus",
            "familynum",
            "malenum",
            "femalenum",
            "plus18num",
            "housetype",
            "datacollectorid",
            "createdat",
            "updatedat",
            "updaterid",
            "updatedby",
        ]
extra_kwargs={
	'updaterid':{'allow_null':True,'allow_blank':True,'required':False},
	'updatedby':{'allow_null':True,'allow_blank':True,'required':False},
	'updatedbyfname':{'allow_null':True,'allow_blank':True,'required':False},
	'updatedat':{'allow_null':True,'allow_blank':True,'required':False},
	'createdat':{'allow_null':True,'allow_blank':True,'required':False},}

class KahnatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Kahnat
        fields=[
            'id',
            "title",
            "othertitle",
            "fname",
            "phonenum",
            "bdate",
            "sfname",
            "stitle",
            "sothertitle",
            "jobtype",
            "education",
            "region",
            "zone",
            "wereda",
            "city",
            "subcity",
            "weredabetekhnet",
            "atbiya",
            "yemiyageleglubetdebr",
            "sebekagubayeabal",
            "mothertongue",
            "economystatus",
            "familynum",
            "malenum",
            "femalenum",
            "plus18num",
            "housetype",
            "yenshaljochnum",
            "datacollectorid",
            "updatedat",
            "updaterid",
            "updatedby",
            "updatedbyfname"
        ]
extra_kwargs={
	'updaterid':{'allow_null':True,'allow_blank':True,'required':False},
	'updatedby':{'allow_null':True,'allow_blank':True,'required':False},
	'updatedbyfname':{'allow_null':True,'allow_blank':True,'required':False},
	'updatedat':{'allow_null':True,'allow_blank':True,'required':False},
	'createdat':{'allow_null':True,'allow_blank':True,'required':False},}
