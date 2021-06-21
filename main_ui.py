'''
# Name: main_ui.py
# Aim: The main() of Expense Manager project. All the functions of expense_manager.py are called here
# Start date: 14.June 2021
# End date: ---
# Files associated with this: expense_manger.py, repair_csv_files.py
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from expense_manager import ExpMngr

exp_mngr = ExpMngr()
main_app = QApplication(sys.argv)
window = QWidget()

# the main home page
window = exp_mngr.homepage_window()
grid = exp_mngr.homepage_frame_grid()

window.setLayout(grid)
window.show()
sys.exit(main_app.exec())
