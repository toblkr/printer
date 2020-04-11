# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


import Addlayout
from DB import Customer


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMaximumSize(QtCore.QSize(700, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setMinimumSize(QtCore.QSize(80, 0))
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_13.addWidget(self.label_18)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.horizontalLayout_13.addWidget(self.lineEdit_17)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_13.addWidget(self.pushButton_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.MainPage = QtWidgets.QFrame(self.centralwidget)
        self.MainPage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainPage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainPage.setObjectName("MainPage")
        self.gridLayout = QtWidgets.QGridLayout(self.MainPage)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.MainPage)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.tableWidget = QtWidgets.QTableWidget(self.MainPage)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.MainPage)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.MainPage)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.MainPage)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.MainPage, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 23))
        self.menubar.setObjectName("menubar")
        self.menuImport = QtWidgets.QMenu(self.menubar)
        self.menuImport.setObjectName("menuImport")
        MainWindow.setMenuBar(self.menubar)
        self.actionImport_From_Excel = QtWidgets.QAction(MainWindow)
        self.actionImport_From_Excel.setObjectName("actionImport_From_Excel")
        self.actionExport_Excel = QtWidgets.QAction(MainWindow)
        self.actionExport_Excel.setObjectName("actionExport_Excel")
        self.menuImport.addAction(self.actionImport_From_Excel)
        self.menuImport.addAction(self.actionExport_Excel)
        self.menubar.addAction(self.menuImport.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.selected = []
        self.current_customer = {}
        self.current_list = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_18.setText(_translate("MainWindow", "Customer Lookup: "))
        self.pushButton_4.setText(_translate("MainWindow", "Find"))
        self.label_2.setText(_translate("MainWindow", "Customer List"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Contact Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Market Group"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Company Name"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "City"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Phone Number"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Address"))
        self.label.setText(_translate("MainWindow", "Check the customers you want to delete or print"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.pushButton.setText(_translate("MainWindow", "Print"))
        self.menuImport.setTitle(_translate("MainWindow", "File"))
        self.actionImport_From_Excel.setText(_translate("MainWindow", "Import From Excel"))
        self.actionExport_Excel.setText(_translate("MainWindow", "Export Excel"))

        # QtCore.QTimer.singleShot(1,self.init_data)

        self.tableWidget.cellClicked.connect(self.check)
        # self.tableWidget.cellDoubleClicked.connect(self.double_clicked)

        # self.pushButton.clicked.connect(self.add_row)
        self.pushButton_2.clicked.connect(self.redirect)

    def init_data(self):
        # read all from current database
        engine = create_engine('sqlite:///test2.db', echo=False)
        metadata = MetaData(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        print(session.query(Customer).first())
        print(self.current_customer)
        rows = session.query(Customer)
        for each_customer in rows:
            current_customer = {}
            current_customer['id'] = each_customer.id
            current_customer['title'] = each_customer.title

            first_name = '' if each_customer.first_name is None else each_customer.first_name
            last_name = '' if each_customer.first_name is None else each_customer.last_name
            current_customer['contact'] = first_name + ' ' + last_name

            company_name = '' if each_customer.company_name is None else each_customer.company_name
            current_customer['company'] = company_name

            market_group = '' if each_customer.market_group is None else each_customer.market_group
            current_customer['market'] = market_group

            city = '' if each_customer.city is None else each_customer.city
            current_customer['city'] = city

            post_code = '' if each_customer.post_code is None else each_customer.post_code
            current_customer['post_code'] = post_code

            address_one = '' if each_customer.address_one is None else each_customer.address_one
            address_two = '' if each_customer.address_two is None else each_customer.address_two
            address_three = '' if each_customer.address_three is None else each_customer.address_three
            current_customer['address'] = address_one.strip(',') + ',' + \
                                               address_two.strip(',') + ',' + \
                                               address_three.strip(',')
            # print(self.current_customer)

            # print(self.current_list)
            self.current_list.append(current_customer)
            # print(self.current_list)

        # get
        self.load_data()
        self.reset()
        session.close()

    def reset(self):
        # self.current_customer = {}
        self.current_list = []

    def clear(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)

    def load_data(self):
        for i in range(len(self.current_list)):
            self.add_row(self.current_list[i])
            # print('added item')

    def add_row(self, customer):
        numRows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(numRows)
        self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(customer['id']))
        self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(customer['title']))
        self.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(customer['contact']))
        self.tableWidget.setItem(numRows, 3, QtWidgets.QTableWidgetItem(customer['company']))
        self.tableWidget.setItem(numRows, 4, QtWidgets.QTableWidgetItem(customer['market']))
        self.tableWidget.setItem(numRows, 5, QtWidgets.QTableWidgetItem(customer['city']))
        self.tableWidget.setItem(numRows, 6, QtWidgets.QTableWidgetItem(customer['post_code']))
        self.tableWidget.setItem(numRows, 7, QtWidgets.QTableWidgetItem(customer['address']))

    def check(self, row, column):
        print(self.tableWidget.selectionModel().selectedRows())
        for index in self.tableWidget.selectionModel().selectedRows():
            print(index.sibling(index.row(),0).data())
        item = self.tableWidget.itemAt(row, column).text()
        if item in self.selected:
            self.selected.remove(item)
        else:
            self.selected.append(item)
        # print(item)
        # print(self.selected)

    def double_clicked(self, row, column):
        # go to detail page
        customer_id = self.tableWidget.itemAt(row, column)
        self.add_customer(customer_id)

    def redirect(self):
        self.window = QtWidgets.QDialog()
        self.ui = Addlayout.Ui_CustomerPage()
        print('coming')
        self.ui.setupUi(self.window)

        self.window.show()
        # self.close()

    def add_customer(self, customer_id=None):
        if customer_id is None:
            self.window = QtWidgets.QDialog()
            self.ui = Addlayout.Ui_CustomerPage()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.window = QtWidgets.QDialog()
            self.ui = Addlayout.Ui_CustomerPage(customer_id)
            self.ui.setupUi(self.window)
            self.window.show()

    def lookup(self, word):
        from sqlalchemy import or_
        engine = create_engine('sqlite:///test2.db', echo=False)
        metadata = MetaData(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        search = "%{}%".format(word)
        print(search)
        customer = session.query(Customer).filter(or_(Customer.address_one.like(search),
                                                    Customer.address_two.like(search),
                                                    Customer.contact_name.like(search),
                                                    Customer.id.like(search),
                                                    Customer.company_name.like(search),
                                                    Customer.market_group.like(search),
                                                    Customer.city.like(search)))
        if len(customer.all()) == 0:
            # pop a dialog to tell no found
            return 0
        else:
            # show in widget
            for each_customer in session.query(customer):
                self.current_customer['id'] = each_customer.id
                self.current_customer['title'] = each_customer.title
                self.current_customer['contact'] = each_customer.first_name + ' ' + each_customer.last_name
                self.current_customer['company'] = each_customer.company_name
                self.current_customer['market'] = each_customer.market_group
                self.current_customer['city'] = each_customer.city
                self.current_customer['post_code'] = each_customer.post_code
                self.current_customer['address'] = each_customer.address_one.strip(',') + ',' + \
                                                   each_customer.address_two.strip(',') + ',' + \
                                                   each_customer.address_three.strip(',')
                self.current_list.append(self.current_customer)
            self.load_data()
            self.reset()
        session.close()

    def popup(self, message):
        pass

    def delete(self):
        pass

    def print(self):
        # go to print page with a list
        pass

    def import_from_file(self):
        pass

    def export_to_file(self):
        pass


