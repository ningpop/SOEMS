from user.models import User
from .models import Study, Participation
from django.shortcuts import get_object_or_404

from twilio.rest import Client

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# root dir에서 twilio.json을 읽어 auth_token 값을 불러오는 함수
def get_twilio_key(setting):
    twilio_file = os.path.join(BASE_DIR, "twilio.json")

    with open(twilio_file) as file:
        twilio_key = json.loads(file.read())

        try:
            return twilio_key["auth_token"]
        except KeyError:
            error_msg = "Set the {} environment variable".format(setting)
            raise ImproperlyConfigured(error_msg)

accounts_id = 'AC7e395a1420bb05fded85b3d46a896b57'
auth_token = get_twilio_key("TWILIO_KEY")
twilio_sending_number = '+12065905325'

client = Client(accounts_id, auth_token)


def sms_reminder(study_id, study_link):
    sms_text = '알림 메시지'

    study = get_object_or_404(Study, pk=study_id)
    participations = Participation.objects.filter(study=study)

    for participation in participations:
        sms_text = study.title + ' 강의의 수업 링크입니다. ' + study_link + ' 링크에 접속하여 강의에 참여해주세요.\n- SOEMS'
        send_to = '+82' + participation.applicant.phone[1:] # 국가번호 포함한 번호로 convert
        message = client.messages.create(
            from_ = twilio_sending_number,
            body = sms_text,
            to = send_to
        )