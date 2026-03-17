# 🚗 Automotive eCall Test Automation Portfolio

> Requirements-based End-to-End Vehicle QA Automation Project

## Overview
이 저장소는 차량 QA 관점에서 수행한 테스트 중 대표 시나리오를 **실행 가능한 코드 + 포트폴리오 문서** 형태로 정리한 통합 프로젝트입니다.

## Included Projects
- **TC1**: ADB + DLT 기반 Button eCall 자동화
- **TC2**: ADB + DLT + Selenium(BASE) 기반 Button eCall + Backend 검증
- **TC3**: CANoe / CAPL 기반 24시간 mileage 반복 테스트 템플릿

## Highlights
- Requirements-based Test Design
- End-to-End Validation
- 24h Repeat Automation Structure
- Summary / CycleSummary / Results Reporting
- Traceability-oriented Documentation

## Install
```bash
pip install -r requirements.txt
```

## Notes
- TC1/TC2는 `config.py`의 환경값 수정이 필요합니다.
- TC2의 Selenium locator와 BASE URL은 예시값입니다.
- TC3는 보안 대응용 placeholder 템플릿입니다.
