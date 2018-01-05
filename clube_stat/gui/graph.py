
import sys

import os
from PyQt5 import QtWidgets, uic

from clube_stat import pth

root = os.path.join(os.path.dirname(__file__))
ui_pth = os.path.join(root, "ui/graph_form.ui")

class GraphicsWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # self.clubs_object = clubs_object
        # self.pxm = None
        # self.current_club_name = None
        # self.db_path = db_path
        # self.resize(500, 500)
        self.form = uic.loadUi(ui_pth, self)
        # self.setWindowTitle("Graphics")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = GraphicsWidget()
    main.show()
    sys.exit(app.exec_())

