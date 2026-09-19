from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel, QScrollArea

WHEEL_NOTCH = 120


class PDFViewer(QScrollArea):
    zoom_in_requested = Signal()
    zoom_out_requested = Signal()

    def __init__(self):
        super().__init__()

        self._wheel_delta = 0

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setWidget(self.image_label)
        self.setWidgetResizable(True)

    def display_page(self, pixmap):
        image = QImage(
            pixmap.samples,
            pixmap.width,
            pixmap.height,
            pixmap.stride,
            QImage.Format.Format_RGB888,
        )

        qt_pixmap = QPixmap.fromImage(image)

        self.image_label.setPixmap(qt_pixmap)

    def wheelEvent(self, event):
        if not event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            super().wheelEvent(event)
            return

        self._wheel_delta += event.angleDelta().y()

        while self._wheel_delta >= WHEEL_NOTCH:
            self._wheel_delta -= WHEEL_NOTCH
            self.zoom_in_requested.emit()

        while self._wheel_delta <= -WHEEL_NOTCH:
            self._wheel_delta += WHEEL_NOTCH
            self.zoom_out_requested.emit()

        event.accept()
