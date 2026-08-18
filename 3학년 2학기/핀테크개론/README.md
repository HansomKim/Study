# 핀테크개론 (FinTech Intro)

수리통계데이터사이언스학부(핀테크학과) 이수 과목으로, 핀테크 산업의 기술적 기반을 다룹니다.
중간고사 범위는 **암호학(Cryptography)** 이었습니다.

## 중간고사 범위 — Cryptography 핵심 정리

**1주차. Introduction**
- Cryptography: 악의적인 제3자가 있어도 안전하게 통신하기 위한 기술 (예: Caesar shift cipher)
- 현대 암호학의 기본 구성요소: Plaintext / Ciphertext / Encryption / Decryption
- **Kerckhoffs's Principle**: 암호 시스템의 안전성은 알고리즘이 아니라 **키(key)** 의 비밀성에서 나온다
  → 키가 유출되면 키만 교체하고, 알고리즘 자체를 재설계할 필요는 없다
- 공격 유형: Passive Attack(도청·트래픽 분석) vs Active Attack(변조·삭제·사칭)
- 공격 모델: Ciphertext-only / Known-plaintext / Chosen-plaintext / Chosen-ciphertext attack
- 공격 기법: Brute-force, 통계적 분석, 수학적 분석(공개키), 사이드채널 분석
- 정보보안 3요소(CIA Triad): Confidentiality(기밀성) · Integrity(무결성) · Availability(가용성)

**2주차. Classic Ciphers**
- Modular arithmetic(모듈러 연산) 기반 고전 암호 체계

## 왜 핀테크 전공에서 암호학을 배우나
블록체인·전자결제·전자서명 등 핀테크 시스템의 신뢰성은 암호학적 안전성 위에서 작동하기 때문에,
암호 시스템 설계 원칙(Kerckhoffs's Principle)과 공격 모델을 이해하는 것이 핀테크 보안의 기초가 됩니다.
이 과목은 전국 대학생 AI 시스템 트레이딩 챌린지에서 다룬 금융 시스템/파생상품 지식과도 함께 학부 핀테크 트랙을 구성합니다.
