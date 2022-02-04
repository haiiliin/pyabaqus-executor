import sys

from abaqus.Tools.AbaqusExecutor.AbaqusExecutor import AbaqusExecutor
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QSettings

def registerFileRelation():
    className = ".abqjson"
    appPath = QApplication.applicationFilePath().replace('/', '\\')
    ext = ".abqjson"
    extDes = "AbaqusExecutor File"
    baseUrl = "HKEY_CURRENT_USER\\Software\\Classes"
    setting = QSettings(baseUrl, QSettings.NativeFormat)
    setting.setValue("/" + className + "/Shell/Open/Command/.", "\"" + appPath + "\" \"%1\"")
    setting.setValue("/" + className + "/.", extDes)
    setting.setValue("/" + className + "/DefaultIcon/.", appPath + ",0")
    setting.setValue("/" + ext + "/OpenWithProgIds/" + className, "")
    setting.sync()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # registerFileRelation()
    # app.setStyle(QStyleFactory.create("Fusion"))
    abqExecutor = AbaqusExecutor()

    # Open file by dou-click
    if len(sys.argv) > 1 and sys.argv[1].lower().endswith('.abqjson'):
        abqExecutor.new(filePath=sys.argv[1])

    abqExecutor.show()
    sys.exit(app.exec_())
