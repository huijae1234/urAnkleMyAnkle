"""호스팅 응답 크기를 넘는 CSV가 오류 대신 안내로 처리되는지 확인한다."""
from types import SimpleNamespace

import pytest
from dash import no_update

from src import wireframe_app


@pytest.mark.parametrize("hosted,size,blocked", [(True, 3_000_001, True), (True, 10, False), (False, 3_000_001, False)])
def test_csv_download_hosting_limit(monkeypatch, hosted, size, blocked):
    if hosted:
        monkeypatch.setenv("VERCEL", "1")
    else:
        monkeypatch.delenv("VERCEL", raising=False)
    monkeypatch.setattr(wireframe_app, "ctx", SimpleNamespace(triggered=[{"value": 1}], triggered_id={"index": "raw"}))
    monkeypatch.setattr(wireframe_app, "_filter_scope", lambda _: (None, None, None))
    monkeypatch.setattr(wireframe_app, "export_table_csv", lambda *args, **kwargs: (b"a" * size, "data.csv"))
    download, message = wireframe_app.export_dtable_csv([1], {})
    if blocked:
        assert download is no_update
        assert "기간이나 기계" in message
    else:
        assert download["filename"] == "data.csv"
        assert message is no_update
