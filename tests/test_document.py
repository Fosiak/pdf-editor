import fitz
import pytest

from app.pdf.document import PDFDocument


@pytest.fixture
def sample_pdf(tmp_path):
    path = tmp_path / "sample.pdf"
    doc = fitz.open()
    doc.new_page(width=200, height=300)
    doc.save(str(path))
    doc.close()
    return str(path)


def test_page_count(sample_pdf):
    document = PDFDocument(sample_pdf)
    try:
        assert document.page_count == 1
    finally:
        document.close()


def test_render_page_scales_with_zoom(sample_pdf):
    document = PDFDocument(sample_pdf)
    try:
        base = document.render_page(0, zoom=1.0)
        zoomed = document.render_page(0, zoom=2.0)
    finally:
        document.close()

    assert (base.width, base.height) == (200, 300)
    assert (zoomed.width, zoomed.height) == (400, 600)
