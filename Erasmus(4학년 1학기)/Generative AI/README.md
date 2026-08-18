# Generative AI (Sapienza Università di Roma)

## One-Shot Symbolic Music Style Transfer
콘텐츠(X)와 스타일(Z) 심볼릭 음악 데이터를 입력받아, **피치는 보존(Chroma Preservation)** 하면서
**리듬/벨로시티 등 스타일 요소만 전이(Style Fit)** 하는 생성 모델 과제입니다.

- 생성 태스크 특성상 Y(정답)는 학습에 사용하지 않고, X(content)·Z(style) 만을 입력으로 사용
- Loss = Chroma Preservation Loss + Style Fit Loss 로 설계

### 파일
- [`music_style_transfer_v4.ipynb`](./music_style_transfer_v4.ipynb)

*추가 과제/노트는 업로드 예정입니다.*
