from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QTableWidget, QTableWidgetItem,
    QHeaderView, QSplitter, QFrame, QStatusBar,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor
import re

from gui.style import ACCENT, ORANGE, BORDER_COLOR, GREEN, DARK_BG, TEXT_PRIMARY, PANEL_BG, TEXT_MUTED, STYLE
from gui.widgets import make_code_panel
from utils import anonymize_code, restore_code

_COL_CHECK = 0   # 체크박스 컬럼
_COL_ORIG  = 1   # ORIGINAL 컬럼
_COL_ALIAS = 2   # ANONYMIZED 컬럼


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.current_mapping: dict[str, str] = {}   # {원본 변수명: 익명 변수명}
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

        # 타이틀 + 서브타이틀
        title_col = QVBoxLayout()
        title_col.setSpacing(2)
        app_title = QLabel("C++ Variable & Function Anonymizer")
        app_title.setObjectName("appTitle")
        subtitle = QLabel("보안 환경 LLM 사용을 위한 변수명 & 함수명 익명화 도구")
        subtitle.setObjectName("appSubtitle")
        title_col.addWidget(app_title)
        title_col.addWidget(subtitle)

        badge = QLabel("SECURE MODE")
        badge.setObjectName("badge")
        badge.setFixedHeight(22)

        self.btn_convert = QPushButton("익명화 ⟶")
        self.btn_convert.setObjectName("convertBtn")
        self.btn_convert.setFixedHeight(40)
        self.btn_convert.setFixedWidth(120)
        self.btn_convert.clicked.connect(self._on_convert)

        self.btn_restore = QPushButton("⟵ 복호화")
        self.btn_restore.setObjectName("restoreBtn")
        self.btn_restore.setFixedHeight(40)
        self.btn_restore.setFixedWidth(120)
        self.btn_restore.clicked.connect(self._on_restore)

        self.btn_clear = QPushButton("초기화")
        self.btn_clear.setObjectName("clearBtn")
        self.btn_clear.setFixedHeight(40)
        self.btn_clear.clicked.connect(self._on_clear)

        header.addLayout(title_col)
        header.addStretch()
        header.addWidget(badge)
        header.addSpacing(12)
        for btn in [self.btn_convert, self.btn_restore, self.btn_clear]:
            header.addWidget(btn)

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

        # 왼쪽: 원본 코드 입력
        left_panel, self.input_edit = make_code_panel(
            "  INPUT — 원본 C++ 코드",
            "C++ 코드를 여기에 붙여넣으세요...",
        )
        # 가운데: 매핑 테이블
        mid_widget = self._build_mapping_panel()
        # 오른쪽: 익명화된 코드 출력 (LLM 결과 붙여넣기 가능)
        right_panel, self.output_edit = make_code_panel(
            "  OUTPUT — 익명화된 코드",
            "익명화된 코드가 여기에 표시됩니다...",
        )

        splitter.addWidget(left_panel)
        splitter.addWidget(mid_widget)
        splitter.addWidget(right_panel)
        splitter.setSizes([500, 300, 500])
        return splitter

    def _build_mapping_panel(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        # 타이틀 행 (레이블 + 갱신 버튼)
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
        layout.addLayout(title_row)

        # 테이블: 체크 / ORIGINAL / ANONYMIZED
        self.table = QTableWidget(0, 3)
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

        n = len(mapping)
        self.count_label.setText(f"변환된 변수: {n}개  ")
        self.status_bar.showMessage(
            f"✓  익명화 완료 — {n}개 변수 치환됨. "
            "체크를 해제한 뒤 [↺ 갱신]으로 일부 변수만 익명화할 수 있습니다."
        )

    def _on_refresh(self) -> None:
        """체크된 항목만 익명화, 해제된 항목은 원본명 그대로 OUTPUT 재생성."""
        if not self.current_mapping:
            self.status_bar.showMessage("⚠  먼저 익명화를 수행해야 합니다.")
            return

        original = self.input_edit.toPlainText()
        if not original.strip():
            self.status_bar.showMessage("⚠  입력 코드가 없습니다.")
            return

        # 체크 여부 읽기
        checked: set[str] = set()
        unchecked: set[str] = set()
        for row in range(self.table.rowCount()):
            chk_item = self.table.item(row, _COL_CHECK)
            orig_item = self.table.item(row, _COL_ORIG)
            if chk_item is None or orig_item is None:
                continue
            orig_name = orig_item.text()
            if chk_item.checkState() == Qt.CheckState.Checked:
                checked.add(orig_name)
            else:
                unchecked.add(orig_name)

        # 체크된 변수만 포함하는 부분 매핑으로 재치환
        active_mapping = {k: v for k, v in self.current_mapping.items() if k in checked}

        result = original
        for orig, alias in active_mapping.items():
            result = re.sub(r'\b' + re.escape(orig) + r'\b', alias, result)

        self.output_edit.setPlainText(result)

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
        self.status_bar.showMessage(
            "✓  복원 완료 — 왼쪽 창에서 원본 변수명으로 복원된 코드를 확인하세요."
        )

    def _on_clear(self) -> None:
        self.input_edit.clear()
        self.output_edit.clear()
        self.table.setRowCount(0)
        self.current_mapping = {}
        self.count_label.setText("변환된 변수: 0개  ")
        self.status_bar.showMessage("초기화되었습니다.")

    # ── 내부 헬퍼 ─────────────────────────────────────────────────────────────

    def _populate_table(self, mapping: dict[str, str]) -> None:
        self.table.setRowCount(0)
        mono_font = QFont("JetBrains Mono, Consolas, Courier New", 10)

        for orig, alias in mapping.items():
            row = self.table.rowCount()
            self.table.insertRow(row)

            # 체크박스 셀 (중앙 정렬)
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