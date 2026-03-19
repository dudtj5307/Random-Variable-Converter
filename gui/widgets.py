from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from PyQt6.QtGui import QTextOption, QFont
from PyQt6.QtCore import QMimeData

from gui.style import TEXT_MUTED

# 고정 폰트 크기 (QSS 상속 무시하고 코드에서 직접 고정)
_CODE_FONT_SIZE = 13


class PlainPasteEdit(QTextEdit):
    """
    붙여넣기 시 서식을 제거하고 순수 텍스트만 삽입하는 QTextEdit.
    웹페이지·리치텍스트 복사본의 HTML/CSS가 그대로 들어오는 문제를 차단합니다.
    """

    def insertFromMimeData(self, source: QMimeData) -> None:  # type: ignore[override]
        if source.hasText():
            self.insertPlainText(source.text())
        # HTML/image 등 다른 형식은 무시


def make_code_panel(title: str, placeholder: str) -> tuple[QWidget, QTextEdit]:
    """
    제목 레이블 + 코드 편집기로 구성된 패널 위젯을 생성합니다.

    Args:
        title       : 패널 상단에 표시할 레이블 텍스트
        placeholder : QTextEdit 플레이스홀더 문자열

    Returns:
        (panel_widget, text_edit) 튜플
        - panel_widget : 레이아웃이 완성된 QWidget (Splitter에 추가 가능)
        - text_edit    : 내부 QTextEdit (외부에서 직접 읽기·쓰기용)
    """
    widget = QWidget()
    layout = QVBoxLayout(widget)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(8)

    label = QLabel(title)
    label.setObjectName("panelTitle")
    layout.addWidget(label)

    edit = PlainPasteEdit()
    edit.setPlaceholderText(placeholder)
    edit.setWordWrapMode(QTextOption.WrapMode.NoWrap)

    # QSS font-size가 외부 스타일시트에 의해 덮어쓰이지 않도록 코드에서도 고정
    font = QFont("JetBrains Mono, Consolas, Courier New")
    font.setPointSize(_CODE_FONT_SIZE)
    font.setStyleHint(QFont.StyleHint.Monospace)
    edit.setFont(font)

    layout.addWidget(edit)

    return widget, edit