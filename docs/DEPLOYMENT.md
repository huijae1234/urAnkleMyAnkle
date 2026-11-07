# 설비 대시보드 배포

현재 Dash 앱은 프로젝트 루트 `app.py`에서 Flask 서버로 내보냅니다. Vercel의 Flask 프리셋과 Python 3.12를 사용하며, 화면·필터·판별 기준은 기존 앱을 그대로 사용합니다.

## 설치와 확인

```bash
python -m pip install -r requirements.txt
python -m src.wireframe_app
```

분석·노트북·시험 도구도 필요하면 `requirements-analysis.txt`를 설치합니다. 배포 진입점 확인은 `python -m pytest tests/test_deployment.py -q`로 실행합니다.

## Vercel

- 프로젝트 루트: 이 저장소의 루트
- Framework Preset: Flask
- Python: `.python-version`에 지정한 3.12
- Build Command / Output Directory: 별도 지정 없음
- 진입점: `app.py`의 `app`

`.vercelignore`는 웹 실행에 필요한 소스·원본 데이터·저장된 비교 결과만 업로드합니다. `vercel.json`의 `includeFiles`는 CSV·JSON·화면 자산·글꼴을 함수에 포함합니다. 예전 모델 파일, 실험용 산출물, 문서와 캡처는 배포하지 않습니다.

PDF 출력에는 한글 TrueType 글꼴이 필요합니다. 배포 루트에 `NanumGothic.ttf`와 해당 글꼴의 `NanumGothic-OFL.txt`를 두면 기존 글꼴 탐색기가 사용합니다. 운영 DB나 API 키는 필요하지 않습니다.

Vercel의 함수 응답 크기는 제한되므로, 전체 원자료 CSV처럼 큰 파일을 내보내는 경우는 별도 처리가 필요합니다. 배포 확인에는 네 화면 이동, 필터 변경, 표 정렬, 작은 CSV와 PDF·Excel 내보내기를 포함합니다.
