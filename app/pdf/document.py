import fitz


class PDFDocument:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.document = fitz.open(file_path)

    @property
    def page_count(self) -> int:
        return self.document.page_count

    def render_page(self, page_number: int, zoom: float = 1.0) -> fitz.Pixmap:
        page = self.document.load_page(page_number)
        matrix = fitz.Matrix(zoom, zoom)
        return page.get_pixmap(matrix=matrix, alpha=False)

    def close(self):
        self.document.close()
