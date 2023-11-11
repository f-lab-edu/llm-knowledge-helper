from pytest import fixture

from src.global_vars import post_repository


# 모든 테스트 함수가 실행되기 전에 항상 실행되는 함수다.
# 테스트 함수마다 독립된 환경을 만들어주는 로직이 보통 여기에 포함된다.
@fixture(autouse=True, scope="function")
def setup():
    # 서버 내의 Post 데이터를 비워준다.
    post_repository.delete_all()
