# HCI — Human-Computer Interaction (Sapienza Università di Roma)

## SyncTime: Mobile Application for Collaborative Group Travel Scheduling & Coordination
6인 국제 팀 프로젝트 (Nino Kurtanidze, Mariana Calais-Pedro, Davide Broza, Aleyna Mehmed,
**Hansom Kim**, Enes-Tarik Yalcin) — SwiftUI 기반 고충실도(high-fidelity) iOS 프로토타입

### 문제의식
Erasmus 교환학생들은 그룹 여행을 자주 계획하지만, 시간대가 다르고 일정이 WhatsApp·메모·구글독스 등에
흩어져 있어 "다 같이 되는 날짜"를 찾는 것 자체가 큰 고통입니다.

### Needfinding
- Erasmus/교환학생 **17명 심층 인터뷰**(1:1, 반구조화)를 통해 여행 빈도·그룹 규모·의사결정 방식·
  플래닝 역할 분담·페인포인트를 파악
- 핵심 페인포인트: ① 모두가 가능한 날짜 찾기의 어려움 ② 여러 앱에 흩어진 정보(WhatsApp/틱톡/구글맵/부킹닷컴 등)
  ③ 늦은 취소·낮은 커밋먼트

### 설계 & 반복
- **6라운드의 usability testing**을 거친 반복적 프로토타이핑 (V4, V5 등 버전별 사용성 테스트 진행)
- 핵심 기능 3가지에 집중: 공유 캘린더 타임라인 기반 가용성 표시, 부분 가용 시간대 지정,
  그룹 내 투표로 계획 교착 상태 해결
- "계정 생성 없이도 링크만으로 참여 가능"한 **zero-friction onboarding** 원칙을 설계 전 과정에 유지
- 테스트 중 발견한 문제(예: 날짜를 하나씩 클릭해야 하는 번거로움)를 다음 버전에서 즉시 개선

### 결론 및 한계
공유 가용성·부분 가용성 관리·그룹 투표라는 3가지 태스크에 집중해 실사용성 있는 프로토타입을 완성했습니다.
다만 실제 백엔드 없이 데이터가 목업(mock)되어 있어, 다음 단계로 계정 없이 링크로 참여 가능한 경량 서버 연동이 필요합니다.

### 파일
- [`SyncTime_HCI_final_report.pdf`](./SyncTime_HCI_final_report.pdf) — 팀 최종 리포트 전문 (Needfinding → 6라운드 프로토타이핑 → 최종 평가)
