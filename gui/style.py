# ─── 색상 팔레트 ─────────────────────────────────────────────────────────────

DARK_BG      = "#0f1117"
PANEL_BG     = "#1a1d27"
BORDER_COLOR = "#2a2d3e"
ACCENT       = "#4f9cf9"
ACCENT2      = "#7c3aed"
TEXT_PRIMARY = "#e8eaf0"
TEXT_MUTED   = "#6b7280"
GREEN        = "#22c55e"
ORANGE       = "#f59e0b"

# ─── 전역 QSS 스타일시트 ──────────────────────────────────────────────────────

STYLE = f"""
QMainWindow {{
    background: {DARK_BG};
}}
QWidget {{
    background: {DARK_BG};
    color: {TEXT_PRIMARY};
    font-family: 'JetBrains Mono', 'Consolas', 'Courier New', monospace;
}}
QTextEdit {{
    background: {PANEL_BG};
    color: {TEXT_PRIMARY};
    border: 1px solid {BORDER_COLOR};
    border-radius: 8px;
    padding: 12px;
    font-family: 'JetBrains Mono', 'Consolas', 'Courier New', monospace;
    font-size: 13px;
    selection-background-color: {ACCENT};
}}
QTextEdit:focus {{
    border: 1px solid {ACCENT};
}}
QTableWidget {{
    background: {PANEL_BG};
    color: {TEXT_PRIMARY};
    border: 1px solid {BORDER_COLOR};
    border-radius: 8px;
    gridline-color: {BORDER_COLOR};
    font-size: 12px;
}}
QTableWidget::item {{
    padding: 6px 10px;
    border: none;
}}
QTableWidget::item:selected {{
    background: rgba(79,156,249,0.2);
    color: {TEXT_PRIMARY};
}}
QHeaderView::section {{
    background: #12151e;
    color: {TEXT_MUTED};
    border: none;
    border-bottom: 1px solid {BORDER_COLOR};
    padding: 8px 10px;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 1px;
    text-transform: uppercase;
}}
QPushButton#convertBtn {{
    background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
        stop:0 {ACCENT}, stop:1 #6366f1);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 28px;
    font-size: 13px;
    font-weight: bold;
    font-family: 'Segoe UI', sans-serif;
    letter-spacing: 0.5px;
}}
QPushButton#convertBtn:hover {{
    background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
        stop:0 #60a5fa, stop:1 #818cf8);
}}
QPushButton#convertBtn:pressed {{
    background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
        stop:0 #3b82f6, stop:1 #6366f1);
}}
QPushButton#restoreBtn {{
    background: transparent;
    color: {GREEN};
    border: 1px solid {GREEN};
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 13px;
    font-weight: bold;
    font-family: 'Segoe UI', sans-serif;
}}
QPushButton#restoreBtn:hover {{
    background: rgba(34,197,94,0.1);
}}
QPushButton#clearBtn {{
    background: transparent;
    color: {TEXT_MUTED};
    border: 1px solid {BORDER_COLOR};
    border-radius: 8px;
    padding: 10px 16px;
    font-size: 12px;
    font-family: 'Segoe UI', sans-serif;
}}
QPushButton#clearBtn:hover {{
    color: {TEXT_PRIMARY};
    border-color: {TEXT_MUTED};
}}
QLabel#panelTitle {{
    color: {TEXT_MUTED};
    font-size: 10px;
    font-family: 'Segoe UI', sans-serif;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: bold;
    padding: 4px 0px;
}}
QLabel#appTitle {{
    color: {TEXT_PRIMARY};
    font-size: 20px;
    font-family: 'Segoe UI', 'Arial', sans-serif;
    font-weight: bold;
    letter-spacing: -0.5px;
}}
QLabel#appSubtitle {{
    color: {TEXT_MUTED};
    font-size: 11px;
    font-family: 'Segoe UI', sans-serif;
}}
QLabel#badge {{
    background: rgba(79,156,249,0.15);
    color: {ACCENT};
    border: 1px solid rgba(79,156,249,0.3);
    border-radius: 4px;
    padding: 2px 8px;
    font-size: 10px;
    font-family: 'Segoe UI', sans-serif;
    font-weight: bold;
}}
QStatusBar {{
    background: #0a0c12;
    color: {TEXT_MUTED};
    border-top: 1px solid {BORDER_COLOR};
    font-size: 11px;
    font-family: 'Segoe UI', sans-serif;
}}
QSplitter::handle {{
    background: {BORDER_COLOR};
    width: 1px;
}}
QScrollBar:vertical {{
    background: {PANEL_BG};
    width: 8px;
    border-radius: 4px;
}}
QScrollBar::handle:vertical {{
    background: {BORDER_COLOR};
    border-radius: 4px;
    min-height: 20px;
}}
QScrollBar::handle:vertical:hover {{
    background: {TEXT_MUTED};
}}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0;
}}
"""
