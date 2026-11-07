"""Vercel 진입점에서 Dash의 HTML·초기 상태·콜백·스타일이 열리는지 확인한다."""

from app import app


def test_deployment_entrypoint_serves_dashboard():
    client = app.test_client()
    assert client.get("/").status_code == 200
    layout = client.get("/_dash-layout")
    assert layout.status_code == 200
    assert "screen-content" in layout.get_data(as_text=True)
    dependencies = client.get("/_dash-dependencies")
    assert dependencies.status_code == 200
    assert dependencies.get_json()
    stylesheet = client.get("/assets/00-tokens.css")
    assert stylesheet.status_code == 200
    assert "--" in stylesheet.get_data(as_text=True)
