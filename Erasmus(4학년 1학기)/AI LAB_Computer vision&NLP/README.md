# AI LAB — Computer Vision & NLP (Sapienza Università di Roma)

## Helmet Detection Under Adverse Imaging Conditions: A Comparative Robustness Benchmark of YOLOv8 Variants
*Department of Computer, Control and Management Engineering, Sapienza Università di Roma — AY 2025–2026*

오토바이 헬멧 착용 감지를 위해 **YOLOv8n / YOLOv8s / YOLOv8m** 세 모델을 학습시키고,
**15가지 이미지 손상(corruption) 유형 × 5단계 심각도**(Michaelis et al., 2019 프로토콜)에서
로버스트니스를 정량적으로 비교한 벤치마크 연구입니다.

### 데이터 & 학습
- Kaggle Helmet Detection Dataset (764장, PASCAL VOC → YOLO 포맷 변환), 70/15/15 split (seed=42)
- COCO 사전학습 가중치에서 파인튜닝, 배치 16, 640×640, SGD(momentum 0.937), 최대 50 epoch + early stopping

### 로버스트니스 벤치마크
- **mPC / rPC 지표** (Michaelis et al.) 로 Noise / Blur / Weather / Digital 4개 그룹, 15개 손상 유형 평가
- Paired t-test + Cohen's d로 모델 간 통계적 유의성 검증

### 핵심 결과
| Model | Clean mAP@.5 | Latency | rPC (Robustness) |
|---|---|---|---|
| YOLOv8n | **0.782** (최고 정확도) | 36.9ms | 72.0% |
| YOLOv8s | 0.743 | **28.7ms (최저 지연)** | **72.9% (최고 강건성)** |
| YOLOv8m | 0.760 | 40.9ms | 69.1% |

- **Weather** 손상은 가장 잘 견디는 반면, **Pixelation·Elastic Transform** 이 가장 치명적
- 모델 간 강건성 차이는 통계적으로 유의하지 않음 (all p > 0.05, Cohen's d < 0.21) → 이 데이터 규모에서는
  모델 크기보다 **손상 인식 학습(corruption-aware training)** 이 더 중요할 수 있음을 시사
- **배포 권장**: YOLOv8s (정확도-강건성-속도 균형 최적, edge 배포에도 적합한 11.1M 파라미터)

### 파일
- [`Advanced_Helmet_Detection.ipynb`](./Advanced_Helmet_Detection.ipynb) — 학습·평가·로버스트니스 벤치마크 전체 코드
