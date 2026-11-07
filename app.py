"""Vercel이 불러오는 Flask 진입점. Dash의 화면과 콜백을 그대로 사용한다."""

from src.wireframe_app import app as dashboard

app = dashboard.server
