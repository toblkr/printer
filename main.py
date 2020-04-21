import sys
# import Addlayout
# from res import MainPage
# from res.DB import init_db
import MainPage
from DB import  init_db
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery




if __name__ == '__main__':
    app = QApplication(sys.argv)
    # database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    # database.setDatabaseName('test.db')
    init_db()

    # if not database.open():
    #     print("open DB not success.")
    #
    # print('open DB success.')
    # query = QSqlQuery()
    # query.exec_("create table person(id int primary key, name varchar(20), address varchar(30))")


    MainWindow = QMainWindow()
    ui = MainPage.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.init_data()

    MainWindow.show()
    sys.exit(app.exec_())
