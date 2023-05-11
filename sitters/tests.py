import datetime
from django.test import TestCase
from django.utils import timezone

from sitters.models import PetSitter

# Create your tests here.
# class QuestionModelTests(TestCase):
        
#         def test_reservation(self):
#              #상황을 코드로 만들어줌
#              #예약일이 과거일경우 false
#              time = timezone.now() + datetime.timedelta(days=30)
#              reservation_petsitter = PetSitter(reservation_start=time)

#              #원하는 결과값이 나오는지 확인
#              self.assertIs(reservation_petsitter.save(), False)

        # def save(self, **kwargs):
        # if self.reservation_start < timezone.now():
        #   raise ValidationError("예약시작일이 오늘보다 이전일 수 없습니다.")
        # if self.reservation_end < self.reservation_start:
        #     raise ValidationError('예약 종료일이 예약 시작일보다 이전일 수 없습니다.')
        # else:    
        #     self.reservation_period = (self.reservation_end - self.reservation_start) + timedelta(days=1)
        #     super(CommonModel, self).save(**kwargs) # super의 첫번째 인자로 클래스명 , 객체 인스턴스가 들어갑니다