import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QColor, QPalette

from gui import MainWindow
from gui.style import DARK_BG, PANEL_BG, TEXT_PRIMARY

LAST_UPDATE, VERSION = "2026.03.20", "*BETA*"

def main() -> None:
    app = QApplication(sys.argv)
    app.setApplicationName("C++ Variable & Function Anonymizer")

    # 다크 팔레트 강제 적용
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window,         QColor(DARK_BG))
    palette.setColor(QPalette.ColorRole.WindowText,     QColor(TEXT_PRIMARY))
    palette.setColor(QPalette.ColorRole.Base,           QColor(PANEL_BG))
    palette.setColor(QPalette.ColorRole.AlternateBase,  QColor(DARK_BG))
    palette.setColor(QPalette.ColorRole.Text,           QColor(TEXT_PRIMARY))
    palette.setColor(QPalette.ColorRole.Button,         QColor(PANEL_BG))
    palette.setColor(QPalette.ColorRole.ButtonText,     QColor(TEXT_PRIMARY))
    app.setPalette(palette)

    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    print("ⓒ 2026,LIG Nex1, YoungSuh Lee, All rights reserved.")
    print(f"Last Revision : {VERSION} Distributed on {LAST_UPDATE} ")
    print("\nInit Complete & GUI created!")
    try:
        main()
    except Exception as e:
        print(e)

