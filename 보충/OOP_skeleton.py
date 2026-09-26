import random



# 메서드 전후에 공통 동작을 추가하는 데코레이터
def clean_decorator(func):
    def wrapper(*args, **kwargs):
        print("[시작 전 청소 작업을 진행합니다]")
        func(*args, **kwargs)
        print("[종료 후 청소 작업을 진행합니다]")

    return wrapper


class Doctor:
    # 모든 인스턴스가 공유하는 클래스 변수
    hospital_name = "한국대학교병원"
    doctors = []

    # 인스턴스 속성 초기화 및 전체 의사 목록 등록
    def __init__(self, name, department, success_rate):
        self.name = name
        self.department = department
        self.reputation = 0
        self.success_rate = success_rate
        Doctor.doctors.append(self)

    # 인스턴스의 수술 결과에 따라 명성 변경
    @clean_decorator
    def surgery(self):
        print(f"{self.name} 의사가 수술을 시작합니다")
        if random.randint(1, 100) <= self.success_rate:
            self.reputation += 10
            print("수술 성공!")
        else:
            self.reputation -= 10
            print("수술 실패!")
        print(f"현재 명성치는 {self.reputation} 입니다")

    @clean_decorator
    def check(self):
        print(f"{self.name} 의사가 진료를 시작합니다")

    # 전체 의사를 명성 순으로 출력
    @classmethod
    def show_ranking(cls):
        ranking = sorted(
            cls.doctors,
            key=lambda doctor: doctor.reputation,
            reverse=True,
        )
        for index, doctor in enumerate(ranking, start=1):
            print(f"{index}등: {doctor.name} ({doctor.reputation})")

    # 객체 상태와 무관한 야간 근무 판별
    @staticmethod
    def is_night(hour):
        if hour >= 22 or hour < 6:
            print("야간 근무 중")
        else:
            print("주간 근무 중")


# 상속1. Doctor 를 상속받아 항문외과 의사 클래스 추가
class ColorectalSurgeon(Doctor):
    # 진료실(clinic_room) 속성 추가
    def __init__(self, name, department, success_rate, clinic_room):
        # 부모로부터 물려받은 속성 name, department, success_rate
        # 부모의 코드를 그대로 활용 --> 부모의 생성자 함수를 호출
        # super(): 상위(MRO 순서 기준 다음) 클래스에 접근하겠다.
        super().__init__(name, department, success_rate)
        self.clinic_room = clinic_room
    

    # 대장 내시경 결과 판독 메서드 추가
    # - 자식 class 에만 있는 추가 메서드
    def colonoscopy_result_interpretation(self):
        print(f"{self.name} 의사가 대장 내시경 결과를 판독합니다.")

    # 오버라이딩1. 기존 check -> 항문외과 환자 진료로 변경
    # - 메서드 이름을 동일하게 check 로 만들어 주어야 한다.
    def check(self):
        print(f"{self.name} 의사가 항문외과 진료를 시작합니다.")

    


class TraumaSurgeon(Doctor):
    def __init__(self, name, department, success_rate, emergency_vehicle):
        super().__init__(name, department, success_rate)
        self.emergency_vehicle = emergency_vehicle

    def request_doctor_helicopter(self):
        print(f"{self.name} 의사가 닥터헬기를 호출했습니다.")
            
    def check(self):
        print(f"{self.name} 의사가 호출한 닥터헬기가 출발합니다.")





# 상속1. Doctor 를 상속받아 외상외과 의사 클래스 추가
class TraumaSurgeon:
    pass


# 클래스에서 인스턴스 생성
doctor1 = Doctor("백강혁", "외상외과", 100)
doctor2 = Doctor("양재원", "항문외과", 75)
doctor3 = ColorectalSurgeon("한유림", "항문외과", 60, "외래3실")

doctor2.check()  # 부모 클래스의 check 를 호출
doctor3.check()  # 자식 클래스의 check 를 호출

# print(f"{Doctor.hospital_name}에 오신 것을 환영합니다")
# print(doctor1.name)
# print(doctor2.name)
# print(doctor3.name)

# doctor1.surgery()
# doctor1.surgery()
# doctor1.surgery()
# doctor2.surgery()
# doctor2.surgery()
# doctor2.surgery()
# doctor3.surgery()
# doctor3.surgery()
# doctor3.surgery()
# doctor3.check()

# Doctor.show_ranking()
# print(doctor1)