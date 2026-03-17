🚗 Automotive SW QA Automation Portfolio
📌 Overview

차량 Telematics 시스템(eCall 포함)에 대한
Spec 기반 검증 및 테스트 자동화 프로젝트입니다.

실제 차량과 유사한 Test Bench 환경에서
다양한 시나리오(정상/예외)를 기반으로 검증을 수행하고,
로그 분석 및 자동화를 통해 품질 안정성을 확보했습니다.

🔍 Test Scope

eCall (Button eCall / Automatic eCall)

Power Mode / Sudden Voltage Drop

Remote Service / Car Sharing

OTA / ECU Flashing

AP Reset / NAD Reset

System Infrastructure / C2X

🛠️ Responsibilities

Spec / Requirement 기반 Test Case 설계

정상 / 예외 시나리오 포함 검증 커버리지 확대

ECU-TEST 기반 테스트 자동화 구축

반복 테스트 자동화 및 Regression Test 환경 구성

DLT / QXDM / Wireshark 로그 분석

필드 이슈 재현 및 원인 분석

결함 관리 (재현 절차 / 발생 조건 / 기대 vs 실제 결과 정리)

Test Result Report 작성 및 고객 대응

개발자 및 유관부서 협업을 통한 품질 개선

⚙️ Test Environment

Test Bench 기반 차량 유사 환경 구성

ECU 및 계측 장비 연동 테스트

DLT Receiver 기반 로그 수집 및 분석

🧪 Test Categories

Power & Voltage

Sudden Voltage Drop

Power Mode

Telematics

eCall (Button / Automatic)

Remote Service

Car Sharing

System

OTA

ECU Flashing

AP Reset / NAD Reset

Environment

Temperature

System Infrastructure

Communication

C2X

🔄 Test Automation Flow

Test Case 실행 (ADB / ECU-TEST 기반)

eCall Trigger (Button / Automatic)

DLT Log 실시간 수집

eCall Status 확인 (1 → 2 → 3 → 0)

결과 판별 (Pass / Fail)

로그 기반 원인 분석

결과 Excel 리포트 자동 생성

📊 DLT Log Example

eCall 상태 변화 확인 (Trigger → Connect → Disconnect → Expire)




💡 Key Achievements

기존 수동 테스트 → 자동화 전환으로 테스트 효율 향상

Spec 기반 Test Case 확장 → 검증 커버리지 개선

로그 기반 분석 체계 구축 → 이슈 재현 시간 단축

반복 테스트 자동화 → Regression Test 안정화

🚀 Skills & Tools

Automation: Python, ECU-TEST

Log Analysis: DLT, QXDM, Wireshark

Tools: ADB, TeraTerm

Domain: Automotive Telematics, eCall, OTA