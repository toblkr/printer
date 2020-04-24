# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os, datetime
from datetime import datetime,timedelta,date
import datetime as dt

from PyQt5 import QtCore, QtGui, QtWidgets
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import xlrd

import AddCustomer, Print
from DB import Customer,db_link
from main import logger

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(873, 591)
        MainWindow.setMaximumSize(QtCore.QSize(900, 780))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
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
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
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
        self.tableWidget.setColumnWidth(1, 50)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 150)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setColumnWidth(6, 80)
        self.tableWidget.setColumnWidth(7,500)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_2 = QtWidgets.QFrame(self.MainPage)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_customer_button = QtWidgets.QPushButton(self.MainPage)
        self.add_customer_button.setObjectName("add_customer_button")
        self.horizontalLayout.addWidget(self.add_customer_button)
        self.import_button = QtWidgets.QPushButton(self.MainPage)
        self.import_button.setObjectName("import_button")
        self.horizontalLayout.addWidget(self.import_button)
        self.delete_button = QtWidgets.QPushButton(self.MainPage)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.print_button = QtWidgets.QPushButton(self.MainPage)
        self.print_button.setObjectName("print_button")
        self.horizontalLayout.addWidget(self.print_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.MainPage, 2, 0, 1, 1)
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
        self.lookup = QtWidgets.QLineEdit(self.frame)
        self.lookup.setObjectName("lookup")
        self.horizontalLayout_13.addWidget(self.lookup)
        self.find_button = QtWidgets.QPushButton(self.frame)
        self.find_button.setObjectName("find_button")
        self.horizontalLayout_13.addWidget(self.find_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 23))
        self.menubar.setObjectName("menubar")
        self.menuImport = QtWidgets.QMenu(self.menubar)
        self.menuImport.setObjectName("menuImport")
        MainWindow.setMenuBar(self.menubar)
        self.actionImport_From_Excel = QtWidgets.QAction(MainWindow)
        self.actionImport_From_Excel.setObjectName("actionImport_From_Excel")
        self.actionExport_Excel = QtWidgets.QAction(MainWindow)
        self.actionExport_Excel.setObjectName("actionExport_Excel")
        # self.actionExport_Selected = QtWidgets.QAction(MainWindow)
        # self.actionExport_Selected.setObjectName("actionExport_Selected")
        self.actionExport_Sample = QtWidgets.QAction(MainWindow)
        self.actionExport_Sample.setObjectName("actionExport_Sample")
        self.menuImport.addAction(self.actionImport_From_Excel)
        self.menuImport.addAction(self.actionExport_Excel)
        # self.menuImport.addAction(self.actionExport_Selected)
        self.menuImport.addAction(self.actionExport_Sample)
        self.menubar.addAction(self.menuImport.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.selected = []
        self.current_customer = {}
        self.current_list = []
        self.cwd = os.getcwd()

        # self.tableWidget.cellClicked.connect(self.check)
        self.tableWidget.doubleClicked.connect(self.double_clicked)

        # self.actionExport_Excel.triggered.connect(self.export_to_file)
        proc_start = QtCore.pyqtSignal()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Customer Printing"))
        self.label_2.setText(_translate("MainWindow", "Customer List"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Cust. ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Batch"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Contact Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Company Name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Market Group"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "City"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Postcode"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Address"))
        self.add_customer_button.setText(_translate("MainWindow", "Add Customer"))
        self.import_button.setText(_translate("MainWindow", "Import From File"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))
        self.print_button.setText(_translate("MainWindow", "Print"))
        self.label_18.setText(_translate("MainWindow", "Customer Lookup: "))
        self.find_button.setText(_translate("MainWindow", "Find"))
        self.menuImport.setTitle(_translate("MainWindow", "File"))
        self.actionImport_From_Excel.setText(_translate("MainWindow", "Import From Excel"))
        self.actionExport_Excel.setText(_translate("MainWindow", "Export All"))
        # self.actionExport_Selected.setText(_translate("MainWindow", "Export Selected"))
        self.actionExport_Sample.setText(_translate("MainWindow", "Export Sample FIle"))

        self.find_button.clicked.connect(self.search_customer)
        self.lookup.returnPressed.connect(self.search_customer)
        self.delete_button.clicked.connect(self.delete)
        self.actionExport_Excel.triggered.connect(self.export_to_file)
        self.import_button.clicked.connect(self.import_from_file)
        self.actionImport_From_Excel.triggered.connect(self.import_from_file)
        self.actionExport_Sample.triggered.connect(self.export_sample)
        self.add_customer_button.clicked.connect(self.add_customer)
        self.print_button.clicked.connect(self.print_page)

    def init_data(self):
        # read all from current database
        self.clear()
        engine = create_engine(db_link, echo=False)
        metadata = MetaData(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        rows = session.query(Customer)
        for each_customer in rows:
            current_customer = {}
            current_customer['id'] = each_customer.id
            current_customer['batch'] = each_customer.batch

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
            current_customer['address'] = (address_one.strip(',') + ',' + \
                                          address_two.strip(',') + ',' + \
                                          address_three.strip(',')).strip(',')
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
        self.selected = []

    def clear(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)

    def load_data(self):
        for i in range(len(self.current_list)):
            self.add_row(self.current_list[i])

    def add_row(self, customer):
        numRows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(numRows)
        self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(customer['id']))
        self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(customer['batch']))
        self.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(customer['contact']))
        self.tableWidget.setItem(numRows, 3, QtWidgets.QTableWidgetItem(customer['company']))
        self.tableWidget.setItem(numRows, 4, QtWidgets.QTableWidgetItem(customer['market']))
        self.tableWidget.setItem(numRows, 5, QtWidgets.QTableWidgetItem(customer['city']))
        self.tableWidget.setItem(numRows, 6, QtWidgets.QTableWidgetItem(customer['post_code']))
        self.tableWidget.setItem(numRows, 7, QtWidgets.QTableWidgetItem(customer['address']))

    def check_item(self):
        print(self.tableWidget.selectionModel().selectedRows())
        self.selected = []
        for index in self.tableWidget.selectionModel().selectedRows():
            print(index.sibling(index.row(), 0).data())
            item = index.sibling(index.row(), 0).data()
            self.selected.append(item)

        print(self.selected)

        # item = self.tableWidget.itemAt(row, column).text()
        # print(item)
        # if item in self.selected:
        #     self.selected.remove(item)
        # else:
        #     self.selected.append(item)
        # print(self.selected)

    def double_clicked(self, mi):
        # go to detail page
        try:
            row = mi.row()
            column = mi.column()
            # print(row)
            # print(column)
            customer_id = self.tableWidget.item(row, 0).text()
            self.add_customer(customer_id)

        except Exception as err:
            print(err)
            logger.info(err, exc_info=True)
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText(err)
            x = msg.exec_()


    def redirect(self, customer_id):
        self.window = QtWidgets.QDialog()
        self.ui = AddCustomer.Ui_CustomerPage()
        print('coming')
        self.ui.setupUi(self.window)
        self.window.show()
        # self.close()

    def add_customer(self, customer_id=None):
        try:
            if customer_id is None:
                self.window = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
                self.ui = AddCustomer.Ui_Dialog()
                # self.window.setWindowFlag()

                self.ui.setupUi(self.window)

                self.window.show()
                self.ui.the_signal.connect(self.init_data)
                self.ui.the_signal2.connect(self.search_customer_from_add)
            else:
                print('1')
                self.window = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
                self.ui = AddCustomer.Ui_Dialog()
                self.ui.setupUi(self.window, customer_id)

                self.window.show()
                self.ui.the_signal.connect(self.init_data)
                self.ui.the_signal2.connect(self.search_customer_from_add)
        except Exception as err:
            logger.info(err, exc_info=True)
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText(err)
            x = msg.exec_()

    # @QtCore.pyqtSlot(str)
    def search_customer_from_add(self, message):
        print(message)
        try:
            self.clear()
            from sqlalchemy import or_
            engine = create_engine(db_link, echo=False)
            metadata = MetaData(engine)
            Session = sessionmaker(bind=engine)
            session = Session()
            word = message
            search = "%{}%".format(word)
            print(search)
            # customer = session.query(Customer).all()
            customers = session.query(Customer).filter(or_(Customer.address_one.like(search),
                                                           Customer.address_two.like(search),
                                                           Customer.contact_name.like(search),
                                                           Customer.id.like(search),
                                                           Customer.company_name.like(search),
                                                           Customer.market_group.like(search),
                                                           Customer.batch.like(search),
                                                           Customer.city.like(search)))
            if len(customers.all()) == 0:
                # pop a dialog to tell no found
                print('0')
                self.label_2.setText('No record found')
            else:
                # show in widget
                self.label_2.setText('{} records found'.format(len(customers.all())))
                for each_customer in customers:
                    current_customer = dict()
                    current_customer['id'] = each_customer.id
                    current_customer['batch'] = each_customer.batch

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
                    current_customer['address'] = (address_one.strip(',') + ',' + \
                                                   address_two.strip(',') + ',' + \
                                                   address_three.strip(',')).strip(',')
                    self.current_list.append(current_customer)
                self.load_data()
                self.reset()
            session.close()
        except Exception as err:
            logger.info(err, exc_info=True)
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText(err)
            x = msg.exec_()

    def search_customer(self, kw=None):
        print(kw)
        try:
            self.clear()
            from sqlalchemy import or_
            engine = create_engine(db_link, echo=False)
            metadata = MetaData(engine)
            Session = sessionmaker(bind=engine)
            session = Session()
            if kw:
                word = kw
            else:
                word = self.lookup.text()
            search = "%{}%".format(word)
            print(search)
            # customer = session.query(Customer).all()
            customers = session.query(Customer).filter(or_(Customer.address_one.like(search),
                                                           Customer.address_two.like(search),
                                                           Customer.contact_name.like(search),
                                                           Customer.id.like(search),
                                                           Customer.company_name.like(search),
                                                           Customer.market_group.like(search),
                                                           Customer.batch.like(search),
                                                           Customer.city.like(search)))
            if len(customers.all()) == 0:
                # pop a dialog to tell no found
                print('0')
                self.label_2.setText('No record found')
            else:
                # show in widget
                self.label_2.setText('{} records found'.format(len(customers.all())))
                for each_customer in customers:
                    current_customer = dict()
                    current_customer['id'] = each_customer.id
                    current_customer['batch'] = each_customer.batch

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
                    current_customer['address'] = (address_one.strip(',') + ',' + \
                                                   address_two.strip(',') + ',' + \
                                                   address_three.strip(',')).strip(',')
                    self.current_list.append(current_customer)
                self.load_data()
                self.reset()
            session.close()
        except Exception as err:
            logger.info(err, exc_info=True)
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText(err)
            x = msg.exec_()

    def popup_button(self, i):
        print(i.text())
        if i.text() == '&Yes':
            print('deleting')
            try:
                print(self.selected)
                to_delete = self.selected
                engine = create_engine(db_link, echo=False)
                metadata = MetaData(engine)
                Session = sessionmaker(bind=engine)
                session = Session()
                session.query(Customer).filter(Customer.id.in_(to_delete)).delete(synchronize_session=False)
                session.commit()
                # remove clicked status
                self.selected = []
                # self.tableWidget.row
                self.clear()
                self.init_data()
            except Exception as err:
                logger.info(err, exc_info=True)
            finally:
                session.close()
        else:
            pass

    def delete(self):
        try:
            self.check_item()
            msg = QMessageBox()
            msg.setWindowTitle("Delete")
            msg.setText("Do you want to delete {} record? You will lose your data".format(len(self.selected)))
            msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
            msg.setDefaultButton(QMessageBox.No)
            msg.buttonClicked.connect(self.popup_button)
            x = msg.exec_()

        except Exception as err:
            logger.info(err, exc_info=True)
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText(err)
            x = msg.exec_()

    def print_page(self):
        # go to print page with a list
        try:
            self.check_item()
            self.window = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
            list_to_print = self.selected
            self.ui = Print.Ui_Dialog()
            # self.ui = Print.Window(customer_list=list_to_print)

            print(list_to_print)

            self.ui.setupUi(self.window, list_to_print)
            self.window.show()
            self.ui.init_data()
        except Exception as err:
            print(err)
            logger.info(err, exc_info=True)

    def import_from_file(self):
        engine = create_engine(db_link, echo=False)
        metadata = MetaData(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        print('importing')
        try:
            file_dialog = QFileDialog()
            file_name, _ = QFileDialog.getOpenFileName(file_dialog, "Import Data", self.cwd,
                                                       "Excel Workbook(*.xlsx);;Excel 97-Excel 2003 Workbook(*.xls)")
            if file_name:
                # print(file_name)
                # load data into database
                workbook = xlrd.open_workbook(file_name)
                worksheet = workbook.sheet_by_index(0)

                rows = []
                for i in range(1,worksheet.nrows):
                    # print(worksheet.row_values(i))
                    id = worksheet.row_values(i)[0]
                    cus = session.query(Customer).filter_by(id=id).first()

                    while session.query(Customer).filter_by(id=id).first():
                        # print(id)
                        if len(id) > 3 and id[-3] == '(' and id[-1] == ')' and id[-2].isdigit():
                            # print(cus.id)
                            # print(str(int(id[-2])+1))
                            try:
                                id = id[:-2] + str(int(id[-2]) + 1) + id[-1]
                                # print(id)
                            except Exception as err:
                                print(err)
                        else:
                            id = id + '(1)'


                    batch = worksheet.row_values(i)[1]
                    company_name = worksheet.row_values(i)[2]
                    contact_name = worksheet.row_values(i)[3]
                    title = worksheet.row_values(i)[4]
                    other_title = worksheet.row_values(i)[5]
                    first_name = worksheet.row_values(i)[6]
                    last_name = worksheet.row_values(i)[7]
                    market_group = worksheet.row_values(i)[8]
                    address_one = worksheet.row_values(i)[9]
                    address_two = worksheet.row_values(i)[10]
                    address_three = worksheet.row_values(i)[11]
                    phone_number_prefix = worksheet.row_values(i)[12]

                    phone_number = worksheet.row_values(i)[13]
                    fax_number_prefix = worksheet.row_values(i)[14]
                    fax_number = worksheet.row_values(i)[15]
                    city = worksheet.row_values(i)[16]
                    post_code = worksheet.row_values(i)[17]
                    country = worksheet.row_values(i)[18]
                    notes = worksheet.row_values(i)[19]
                    email_one = worksheet.row_values(i)[20]
                    email_two = worksheet.row_values(i)[21]
                    email_three = worksheet.row_values(i)[22]
                    excel_create_date = worksheet.row_values(i)[23]
                    excel_update_date = worksheet.row_values(i)[24]
                    # print(type(excel_create_date))
                    # print(int(excel_create_date))
                    # print(round(excel_create_date))

                    create_date = xlrd.xldate_as_datetime(float(excel_create_date), 0)
                    update_date = xlrd.xldate_as_datetime(float(excel_update_date), 0)
                    # update_date = datetime.datetime(*xlrd.xldate_as_tuple(excel_update_date,workbook.datemode))


                    # print(create_date)
                    # print(type(create_date))

                    session.add(Customer(id=id,batch=batch,company_name=company_name,contact_name=contact_name,title=title,other_title=other_title,
                                         first_name=first_name,last_name=last_name,market_group=market_group,address_one=address_one,
                                         address_two=address_two,address_three=address_three,phone_number_prefix=phone_number_prefix,country=country,
                                         phone_number=phone_number,fax_number_prefix=fax_number_prefix,fax_number=fax_number,city=city,
                                         post_code=post_code,notes=notes,email_one=email_one,email_two=email_two,email_three=email_three,create_date=create_date
                                         ,update_date=update_date))
                # print(rows)
                # print(rows[0])
                # print(rows[0].id)
                # print(rows[1].id)
                # print(rows[2].id)
                # print(rows[3].id)
                # print(rows[4].id)
                # try:
                #     # session.bulk_save_objects(rows)
                # except Exception as err:
                #     print(err)
                print('end')
                session.commit()
                session.close()
                self.clear()
                self.init_data()
            else:
                print('erer')
                pass
        except Exception as err:
            session.rollback()
            logger.info(err, exc_info=True)
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText(err)
            x = msg.exec_()

        finally:
            session.close()

    def export_to_file(self):
        import xlsxwriter

        file_dialog = QFileDialog()
        file_name, _ = QFileDialog.getSaveFileName(file_dialog,'Export',self.cwd, "Excel Workbook(*.xlsx);;Excel 97-Excel 2003 Workbook(*.xls)"
                                                       )
        print(type(file_name))
        print(type(_))
        if file_name != '':
            try:
                workbook = xlsxwriter.Workbook(file_name)
                format1 = workbook.add_format({'num_format': 'yyyy-mm-dd'})
                sheet = workbook.add_worksheet()

                engine = create_engine(db_link, echo=False)
                metadata = MetaData(engine)
                Session = sessionmaker(bind=engine)
                session = Session()
                rows = session.query(Customer)

                col = ['id','batch','company_name','contact_name','title','other_title','first_name','last_name','market_group','address_one','address_two',
                        'address_three','phone_number_prefix','phone_number','fax_number_prefix','fax_number','city','post_code','country','notes','email_one','email_two',
                       'email_three','create_date','update_date']
                print(len(col))
                for i in range(0, len(col)):
                    sheet.write(0, i, col[i])
                j = 1
                for row in rows:
                    sheet.write(j, 0, row.id)
                    sheet.write(j, 1, row.batch)
                    sheet.write(j, 2, row.company_name)
                    sheet.write(j, 3, row.contact_name)
                    sheet.write(j, 4, row.title)
                    sheet.write(j, 5, row.other_title)
                    sheet.write(j, 6, row.first_name)
                    sheet.write(j, 7, row.last_name)
                    sheet.write(j, 8, row.market_group)
                    sheet.write(j, 9, row.address_one)
                    sheet.write(j, 10, row.address_two)
                    sheet.write(j, 11, row.address_three)
                    sheet.write(j, 12, row.phone_number_prefix)
                    sheet.write(j, 13, row.phone_number)
                    sheet.write(j, 14, row.fax_number_prefix)
                    sheet.write(j, 15, row.fax_number)
                    sheet.write(j, 16, row.city)
                    sheet.write(j, 17, row.post_code)
                    sheet.write(j, 18, row.country)
                    sheet.write(j, 19, row.notes)
                    sheet.write(j, 20, row.email_one)
                    sheet.write(j, 21, row.email_two)
                    sheet.write(j, 22, row.email_three)
                    sheet.write(j, 23, row.create_date,format1)
                    sheet.write(j, 24, row.update_date,format1)
                    j += 1
                workbook.close()
                print(file_name)
            except Exception as err:
                logger.info(err, exc_info=True)
                os.remove(file_name)
        else:
            pass

    def export_sample(self):
        import xlsxwriter

        file_dialog = QFileDialog()
        file_name, _ = QFileDialog.getSaveFileName(file_dialog, 'Export', self.cwd,
                                                   "Excel Workbook(*.xlsx);;Excel 97-Excel 2003 Workbook(*.xls)")
        if file_name != '':
            try:
                workbook = xlsxwriter.Workbook(file_name)
                format1 = workbook.add_format({'num_format': 'yyyy-mm-dd'})
                sheet = workbook.add_worksheet()

                # engine = create_engine('sqlite:///test2.db', echo=False)
                # metadata = MetaData(engine)
                # Session = sessionmaker(bind=engine)
                # session = Session()
                # rows = session.query(Customer)

                col = ['id', 'batch', 'company_name', 'contact_name', 'title', 'other_title', 'first_name', 'last_name',
                       'market_group', 'address_one', 'address_two',
                       'address_three', 'phone_number_prefix', 'phone_number', 'fax_number_prefix', 'fax_number', 'city',
                       'post_code', 'country', 'notes', 'email_one', 'email_two',
                       'email_three', 'create_date', 'update_date']
                print(len(col))
                for i in range(0, len(col)):
                    sheet.write(0, i, col[i])
                j = 1
                # for row in rows:
                sheet.write(j, 0, 'A1234')
                sheet.write(j, 1, 'B20200420')
                sheet.write(j, 2, 'A company')
                sheet.write(j, 3, "Leo")
                sheet.write(j, 4, 'mrs')
                sheet.write(j, 5, '')
                sheet.write(j, 6, 'leo')
                sheet.write(j, 7, '')
                sheet.write(j, 8, 'Auckland')
                sheet.write(j, 9, 'No. 14 Prince St.')
                sheet.write(j, 10, 'Canterbury, Auckland')
                sheet.write(j, 11, 'NZ')
                sheet.write(j, 12, '020')
                sheet.write(j, 13, '45671234')
                sheet.write(j, 14, '020')
                sheet.write(j, 15, '595857213')
                sheet.write(j, 16, 'Auckland')
                sheet.write(j, 17, '0115')
                sheet.write(j, 18, 'New Zealand')
                sheet.write(j, 19, 'Need to deliver in three days')
                sheet.write(j, 20, 'leo@gmail.com')
                sheet.write(j, 21, '')
                sheet.write(j, 22, '')
                print(dt.date.today())
                sheet.write(j, 23, dt.date.today(), format1)
                sheet.write(j, 24, dt.date.today(), format1)

                workbook.close()
                print(file_name)
            except Exception as err:
                logger.info(err, exc_info=True)
                # os.remove(file_name)
        else:
            pass

    # @QtCore.pyqtSlot()
    def receive(self):
        print('received ')
