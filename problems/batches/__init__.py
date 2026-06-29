"""추가 문제 배치들이 모이는 패키지.

각 배치 파일은 다음 형식을 따른다:
    from engine.models import Problem
    RANK = "Bronze"   # 또는 Silver/Gold/Platinum
    PROBLEMS = [ Problem(...), ... ]

problems/__init__.py 가 이 폴더의 모든 모듈을 자동으로 수집한다.
"""
