# 데이터베이스 (Database, SQL)

관계형 데이터베이스 이론(데이터베이스 시스템, 관계 데이터 모델, SQL 기초/고급, 데이터베이스 프로그래밍)과
MySQL Workbench 실습을 다루는 수업입니다.

## 실습 1 — 마당서점(Madang Bookstore) SQL 실습
표준 교육용 서점 스키마(`madangdb`)를 MySQL Workbench에 구축하고, 고객·운영자·경영자 관점의 다양한
비즈니스 질의를 SQL로 작성하는 과제입니다.
- [`demo_madang.sql`](./demo_madang.sql) — 데이터베이스/사용자 생성 및 초기 스키마 스크립트

## 실습 2 — EduLink: 과외/학원 관리 시스템 설계
학생–학부모–튜터 관계를 직접 스키마로 설계하고 데이터를 채운 뒤 JOIN 쿼리로 관계를 조회하는 2차 과제입니다.
Math & Coding Instructor로 활동하며 실제 만들었던 Notion 기반 LMS 경험을 SQL 스키마 설계로 확장한 실습이기도 합니다.
- [`edulink1.sql`](./edulink1.sql) — Student / Parent / Tutor / Subject / Enrollment 테이블 스키마 설계 (FK 관계 포함)
- [`edulink2.sql`](./edulink2.sql) — 샘플 데이터 삽입
- [`edulink3.sql`](./edulink3.sql) — 학생-과목-수강, 학생-학부모, 학생-멘토 등 다중 테이블 JOIN 쿼리
