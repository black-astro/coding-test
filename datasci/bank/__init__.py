"""데이터분석 트랙 채점 문제 모음.

각 모듈은 다음 형식을 따른다:
    from engine.models import Problem
    PROBLEMS = [ Problem(id="dsq1-01", type="func", category="1. 데이터 기초", ...), ... ]

설계 규칙 (채점 엔진 제약에서 나온 것 — 반드시 지킬 것)
  · type="func" 고정 → 자동으로 Python 전용 채점이 된다.
  · 인자(args)는 JSON 으로 직렬화되므로 list/dict/int/float/str 만 가능하다.
    (numpy 배열·DataFrame 을 인자로 넘길 수 없다 → 리스트로 주고 함수 안에서 변환)
  · 반환값은 repr() 문자열로 비교한다. numpy 스칼라를 그대로 돌려주면
    repr 이 'np.float64(3.0)' 이 되어 오답 처리된다 → 반드시 float()/int()/tolist() 로 변환.
  · 실수 결과는 부동소수점 오차를 피하기 위해 문제에서 반올림 자리수를 명시한다.

datasci/__init__.py 가 이 폴더의 모든 모듈을 자동 수집한다.
"""
