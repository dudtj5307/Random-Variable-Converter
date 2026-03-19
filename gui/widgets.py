from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from PyQt6.QtGui import QTextOption
from gui.style import TEXT_MUTED


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

    edit = QTextEdit()
    edit.setPlaceholderText(placeholder)
    edit.setWordWrapMode(QTextOption.WrapMode.NoWrap)
    layout.addWidget(edit)

    return widget, edit
