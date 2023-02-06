from rest_framework import serializers
from Ainaw_And_Social_Connect.models import RegisterNGO, NonRegisterNGO, SocialActivist_Enterpreneur, Business_Manpower


class RegisterNGOSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterNGO
        fields = ('fullName', 'email', 'mobile', 'password', 'subproject')

    def create(self, validated_data):
        ngo = RegisterNGO.objects.create(
            fullName=validated_data[' fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            subproject=validated_data['subproject']
        )
        ngo.save()
        return ngo


class NonRegisterNGOSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonRegisterNGO
        fields = ('fullName', 'email', 'mobile', 'password', 'subproject')

    def create(self, validated_data):
        non_ngo = NonRegisterNGO.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            subproject=validated_data['subproject']
        )
        non_ngo.save()
        return non_ngo


class SocialActivist_EnterpreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialActivist_Enterpreneur
        fields = ('fullName', 'email', 'mobile', 'password', 'subproject')

    def create(self, validated_data):
        socialactivist = SocialActivist_Enterpreneur.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            subproject=validated_data['subproject']
        )
        socialactivist.save()
        return socialactivist


class Business_ManpowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business_Manpower
        fields = ('fullName', 'email', 'mobile', 'password', 'subproject')

    def create(self, validated_data):
        business = Business_Manpower.objects.create(
        fullName=validated_data['fullName'],
        email=validated_data['email'],
        mobile=validated_data['mobile'],
        password=validated_data['password'],
        subproject=validated_data['subproject']
        )
        business.save()
        return business
