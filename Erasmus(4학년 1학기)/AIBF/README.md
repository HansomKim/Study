# AIBF — Artificial Intelligence in Banking and Finance (Sapienza Università di Roma)

금융/은행 도메인에 머신러닝을 적용하는 응용 수업입니다. (담당: Valentina Lagasio)

## 다룬 모델과 금융 응용
- **Decision Trees** — 불순도 지표(Gini, Entropy), 비용-복잡도 가지치기(Cost-complexity pruning),
  신용 리스크(credit risk) 평가에서 로지스틱 회귀 대비 해석력/안정성 트레이드오프 비교
- **Random Forest & Ensemble Models** — 단일 트리 대비 낮은 분산·과적합 완화, 특성 중요도(feature importance)
  자동 산출, 블랙박스 특성으로 인한 해석력 손실이라는 트레이드오프
- **SVM & KNN** — 마진 최대화(hard/soft margin, 커널 트릭)와 최근접 이웃 기반 분류를 비교하고,
  **사기 탐지(fraud detection)** 와 **신용평가(credit scoring)** 응용 사례에 적용
- **PCA** — 공분산·고유벡터·SVD 기반 차원 축소, 수익률 곡선(yield curve)·리스크 팩터·신용 분석·클러스터링 등
  금융 데이터에서 다중공선성이 높은 변수를 소수의 직교 성분으로 요약하는 방법

## 핵심 관점
단순히 모델 성능만이 아니라, **은행/금융 규제 맥락에서 해석 가능성(interpretability)과 예측 성능 사이의
트레이드오프**를 각 모델별로 비교·평가하는 관점을 일관되게 배웠습니다. (경영컨설팅학회 ESG 연구에서
투명성-신뢰성 지표를 설계할 때도 이 관점을 참고했습니다.)

*강의자료는 저작권상 업로드하지 않았으며, 위 내용은 수강 후 직접 정리한 요약입니다.*
