"""데이터분석 트랙 레슨 콘텐츠 모듈 모음.

각 모듈은 다음 형식을 따른다:
    from engine.models import Lesson
    LESSONS = [ Lesson(id="ds1-01-...", lang="datasci", level="1. 데이터 기초", ...), ... ]

level 은 datasci/__init__.py 의 STAGES 중 하나여야 한다.
datasci/__init__.py 가 이 폴더의 모든 모듈을 자동 수집한다.
"""
