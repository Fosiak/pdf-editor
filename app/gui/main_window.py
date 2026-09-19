from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QFileDialog, QMainWindow

from app.gui.pdf_viewer import PDFViewer
from app.pdf.document import PDFDocument

DEFAULT_ZOOM = 1.0
MIN_ZOOM = 0.25
MAX_ZOOM = 4.0
ZOOM_STEP = 1.25


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PDF Editor")
        self.resize(1400, 900)
        self.setMinimumSize(800, 600)

        self.document = None
        self.current_page = 0
        self.zoom = DEFAULT_ZOOM

        self.pdf_viewer = PDFViewer()
        self.setCentralWidget(self.pdf_viewer)

        self.pdf_viewer.zoom_in_requested.connect(self.zoom_in)
        self.pdf_viewer.zoom_out_requested.connect(self.zoom_out)

        self.create_menu_bar()

    def create_menu_bar(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")
        open_action = file_menu.addAction("Open PDF...")
        open_action.triggered.connect(self.open_pdf)

        view_menu = menu_bar.addMenu("View")

        zoom_in_action = view_menu.addAction("Zoom In")
        zoom_in_action.setShortcut(QKeySequence.StandardKey.ZoomIn)
        zoom_in_action.triggered.connect(self.zoom_in)

        zoom_out_action = view_menu.addAction("Zoom Out")
        zoom_out_action.setShortcut(QKeySequence.StandardKey.ZoomOut)
        zoom_out_action.triggered.connect(self.zoom_out)

        reset_zoom_action = view_menu.addAction("Actual Size")
        reset_zoom_action.setShortcut(QKeySequence("Ctrl+0"))
        reset_zoom_action.triggered.connect(self.reset_zoom)

    def open_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open PDF",
            "",
            "PDF Files (*.pdf)"
        )

        if not file_path:
            return

        if self.document is not None:
            self.document.close()

        self.document = PDFDocument(file_path)
        self.current_page = 0
        self.zoom = DEFAULT_ZOOM

        self.refresh_view()

    def zoom_in(self):
        self.set_zoom(self.zoom * ZOOM_STEP)

    def zoom_out(self):
        self.set_zoom(self.zoom / ZOOM_STEP)

    def reset_zoom(self):
        self.set_zoom(DEFAULT_ZOOM)

    def set_zoom(self, zoom: float):
        if self.document is None:
            return

        self.zoom = max(MIN_ZOOM, min(MAX_ZOOM, zoom))
        self.refresh_view()

    def refresh_view(self):
        pixmap = self.document.render_page(self.current_page, self.zoom)
        self.pdf_viewer.display_page(pixmap)

        self.statusBar().showMessage(
            f"Page {self.current_page + 1} / {self.document.page_count}"
            f"  |  Zoom: {round(self.zoom * 100)}%"
        )
