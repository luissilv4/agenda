from rest_framework import serializers
from clients.models import Client, RGPD, Sex


class RGPDSerializer(serializers.ModelSerializer):
    class Meta:
        model=RGPD
        fields=['sms_reminders','email_reminders','new_appointment_notification',
                'marketing','satisfaction_forms']

class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = ('__all__')


class ClientSerializer(serializers.ModelSerializer):
    rgpd = RGPDSerializer()

    class Meta:
        model = Client
        fields = ['id','name','email','phone_number','alt_phone_number','data',
        'birthday', 'nif', 'cc','fav_staff','uuid', 'sex','rgpd']
        # depth = 1
        # read_only_fields = ['id','uuid']

    def create(self, validated_data):
        rgpd_data = validated_data.pop('rgpd')
        rgpd = RGPD.objects.create(**rgpd_data)
        client = Client.objects.create(rgpd=rgpd, **validated_data)

        return client

    def update(self, instance, validated_data):
        rgpd_data = validated_data.pop('rgpd')
        rgpd_instance = instance.rgpd

        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.alt_phone_number = validated_data.get('alt_phone_number', instance.alt_phone_number)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.nif = validated_data.get('nif', instance.nif)
        instance.fav_staff = validated_data.get('fav_staff', instance.fav_staff)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.cc = validated_data.get('cc', instance.cc)
        instance.save()

        rgpd_instance.sms_reminders = rgpd_data.get(
            'sms_reminders',
            rgpd_instance.sms_reminders
            )
        rgpd_instance.email_reminders = rgpd_data.get(
            'email_reminders',
            rgpd_instance.email_reminders
             )
        rgpd_instance.new_appointment_notification = rgpd_data.get(
            'new_appointment_notification',
            rgpd_instance.new_appointment_notification
         )
        rgpd_instance.marketing = rgpd_data.get(
            'marketing',
            rgpd_instance.marketing
        )
        rgpd_instance.satisfaction_forms = rgpd_data.get(
            'sms_reminder',
            rgpd_instance.satisfaction_forms
        )
        
        instance.save()
        return instance
