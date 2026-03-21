from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QTableWidget, QTableWidgetItem,
    QHeaderView, QSplitter, QFrame, QStatusBar,
    QStyle, QStyleOptionButton,
)
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import (
    QFont, QColor, QPainter,
    QTextCharFormat, QTextCursor,
)
import re

from gui.style import ACCENT, ORANGE, BORDER_COLOR, GREEN, DARK_BG, TEXT_PRIMARY, PANEL_BG, TEXT_MUTED, STYLE
from gui.widgets import make_code_panel
from utils import anonymize_code, restore_code

_COL_CHECK = 0
_COL_ORIG  = 1
_COL_ALIAS = 2

# 하이라이트 색상
_HL_BG   = "#3a3000"   # 어두운 황색 배경
_HL_FG   = "#ffd700"   # 밝은 황색 글씨


class CheckableHeader(QHeaderView):
    """0번 컬럼 헤더에 체크박스를 그려 전체 선택/해제를 토글합니다."""

    def __init__(self, parent: QTableWidget) -> None:
        super().__init__(Qt.Orientation.Horizontal, parent)
        self._checked = True
        self.setSectionsClickable(True)
        self.sectionClicked.connect(self._on_section_clicked)

    def paintSection(self, painter: QPainter, rect: QRect, logical_index: int) -> None:
        painter.save()
        super().paintSection(painter, rect, logical_index)
        painter.restore()

        if logical_index != _COL_CHECK:
            return

        cb_size = 13
        x = rect.x() + (rect.width()  - cb_size) // 2
        y = rect.y() + (rect.height() - cb_size) // 2

        opt = QStyleOptionButton()
        opt.rect = QRect(x, y, cb_size, cb_size)
        opt.state = (
            QStyle.StateFlag.State_Enabled |
            (QStyle.StateFlag.State_On if self._checked else QStyle.StateFlag.State_Off)
        )
        self.style().drawControl(QStyle.ControlElement.CE_CheckBox, opt, painter)

    def _on_section_clicked(self, logical_index: int) -> None:
        if logical_index != _COL_CHECK:
            return
        self._checked = not self._checked
        state = Qt.CheckState.Checked if self._checked else Qt.CheckState.Unchecked
        table: QTableWidget = self.parent()  # type: ignore[assignment]
        for row in range(table.rowCount()):
            item = table.item(row, _COL_CHECK)
            if item:
                item.setCheckState(state)
        self.viewport().update()

    def set_all_checked(self, checked: bool) -> None:
        self._checked = checked
        self.viewport().update()


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.current_mapping: dict[str, str] = {}
        self.setWindowTitle("C++ Variable & Function Anonymizer")
        self.setMinimumSize(1280, 720)
        self.resize(1400, 800)
        self.setStyleSheet(STYLE)
        self._build_ui()

    # ── UI 구성 ───────────────────────────────────────────────────────────────

    def _build_ui(self) -> None:
        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(20, 16, 20, 12)
        root.setSpacing(16)

        root.addLayout(self._build_header())
        root.addWidget(self._build_divider())
        root.addWidget(self._build_main_panels())

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage(
            "준비  ·  왼쪽 창에 C++ 코드를 붙여넣고 [변수명 익명화] 버튼을 누르세요."
        )

    def _build_header(self) -> QHBoxLayout:
        header = QHBoxLayout()

        title_col = QVBoxLayout()
        title_col.setSpacing(2)
        app_title = QLabel("C++ Variable & Function Anonymizer")
        app_title.setObjectName("appTitle")
        subtitle = QLabel("보안 환경 LLM 사용을 위한 변수명 & 함수명 익명화 도구")
        subtitle.setObjectName("appSubtitle")
        title_col.addWidget(app_title)
        title_col.addWidget(subtitle)

        self.btn_convert = QPushButton("익명화   ▶")
        self.btn_convert.setObjectName("convertBtn")
        self.btn_convert.setFixedHeight(40)
        self.btn_convert.setMinimumWidth(80)
        self.btn_convert.clicked.connect(self._on_convert)

        self.btn_restore = QPushButton("◀   복호화")
        self.btn_restore.setObjectName("restoreBtn")
        self.btn_restore.setFixedHeight(40)
        self.btn_restore.setMinimumWidth(80)
        self.btn_restore.clicked.connect(self._on_restore)

        self.btn_clear = QPushButton("초기화")
        self.btn_clear.setObjectName("clearBtn")
        self.btn_clear.setFixedHeight(40)
        self.btn_clear.clicked.connect(self._on_clear)

        header.addLayout(title_col)
        header.addSpacing(16)
        header.addWidget(self.btn_convert)
        header.addStretch()

        header.addWidget(self.btn_restore)
        header.addSpacing(12)
        header.addWidget(self.btn_clear)

        return header

    def _build_divider(self) -> QFrame:
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setStyleSheet(f"color: {BORDER_COLOR}; background: {BORDER_COLOR};")
        line.setFixedHeight(1)
        return line

    def _build_main_panels(self) -> QSplitter:
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setHandleWidth(8)
        splitter.setChildrenCollapsible(False)

        left_panel, self.input_edit = make_code_panel(
            "  INPUT — 원본 C++ 코드",
            "C++ 코드를 여기에 붙여넣으세요...",
        )
        mid_widget = self._build_mapping_panel()
        right_panel, self.output_edit = make_code_panel(
            "  OUTPUT — 익명화된 코드",
            "익명화된 코드가 여기에 표시됩니다...",
        )

        splitter.addWidget(left_panel)
        splitter.addWidget(mid_widget)
        splitter.addWidget(right_panel)
        splitter.setSizes([500, 300, 500])

        # 좌우 스크롤바 동기화
        self._syncing_scroll = False
        self._connect_scroll_sync()

        return splitter

    def _build_mapping_panel(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        title_row = QHBoxLayout()
        mid_title = QLabel("  MAPPING — 변수명/함수명 매핑")
        mid_title.setObjectName("panelTitle")
        self.btn_refresh = QPushButton("↺  갱신")
        self.btn_refresh.setObjectName("refreshBtn")
        self.btn_refresh.setFixedHeight(24)
        self.btn_refresh.setToolTip("체크 해제된 변수는 원본명 그대로 유지하고 OUTPUT을 다시 생성합니다.")
        self.btn_refresh.clicked.connect(self._on_refresh)
        title_row.addWidget(mid_title)
        title_row.addStretch()
        title_row.addWidget(self.btn_refresh)
        title_row.addSpacing(6)
        layout.addLayout(title_row)

        self.table = QTableWidget(0, 3)

        self._header = CheckableHeader(self.table)
        self.table.setHorizontalHeader(self._header)
        self.table.setHorizontalHeaderLabels(["", "ORIGINAL", "ANONYMIZED"])

        hh = self.table.horizontalHeader()
        hh.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        hh.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        hh.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.table.setColumnWidth(0, 30)
        self.table.verticalHeader().setVisible(False)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setAlternatingRowColors(False)

        # 더블클릭 → 양쪽 텍스트 하이라이트
        self.table.cellDoubleClicked.connect(self._on_cell_double_clicked)

        layout.addWidget(self.table)

        self.count_label = QLabel("변환된 변수: 0개  ")
        self.count_label.setObjectName("appSubtitle")
        self.count_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.count_label)

        return widget

    # ── 이벤트 핸들러 ─────────────────────────────────────────────────────────

    def _on_convert(self) -> None:
        original = self.input_edit.toPlainText().strip()
        if not original:
            self.status_bar.showMessage("⚠  입력 코드가 없습니다.")
            return

        anonymized, mapping = anonymize_code(original)
        self.current_mapping = mapping

        self.output_edit.setPlainText(anonymized)
        self._populate_table(mapping)
        self._clear_highlights()

        n = len(mapping)
        self.count_label.setText(f"변환된 변수: {n}개  ")
        self.status_bar.showMessage(
            f"✓  익명화 완료 — {n}개 변수 치환됨. "
            "체크를 해제한 뒤 [↺ 갱신]으로 일부 변수만 익명화할 수 있습니다."
        )

    def _on_refresh(self) -> None:
        if not self.current_mapping:
            self.status_bar.showMessage("⚠  먼저 익명화를 수행해야 합니다.")
            return

        original = self.input_edit.toPlainText()
        if not original.strip():
            self.status_bar.showMessage("⚠  입력 코드가 없습니다.")
            return

        checked: set[str] = set()
        unchecked: set[str] = set()
        for row in range(self.table.rowCount()):
            chk_item  = self.table.item(row, _COL_CHECK)
            orig_item = self.table.item(row, _COL_ORIG)
            if chk_item is None or orig_item is None:
                continue
            orig_name = orig_item.text()
            if chk_item.checkState() == Qt.CheckState.Checked:
                checked.add(orig_name)
            else:
                unchecked.add(orig_name)

        active_mapping = {k: v for k, v in self.current_mapping.items() if k in checked}

        result = original
        for orig, alias in active_mapping.items():
            result = re.sub(r'\b' + re.escape(orig) + r'\b', alias, result)

        self.output_edit.setPlainText(result)
        self._clear_highlights()

        skipped = len(unchecked)
        applied = len(active_mapping)
        self.count_label.setText(f"변환된 변수: {applied}개  (제외: {skipped}개)  ")
        self.status_bar.showMessage(
            f"↺  갱신 완료 — {applied}개 익명화 · {skipped}개 원본 유지."
        )

    def _on_restore(self) -> None:
        if not self.current_mapping:
            self.status_bar.showMessage("⚠  먼저 익명화를 수행해야 합니다.")
            return

        anonymized_result = self.output_edit.toPlainText().strip()
        if not anonymized_result:
            self.status_bar.showMessage("⚠  오른쪽 창에 LLM 결과를 붙여넣어 주세요.")
            return

        restored = restore_code(anonymized_result, self.current_mapping)
        self.input_edit.setPlainText(restored)
        self._clear_highlights()
        self.status_bar.showMessage(
            "✓  복원 완료 — 왼쪽 창에서 원본 변수명으로 복원된 코드를 확인하세요."
        )

    def _on_clear(self) -> None:
        self.input_edit.clear()
        self.output_edit.clear()
        self.table.setRowCount(0)
        self.current_mapping = {}
        self.count_label.setText("변환된 변수: 0개  ")
        self._clear_highlights()
        self.status_bar.showMessage("초기화되었습니다.")

    def _on_cell_double_clicked(self, row: int, col: int) -> None:
        """더블클릭한 행의 원본명/익명명을 양쪽 편집기에서 하이라이트합니다."""
        chk_item   = self.table.item(row, _COL_CHECK)
        orig_item  = self.table.item(row, _COL_ORIG)
        alias_item = self.table.item(row, _COL_ALIAS)
        if orig_item is None or alias_item is None:
            return

        orig_word  = orig_item.text()
        alias_word = alias_item.text()

        # 체크 해제된 항목은 output에도 원본명 그대로 남아 있으므로 orig_word로 검색
        is_checked = (
            chk_item is not None
            and chk_item.checkState() == Qt.CheckState.Checked
        )
        output_word = alias_word if is_checked else orig_word

        self._clear_highlights()
        self._highlight_word(self.input_edit,  orig_word)
        self._highlight_word(self.output_edit, output_word)

        if is_checked:
            msg = f"🔍  '{orig_word}'  →  '{alias_word}'  하이라이트 중"
        else:
            msg = f"🔍  '{orig_word}'  (익명화 제외 — 양쪽 모두 원본명으로 표시)  하이라이트 중"
        self.status_bar.showMessage(msg + " — 다른 행 더블클릭 시 전환됩니다.")

    # ── 내부 헬퍼 ─────────────────────────────────────────────────────────────

    def _highlight_word(self, editor, word: str) -> None:
        """editor 안에서 word와 일치하는 모든 토큰을 ExtraSelection으로 강조합니다."""
        fmt = QTextCharFormat()
        fmt.setBackground(QColor(_HL_BG))
        fmt.setForeground(QColor(_HL_FG))
        fmt.setFontWeight(QFont.Weight.Bold)

        selections = []
        doc = editor.document()
        cursor = QTextCursor(doc)

        pattern = re.compile(r'\b' + re.escape(word) + r'\b')
        full_text = editor.toPlainText()

        for m in pattern.finditer(full_text):
            sel = editor.ExtraSelection()  # type: ignore[attr-defined]
            c = QTextCursor(doc)
            c.setPosition(m.start())
            c.setPosition(m.end(), QTextCursor.MoveMode.KeepAnchor)
            sel.cursor = c
            sel.format = fmt
            selections.append(sel)

        editor.setExtraSelections(selections)

    def _connect_scroll_sync(self) -> None:
        """좌우 편집기 스크롤바를 양방향으로 동기화합니다."""
        in_v  = self.input_edit.verticalScrollBar()
        out_v = self.output_edit.verticalScrollBar()
        in_h  = self.input_edit.horizontalScrollBar()
        out_h = self.output_edit.horizontalScrollBar()

        in_v.valueChanged.connect(lambda v: self._sync_scroll(out_v, v))
        out_v.valueChanged.connect(lambda v: self._sync_scroll(in_v,  v))
        in_h.valueChanged.connect(lambda v: self._sync_scroll(out_h, v))
        out_h.valueChanged.connect(lambda v: self._sync_scroll(in_h,  v))

    def _sync_scroll(self, target, value: int) -> None:
        """재귀 호출 없이 상대 스크롤바 값을 동기화합니다."""
        if self._syncing_scroll:
            return
        self._syncing_scroll = True
        target.setValue(value)
        self._syncing_scroll = False

    def _clear_highlights(self) -> None:
        """양쪽 편집기의 하이라이트를 모두 제거합니다."""
        self.input_edit.setExtraSelections([])
        self.output_edit.setExtraSelections([])

    def _populate_table(self, mapping: dict[str, str]) -> None:
        self.table.setRowCount(0)
        mono_font = QFont("JetBrains Mono, Consolas, Courier New", 10)

        self._header.set_all_checked(True)

        for orig, alias in mapping.items():
            row = self.table.rowCount()
            self.table.insertRow(row)

            chk_item = QTableWidgetItem()
            chk_item.setCheckState(Qt.CheckState.Checked)
            chk_item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            chk_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            orig_item = QTableWidgetItem(orig)
            orig_item.setForeground(QColor(ORANGE))
            orig_item.setFont(mono_font)

            alias_item = QTableWidgetItem(alias)
            alias_item.setForeground(QColor(ACCENT))
            alias_item.setFont(mono_font)

            self.table.setItem(row, _COL_CHECK, chk_item)
            self.table.setItem(row, _COL_ORIG,  orig_item)
            self.table.setItem(row, _COL_ALIAS, alias_item)
            self.table.setRowHeight(row, 24)