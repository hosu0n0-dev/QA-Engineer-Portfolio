# Overall Architecture

## Requirement Analysis
- RQ-01 eCall Trigger
- RQ-02 eCall Status Transition
- RQ-03 Call Connection Handling
- RQ-04 Backend Data Verification
- RQ-05 Timeout Handling
- RQ-06 Repeatability / Reliability
- RQ-07 Signal-based Value Change Verification

## Additional Test Coverage
| Category | Test Case | Description |
|---|---|---|
| eCall | Button eCall | 사용자 버튼 기반 긴급 호출 검증 |
| eCall | Automatic eCall | Crash/Airbag 기반 자동 호출 검증 |
| Power | Power Mode | IGN 상태 변화 검증 |
| Power | Sudden Voltage Drop | 저전압 상황 안정성 검증 |
| Backend | Remote Service | 원격 명령 수행 및 차량 응답 검증 |
| Connectivity | Car Sharing | 차량 공유 기능 및 인증 흐름 검증 |
| Connectivity | MTS Mode | Telecommunication 모드 동작 검증 |
| Update | OTA | Over-the-Air 업데이트 검증 |
| Maintenance | ECU Flashing | ECU 소프트웨어 업데이트 검증 |
| Recovery | AP Reset | AP 재기동 검증 |
| Recovery | NAD Reset | 네트워크 모듈 재시작 후 복구 검증 |
