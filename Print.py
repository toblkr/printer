# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Print.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from DB import Customer, Sender, db_link
from sqlalchemy import create_engine, MetaData, Table, func
from sqlalchemy.orm import sessionmaker

import win32ui, win32print, win32con
from main import logger

class Ui_Dialog(QtCore.QObject):
    x_100 = 10
    x_80 = 110
    y_100_distance = 72
    y_80_distance = 55
    y_100 = 20
    y_80 = 20
    length_100 = 650
    length_80 = 590
    current_index = 0
    resized = QtCore.pyqtSignal()
    current_sender = {}
    records_number = 0
    font_80 = 13
    font_100 = 17

    def setupUi(self, Dialog, customer_list):
        Dialog.setObjectName("Dialog")
        Dialog.resize(861, 637)

        try:
            Dialog.resizeEvent = self.changeEvent
        except Exception as err:
            logger.info(err, exc_info=True)
            print(err)
        self.gridLayout_5 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_5 = QtWidgets.QFrame(Dialog)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.printer_box = QtWidgets.QComboBox(self.frame_5)
        self.printer_box.setMinimumSize(QtCore.QSize(120, 0))
        self.printer_box.setObjectName("printer_box")
        # self.printer_box.addItem("")
        # self.printer_box.addItem("")
        self.horizontalLayout_2.addWidget(self.printer_box)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setMinimumSize(QtCore.QSize(60, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.tag_size_box = QtWidgets.QComboBox(self.frame_5)
        self.tag_size_box.setMinimumSize(QtCore.QSize(120, 0))
        self.tag_size_box.setObjectName("tag_size_box")
        self.tag_size_box.addItem("")
        self.tag_size_box.addItem("")
        self.horizontalLayout.addWidget(self.tag_size_box)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.frame_5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.sender_name = QtWidgets.QLineEdit(self.frame_5)
        self.sender_name.setObjectName("sender_name")
        self.horizontalLayout_5.addWidget(self.sender_name)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setMinimumSize(QtCore.QSize(72, 0))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.sender_company = QtWidgets.QLineEdit(self.frame_5)
        self.sender_company.setObjectName("sender_company")
        self.horizontalLayout_3.addWidget(self.sender_company)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setMinimumSize(QtCore.QSize(72, 0))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.sender_phone = QtWidgets.QLineEdit(self.frame_5)
        self.sender_phone.setObjectName("sender_phone")
        self.horizontalLayout_6.addWidget(self.sender_phone)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        self.label_10.setMinimumSize(QtCore.QSize(72, 0))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.sender_city = QtWidgets.QLineEdit(self.frame_5)
        self.sender_city.setObjectName("sender_city")
        self.horizontalLayout_7.addWidget(self.sender_city)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 2, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.new_sender_button = QtWidgets.QPushButton(self.frame_5)
        self.new_sender_button.setObjectName("new_sender_button")
        self.verticalLayout_9.addWidget(self.new_sender_button)
        self.save_sender_button = QtWidgets.QPushButton(self.frame_5)
        self.save_sender_button.setObjectName("save_sender_button")
        self.verticalLayout_9.addWidget(self.save_sender_button)
        self.gridLayout_4.addLayout(self.verticalLayout_9, 0, 5, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame_5)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        self.label_14 = QtWidgets.QLabel(self.frame_5)
        self.label_14.setMinimumSize(QtCore.QSize(60, 0))
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_11.addWidget(self.label_14)
        self.sender_addr1 = QtWidgets.QLineEdit(self.frame_5)
        self.sender_addr1.setObjectName("sender_addr1")
        self.horizontalLayout_11.addWidget(self.sender_addr1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")



        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setMinimumSize(QtCore.QSize(60, 0))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.sender_addr2 = QtWidgets.QLineEdit(self.frame_5)
        self.sender_addr2.setObjectName("sender_addr2")
        self.horizontalLayout_8.addWidget(self.sender_addr2)

        # self.horizontalLayout_8.addWidget(self.sender_country)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        self.label_13.setMinimumSize(QtCore.QSize(60, 0))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        self.sender_addr3 = QtWidgets.QLineEdit(self.frame_5)
        self.sender_addr3.setObjectName("sender_addr3")
        self.horizontalLayout_10.addWidget(self.sender_addr3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")

        self.label_12 = QtWidgets.QLabel(self.frame_5)
        self.label_12.setMinimumSize(QtCore.QSize(60, 0))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.sender_postcode = QtWidgets.QLineEdit(self.frame_5)
        self.sender_postcode.setObjectName("sender_postcode")
        self.horizontalLayout_9.addWidget(self.sender_postcode)

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")

        self.label_country = QtWidgets.QLabel(self.frame_5)
        self.label_country.setMinimumSize(QtCore.QSize(60, 0))
        self.label_country.setObjectName("label_country")
        self.horizontalLayout_20.addWidget(self.label_country)
        self.sender_country = QtWidgets.QLineEdit(self.frame_5)
        self.sender_country.setObjectName("sender_country")
        self.horizontalLayout_20.addWidget(self.sender_country)


        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 4, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setMinimumSize(QtCore.QSize(60, 0))
        self.label_6.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.sender_choice_box = QtWidgets.QComboBox(self.frame_5)
        self.sender_choice_box.setMinimumSize(QtCore.QSize(0, 0))
        self.sender_choice_box.setMaximumSize(QtCore.QSize(150, 16777215))
        self.sender_choice_box.setObjectName("sender_choice_box")
        # self.sender_choice_box.addItem("")
        # self.sender_choice_box.addItem("")
        self.verticalLayout_4.addWidget(self.sender_choice_box)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.sender_id = QtWidgets.QLineEdit(self.frame_5)
        self.sender_id.setMaximumSize(QtCore.QSize(150, 16777215))
        self.sender_id.setObjectName("sender_id")
        self.verticalLayout.addWidget(self.sender_id)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.frame_5)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.graphicsView = QtWidgets.QGraphicsView(self.frame_5)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_6.addWidget(self.graphicsView)
        self.print_sender_button = QtWidgets.QPushButton(self.frame_5)
        self.print_sender_button.setObjectName("print_sender_button")
        self.verticalLayout_6.addWidget(self.print_sender_button)
        self.horizontalLayout_15.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.frame_5)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_8.addWidget(self.graphicsView_2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.prev_button = QtWidgets.QPushButton(self.frame_5)
        self.prev_button.setObjectName("prev_button")
        self.horizontalLayout_13.addWidget(self.prev_button)
        self.next_button = QtWidgets.QPushButton(self.frame_5)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout_13.addWidget(self.next_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.print_button = QtWidgets.QPushButton(self.frame_5)
        self.print_button.setObjectName("print_button")
        self.horizontalLayout_14.addWidget(self.print_button)
        self.print_all_button = QtWidgets.QPushButton(self.frame_5)
        self.print_all_button.setObjectName("print_all_button")
        self.horizontalLayout_14.addWidget(self.print_all_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.horizontalLayout_15.addLayout(self.verticalLayout_8)
        self.gridLayout.addLayout(self.horizontalLayout_15, 4, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.frame_5)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_5, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.customer_list = customer_list
        self.to_print = []

        self.sender_choice_box.activated[str].connect(self.preview_sender)
        self.tag_size_box.activated[str].connect(self.changeEvent)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Print"))
        self.label.setText(_translate("Dialog", "Printer:"))
        # self.printer_box.setItemText(0, _translate("Dialog", "Printer 1"))
        # self.printer_box.setItemText(1, _translate("Dialog", "Printer 2"))
        self.label_3.setText(_translate("Dialog", "Tag Size:"))
        self.tag_size_box.setItemText(0, _translate("Dialog", "100*80"))
        self.tag_size_box.setItemText(1, _translate("Dialog", "80*60"))
        self.label_7.setText(_translate("Dialog", "New Sender"))
        self.label_4.setText(_translate("Dialog", "Sender Name:"))
        self.label_8.setText(_translate("Dialog", "Company:"))
        self.label_9.setText(_translate("Dialog", "Phone:"))
        self.label_10.setText(_translate("Dialog", "City:"))
        self.new_sender_button.setText(_translate("Dialog", "New"))
        self.save_sender_button.setText(_translate("Dialog", "Save"))
        self.label_14.setText(_translate("Dialog", "Address 1:"))
        self.label_11.setText(_translate("Dialog", "Address 2:"))
        self.label_13.setText(_translate("Dialog", "Address 3:"))
        self.label_12.setText(_translate("Dialog", "Postcode:"))
        self.label_country.setText(_translate("Dialog", "Country:"))
        self.label_6.setText(_translate("Dialog", "Sender Detail:"))
        # self.sender_choice_box.setItemText(0, _translate("Dialog", "Alice"))
        # self.sender_choice_box.setItemText(1, _translate("Dialog", "Bob"))
        self.label_15.setText(_translate("Dialog", "Sender ID:"))
        self.label_5.setText(_translate("Dialog", "Sender Preview:"))
        self.print_sender_button.setText(_translate("Dialog", "Print"))
        self.label_2.setText(_translate("Dialog", "Customer Preview:"))
        self.prev_button.setText(_translate("Dialog", "Prev"))
        self.next_button.setText(_translate("Dialog", "Next"))
        self.print_button.setText(_translate("Dialog", "Print"))
        self.print_all_button.setText(_translate("Dialog", "Print All"))

        self.print_button.clicked.connect(self.print_cust)

        self.new_sender_button.clicked.connect(self.new_sender)
        self.save_sender_button.clicked.connect(self.save)
        self.prev_button.clicked.connect(self.prev)
        self.next_button.clicked.connect(self.next)
        self.print_all_button.clicked.connect(self.print_cust_all)
        self.print_sender_button.clicked.connect(self.print_sender)

    def init_data(self):
        print("init print page")
        # print(self.customer_list)

        printer_list = win32print.EnumPrinters(2)
        # print(printer_list[0][2])
        if len(printer_list) > 0:
            for i in range(len(printer_list)):
                self.printer_box.addItem(printer_list[i][2])
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Printer not found")
            msg.setText('Please connect a printer to your PC and open the printing page again.')
            x = msg.exec_()

        engine = create_engine(db_link, echo=False)
        metadata = MetaData(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        for i in range(len(self.customer_list)):
            current_cust = {}
            cust = session.query(Customer).filter_by(id=self.customer_list[i]).first()
            current_cust['city'] = cust.city
            current_cust['country'] = cust.country
            current_cust['company'] = cust.company_name
            current_cust['name'] = cust.first_name + ' ' + cust.last_name
            current_cust['postcode'] = cust.post_code
            current_cust['phone'] = cust.phone_number_prefix + '-' + cust.phone_number
            current_cust['address1'] = cust.address_one.strip(',')
            current_cust['address2'] = cust.address_two.strip(',')
            current_cust['address3'] = cust.address_three.strip(',')
            self.to_print.append(current_cust)

        senders = session.query(Sender).all()
        print(len(senders))
        if len(senders) == 0:
            self.save_sender_button.setText('Save')
        else:
            for sender in senders:
                self.sender_choice_box.addItem(sender.id)
            self.preview_sender(self.sender_choice_box.currentText())
        # print('123213')

        self.records_number = len(self.to_print)

        if self.records_number == 0:
            self.print_all_button.setDisabled(True)
            self.print_button.setDisabled(True)
            self.next_button.setDisabled(True)

        if self.records_number == 1:
            self.prev_button.setDisabled(True)
            self.next_button.setDisabled(True)
            self.print_all_button.setDisabled(True)
        else:
            self.prev_button.setDisabled(True)

        # print(self.graphicsView.width())

        if(self.records_number >= 1):
            self.show_cust(self.current_index)

        session.close()

    def new_sender(self):
        self.label_7.setText("Please Enter Sender Info")
        self.sender_id.setText('')
        self.sender_name.setText('')
        self.sender_addr1.setText('')
        self.sender_addr2.setText('')
        self.sender_addr3.setText('')
        self.sender_phone.setText('')
        self.sender_company.setText('')
        self.sender_country.setText('')
        self.sender_postcode.setText('')
        self.sender_city.setText('')
        self.sender_choice_box.setCurrentText('')
        self.save_sender_button.setText("Save")

    def popup_button(self, i):
        if i.text() == '&Yes':
            print('updating')
            try:
                engine = create_engine(db_link, echo=False)
                metadata = MetaData(engine)
                Session = sessionmaker(bind=engine)
                session = Session()
                sender = session.query(Sender).filter_by(id=self.sender_id.text()).first()
                sender.address_one = self.sender_addr1.text()
                sender.address_two = self.sender_addr2.text()
                sender.address_three = self.sender_addr3.text()
                sender.post_code = self.sender_postcode.text()
                sender.country = self.sender_country.text()
                sender.sender_name = self.sender_name.text()
                sender.company_name = self.sender_company.text()
                sender.phone_number = self.sender_phone.text()
                sender.city = self.sender_city.text()
                session.commit()

            except Exception as err:
                logger.info(err, exc_info=True)
                print(err)
            finally:
                session.close()
                self.preview_sender(self.sender_id.text())
                self.show_sender()
        else:
            pass

    def save(self):
        sender_id = self.sender_id.text()
        if sender_id == '':
            msg = QMessageBox()
            msg.setWindowTitle("Sender ID not entered")
            msg.setText("Please enter your sender ID")
            x = msg.exec_()
        else:
            engine = create_engine(db_link, echo=False)
            metadata = MetaData(engine)
            Session = sessionmaker(bind=engine)
            session = Session()

            if session.query(Sender).filter_by(id=sender_id).first():
                msg = QMessageBox()
                msg.setWindowTitle("Sender Exists")
                msg.setText("Do you want to update {} info?".format(sender_id))
                msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
                msg.setDefaultButton(QMessageBox.No)
                msg.buttonClicked.connect(self.popup_button)
                x = msg.exec_()
            else:
                addr1 = self.sender_addr1.text()
                addr2 = self.sender_addr2.text()
                addr3 = self.sender_addr3.text()
                postcode = self.sender_postcode.text()
                country = self.sender_country.text()
                name = self.sender_name.text()
                company = self.sender_company.text()
                phone = self.sender_phone.text()
                city = self.sender_city.text()

                sender = Sender(id=sender_id,sender_name=name,company_name=company,address_one=addr1,address_two=addr2,address_three=addr3,
                                phone_number=phone,country=country,city=city,post_code=postcode)

                try:
                    session.add(sender)
                except Exception as err:
                    logger.info(err, exc_info=True)
                    print(err)
                    session.rollback()
                finally:
                    session.commit()
                    self.sender_choice_box.addItem(sender_id)
                    if self.current_sender == {}:
                        self.preview_sender(sender_id)
                        self.show_sender()
                    self.label_7.setText("New Sender Created")

    def preview_sender(self, sender_id):
        print(sender_id)
        self.label_7.setText("Sender detail")
        self.save_sender_button.setText("Update")
        engine = create_engine(db_link, echo=False)
        metadata = MetaData(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        preview = {}

        sender = session.query(Sender).filter_by(id=sender_id).first()
        try:
            preview['id'] = sender_id
            preview['sender_name'] = sender.sender_name
            preview['sender_addr1'] = sender.address_one.strip(',')
            preview['sender_addr2'] = sender.address_two.strip(',')
            preview['sender_addr3'] = sender.address_three.strip(',')
            preview['sender_phone'] = sender.phone_number
            preview['sender_country'] = sender.country
            preview['sender_postcode'] = sender.post_code
            preview['sender_company'] = sender.company_name
            preview['sender_city'] = sender.city
            self.current_sender = preview
            self.sender_id.setText(sender_id)
            self.sender_name.setText(sender.sender_name)
            self.sender_addr1.setText(sender.address_one)
            self.sender_addr2.setText(sender.address_two)
            self.sender_addr3.setText(sender.address_three)
            self.sender_phone.setText(sender.phone_number)
            self.sender_company.setText(sender.company_name)
            self.sender_country.setText(sender.country)
            self.sender_postcode.setText(sender.post_code)
            self.sender_city.setText(sender.city)
            self.show_sender()
        except Exception as err:
            print(err)
            logger.info(err, exc_info=True)

    def show_sender(self,):
        # print(width)
        # print(self.width)
        width = self.graphicsView.width()
        height = self.graphicsView.height()
        scene = QtWidgets.QGraphicsScene()
        if self.tag_size_box.currentText() == '100*80':
            # print(scene.height())
            try:
                rect_item = QtWidgets.QGraphicsRectItem(QtCore.QRectF(0.1*width, 0, width*0.8, 0.64*width))
                distance = width*0.64/8
                # scene.addText("Hello, world!")
                font1 = QtGui.QFont()
                font2 = QtGui.QFont()
                font1.setPixelSize(width*0.03685)
                font2.setPixelSize(10)

                name = self.current_sender['sender_name']
                line1 = QtWidgets.QGraphicsTextItem('Name:    ' + name)# + (31-len(name))*' ' )
                scene.addItem(line1)
                line1.setPos(0.11*width,0)
                line1.setFont(font1)

                company = self.current_sender['sender_company']
                line2 = QtWidgets.QGraphicsTextItem('Company: ' + company)# + (31-len(company))*' ' )
                scene.addItem(line2)
                line2.setPos(0.11 * width, distance)
                line2.setFont(font1)

                address1 = self.current_sender['sender_addr1']
                line3 = QtWidgets.QGraphicsTextItem('Address: ' + address1)# + (31- len(address1))*' ')
                scene.addItem(line3)
                line3.setPos(0.11 * width, distance*2)
                line3.setFont(font1)

                address2 = self.current_sender['sender_addr2']
                line4 = QtWidgets.QGraphicsTextItem('         ' + address2)# + (31- len(address2))*' ' )
                scene.addItem(line4)
                line4.setPos(0.11 * width, distance*3)
                line4.setFont(font1)

                address3 = self.current_sender['sender_addr3']
                line5 = QtWidgets.QGraphicsTextItem('         ' + address3)# + (31- len(address3))*' ' )
                scene.addItem(line5)
                line5.setPos(0.11 * width, distance*4)
                line5.setFont(font1)

                phone = self.current_sender['sender_phone']
                line6 = QtWidgets.QGraphicsTextItem('Phone:   ' + phone)# + (31-len(phone))*' ')
                scene.addItem(line6)
                line6.setPos(0.11 * width, distance*5)
                line6.setFont(font1)

                city = self.current_sender['sender_city']
                line7 = QtWidgets.QGraphicsTextItem('City:    ' + city)# + (31-len(city))*' ' )
                scene.addItem(line7)
                line7.setPos(0.11 * width, distance*6)
                line7.setFont(font1)

                country = self.current_sender['sender_country']
                postcode = self.current_sender['sender_postcode']
                line8 = QtWidgets.QGraphicsTextItem('Country: ' + country + (20-len(postcode)-len(country))*' ' + ' Postcode: ' + postcode)
                scene.addItem(line8)
                line8.setPos(0.11 * width, distance * 7)
                line8.setFont(font1)


                # print(scene.width())
                # print(scene.height())
                scene.addItem(rect_item)
                # scene.addText("Hello, world!").setPos(0, 80)
                self.graphicsView.setScene(scene)
            except Exception as err:
                logger.info(err, exc_info=True)
                print(err)

        elif self.tag_size_box.currentText() == '80*60':
            rect_item = QtWidgets.QGraphicsRectItem(QtCore.QRectF(0.18 * width, 0, width * 0.64, 0.75*0.64*width))
            scene.addItem(rect_item)
            distance = width * 0.64 * 0.75 / 8
            # scene.addText("Hello, world!")
            font1 = QtGui.QFont()
            font2 = QtGui.QFont()
            font1.setPixelSize(width * 0.03685 * 0.8)
            font2.setPixelSize(10)

            name = self.current_sender['sender_name']
            line1 = QtWidgets.QGraphicsTextItem('Name:    ' + name)# + (31-len(name))*' ' )
            scene.addItem(line1)
            line1.setPos(0.19 * width, 0)
            line1.setFont(font1)

            company = self.current_sender['sender_company']
            line2 = QtWidgets.QGraphicsTextItem('Company: ' + company)# + (31-len(company))*' ' )
            scene.addItem(line2)
            line2.setPos(0.19 * width, distance)
            line2.setFont(font1)

            address1 = self.current_sender['sender_addr1']
            line3 = QtWidgets.QGraphicsTextItem('Address: '+ address1)# + (31- len(address1))*' ' )
            scene.addItem(line3)
            line3.setPos(0.19 * width, distance * 2)
            line3.setFont(font1)

            address2 = self.current_sender['sender_addr2']
            line4 = QtWidgets.QGraphicsTextItem('         ' + address2)# + (31- len(address2))*' ')
            scene.addItem(line4)
            line4.setPos(0.19 * width, distance * 3)
            line4.setFont(font1)

            address3 = self.current_sender['sender_addr3']
            line5 = QtWidgets.QGraphicsTextItem('         ' + address3)# + (31- len(address3))*' ')
            scene.addItem(line5)
            line5.setPos(0.19 * width, distance * 4)
            line5.setFont(font1)

            phone = self.current_sender['sender_phone']
            line6 = QtWidgets.QGraphicsTextItem('Phone:   ' + phone)# + (31-len(phone))*' ')
            scene.addItem(line6)
            line6.setPos(0.19 * width, distance * 5)
            line6.setFont(font1)

            city = self.current_sender['sender_city']
            line7 = QtWidgets.QGraphicsTextItem('City:    ' + city)# + (31-len(city))*' ')
            scene.addItem(line7)
            line7.setPos(0.19 * width, distance * 6)
            line7.setFont(font1)

            country = self.current_sender['sender_country']
            postcode = self.current_sender['sender_postcode']
            line8 = QtWidgets.QGraphicsTextItem(
                'Country: ' + country + (15 - len(postcode) - len(country)) * ' ' + ' Postcode: ' + postcode)
            scene.addItem(line8)
            line8.setPos(0.19 * width, distance * 7)
            line8.setFont(font1)

            self.graphicsView.setScene(scene)

    def show_cust(self, index):
        width = self.graphicsView_2.width()
        height = self.graphicsView_2.height()
        scene = QtWidgets.QGraphicsScene()
        if self.tag_size_box.currentText() == '100*80':
            # print(scene.height())
            try:
                rect_item = QtWidgets.QGraphicsRectItem(QtCore.QRectF(0.1 * width, 0, width * 0.8, 0.64 * width))
                distance = width * 0.64 / 8
                # scene.addText("Hello, world!")
                font1 = QtGui.QFont()

                font1.setPixelSize(width * 0.03685)


                name = self.to_print[index]['name']
                line1 = QtWidgets.QGraphicsTextItem('Name:    ' + name)# + (31-len(name))*' ')
                scene.addItem(line1)
                line1.setPos(0.11 * width, 0)
                line1.setFont(font1)

                company = self.to_print[index]['company']
                line2 = QtWidgets.QGraphicsTextItem('Company: ' + company)# + (31-len(company))*' ')
                scene.addItem(line2)
                line2.setPos(0.11 * width, distance)
                line2.setFont(font1)

                address1 = self.to_print[index]['address1']
                line3 = QtWidgets.QGraphicsTextItem('Address: '+ address1)# + (31- len(address1))*' ' )
                scene.addItem(line3)
                line3.setPos(0.11 * width, distance * 2)
                line3.setFont(font1)

                address2 = self.to_print[index]['address2']
                line4 = QtWidgets.QGraphicsTextItem('         ' + address2)# + (31- len(address2))*' ')
                scene.addItem(line4)
                line4.setPos(0.11 * width, distance * 3)
                line4.setFont(font1)

                address3 = self.to_print[index]['address3']
                line5 = QtWidgets.QGraphicsTextItem('         ' + address3)# + (31- len(address3))*' ')
                scene.addItem(line5)
                line5.setPos(0.11 * width, distance * 4)
                line5.setFont(font1)

                phone = self.to_print[index]['phone']
                line6 = QtWidgets.QGraphicsTextItem('Phone:   ' + phone)# + (31-len(phone))*' ')
                scene.addItem(line6)
                line6.setPos(0.11 * width, distance * 5)
                line6.setFont(font1)

                city = self.to_print[index]['city']
                line7 = QtWidgets.QGraphicsTextItem('City:    ' + city)# + (31-len(city))*' ')
                scene.addItem(line7)
                line7.setPos(0.11 * width, distance * 6)
                line7.setFont(font1)

                country = self.to_print[index]['country']
                postcode = self.to_print[index]['postcode']
                line8 = QtWidgets.QGraphicsTextItem(
                    'Country: ' + country + (15 - len(postcode) - len(country)) * ' ' + ' Postcode: ' + postcode)
                scene.addItem(line8)
                line8.setPos(0.11 * width, distance * 7)
                line8.setFont(font1)

                # print(scene.width())
                # print(scene.height())
                scene.addItem(rect_item)
                # scene.addText("Hello, world!").setPos(0, 80)
                self.graphicsView_2.setScene(scene)
            except Exception as err:
                logger.info(err, exc_info=True)
                print(err)

        elif self.tag_size_box.currentText() == '80*60':
            try:
                rect_item = QtWidgets.QGraphicsRectItem(QtCore.QRectF(0.18 * width, 0, width * 0.64, 0.75 * 0.64 * width))
                scene.addItem(rect_item)
                distance = width * 0.64 * 0.75 / 8
                # scene.addText("Hello, world!")
                font1 = QtGui.QFont()
                font2 = QtGui.QFont()
                font1.setPixelSize(width * 0.03685 * 0.8)
                font2.setPixelSize(10)

                name = self.to_print[index]['name']
                line1 = QtWidgets.QGraphicsTextItem('Name:    ' + name)# + (31-len(name))*' ')
                scene.addItem(line1)
                line1.setPos(0.19 * width, 0)
                line1.setFont(font1)

                company = self.to_print[index]['company']
                line2 = QtWidgets.QGraphicsTextItem('Company: ' + company)# + (31-len(company))*' ')
                scene.addItem(line2)
                line2.setPos(0.19 * width, distance)
                line2.setFont(font1)

                address1 = self.to_print[index]['address1']
                line3 = QtWidgets.QGraphicsTextItem('Address: '+ address1 )#+ (31- len(address1))*' ' )
                scene.addItem(line3)
                line3.setPos(0.19 * width, distance * 2)
                line3.setFont(font1)

                address2 = self.to_print[index]['address2']
                line4 = QtWidgets.QGraphicsTextItem('         ' + address2)# + (31- len(address2))*' ')
                scene.addItem(line4)
                line4.setPos(0.19 * width, distance * 3)
                line4.setFont(font1)

                address3 = self.to_print[index]['address3']
                line5 = QtWidgets.QGraphicsTextItem('         ' + address3)# + (31- len(address3))*' ')
                scene.addItem(line5)
                line5.setPos(0.19 * width, distance * 4)
                line5.setFont(font1)

                phone = self.to_print[index]['phone']
                line6 = QtWidgets.QGraphicsTextItem('Phone:   ' + phone)# + (31-len(phone))*' ')
                scene.addItem(line6)
                line6.setPos(0.19 * width, distance * 5)
                line6.setFont(font1)

                city = self.to_print[index]['city']
                line7 = QtWidgets.QGraphicsTextItem('City:    ' + city)# + (31-len(city))*' ')
                scene.addItem(line7)
                line7.setPos(0.19 * width, distance * 6)
                line7.setFont(font1)

                country = self.to_print[index]['country']
                postcode = self.to_print[index]['postcode']
                line8 = QtWidgets.QGraphicsTextItem(
                    'Country: ' + country + (15 - len(postcode) - len(country)) * ' ' + ' Postcode: ' + postcode)
                scene.addItem(line8)
                line8.setPos(0.19 * width, distance * 7)
                line8.setFont(font1)

                self.graphicsView_2.setScene(scene)
            except Exception as err:
                logger.info(err, exc_info=True)
                print(err)

    def prev(self):
        self.current_index -= 1
        if self.current_index == 0:
            self.prev_button.setDisabled(True)
        self.next_button.setDisabled(False)
        self.show_cust(self.current_index)
        # self.show_text()

    def next(self):
        self.current_index += 1
        if self.current_index == self.records_number - 1:
            self.next_button.setDisabled(True)
        self.prev_button.setDisabled(False)
        self.show_cust(self.current_index)

        # self.show_text()

    def print_cust(self):
        # remove printed customer
        print('print_cust')
        self.prev_button.setDisabled(True)
        self.next_button.setDisabled(True)
        try:
            if self.tag_size_box.currentText() == '100*80':
                font_width = self.font_100
                X = self.x_100
                Y = self.y_100
                Y_distance = self.y_100_distance
            elif self.tag_size_box.currentText() == '80*60':
                font_width = self.font_80
                X = self.x_80
                Y = self.y_80
                Y_distance = self.y_80_distance

            name = self.to_print[self.current_index]['name']
            line1 = ('Name:        ' + name)
            company = self.to_print[self.current_index]['company']
            line2 = ('Company:  ' + company)

            address1 = self.to_print[self.current_index]['address1']
            line3 = ('Address:    ' + address1)
            address2 = self.to_print[self.current_index]['address2']
            line4 = ('                  ' + address2)
            address3 = self.to_print[self.current_index]['address3']
            line5 = ('                  ' + address3)

            phone = self.to_print[self.current_index]['phone']
            line6 = ('Phone:       ' + phone)

            city = self.to_print[self.current_index]['city']
            line7 = ('City:           ' + city)

            country = self.to_print[self.current_index]['country']
            postcode = self.to_print[self.current_index]['postcode']
            line8 = (
                    'Country:    ' + country + (20 - len(postcode) - len(country)) * ' ' + ' Postcode: ' + postcode)
            multi_line_string = [line1, line2, line3, line4, line5, line6, line7, line8]
            fontdata = {'name': 'Arial', 'weight': win32con.FW_NORMAL, 'height': 60, 'width': font_width}

        except Exception as err:
            print(err)
            logger.info(err, exc_info=True)

        try:
            print(self.next_button.isEnabled())
            hDC = win32ui.CreateDC()
            hDC.CreatePrinterDC(self.printer_box.currentText())
            font = win32ui.CreateFont(fontdata);
            hDC.SelectObject(font)
            hDC.StartDoc('alex')
            hDC.StartPage()
            for line in multi_line_string:
                hDC.TextOut(X, Y, line)
                # 行距, 唯一影响行数
                Y += Y_distance

            hDC.EndPage()
            hDC.EndDoc()

            # base on current index
            # print(self.current_index)
            # print(self.to_print)
            print(self.next_button.isEnabled())
            if self.current_index != 0:
                self.prev_button.setDisabled(False)
            if self.current_index != len(self.to_print)-1:
                self.next_button.setDisabled(False)

            # if self.current_index == 0 and len(self.to_print) == 1:
            #     self.prev_button.setDisabled(True)
            #     self.next_button.setDisabled(True)
            # elif len(self.to_print) > 1 and self.current_index == len(self.to_print) - 1 :
            #     self.current_index -= 1
            #     self.to_print.pop(-1)
            #     self.show_cust(self.current_index)
            #     self.prev_button.setDisabled(False)
            #     if self.current_index == 0:
            #         self.prev_button.setDisabled(True)
            # else:
            #     self.to_print.pop(self.current_index)
            #     # self.current_index += 1
            #     self.show_cust(self.current_index)
            #     if self.current_index != len(self.to_print) - 1:
            #

            # print(self.current_index)
            # print(self.to_print)
        except Exception as err:
            print(err)
            logger.info(err, exc_info=True)


    def print_cust_all(self):
        self.prev_button.setDisabled(True)
        self.next_button.setDisabled(True)
        self.current_index = 0
        self.show_cust(self.current_index)
        for i in range(len(self.to_print)):
            self.show_cust(self.current_index)
            self.print_cust()
            if self.current_index != len(self.to_print)-1:
                self.current_index += 1
        self.prev_button.setDisabled(False)
        self.next_button.setDisabled(True)


    def print_sender(self):
        try:
            print('ready to print')
            if self.tag_size_box.currentText() == '100*80':
                font_width = self.font_100
                X = self.x_100
                Y = self.y_100
                Y_distance = self.y_100_distance
            elif self.tag_size_box.currentText() == '80*60':
                font_width = self.font_100
                X = self.x_80
                Y = self.y_80
                Y_distance = self.y_80_distance

            name = self.current_sender['sender_name']
            line1 = ('Name:        ' + name)
            company = self.current_sender['sender_company']
            line2 = ('Company:  ' + company)

            address1 = self.current_sender['sender_addr1']
            line3 = ('Address:    ' + address1)
            address2 = self.current_sender['sender_addr2']
            line4 = ('                  ' + address2)
            address3 = self.current_sender['sender_addr3']
            line5 = ('                  ' + address3)

            phone = self.current_sender['sender_phone']
            line6 = ('Phone:       ' + phone)

            city = self.current_sender['sender_city']
            line7 = ('City:           ' + city)

            country = self.current_sender['sender_country']
            postcode = self.current_sender['sender_postcode']
            line8 = (
                'Country:    ' + country + (20 - len(postcode) - len(country)) * ' ' + ' Postcode: ' + postcode)
            multi_line_string = [line1,line2,line3,line4,line5,line6,line7,line8]

            fontdata = {'name': 'Arial', 'weight': win32con.FW_NORMAL, 'height': 60, 'width': font_width}
        except Exception as err:
            logger.info(err, exc_info=True)
            print(err)
        print('before print')
        try:
            hDC = win32ui.CreateDC()
            hDC.CreatePrinterDC(self.printer_box.currentText())
            font = win32ui.CreateFont(fontdata);
            hDC.SelectObject(font)
            hDC.StartDoc('alex')
            hDC.StartPage()
            for line in multi_line_string:
                hDC.TextOut(X, Y, line)
                # 行距, 唯一影响行数
                Y += Y_distance

            hDC.EndPage()
            hDC.EndDoc()
        except Exception as err:
            logger.info(err, exc_info=True)
            print(err)


    def changeEvent(self,e):
        try:
            print('change event')
            if self.sender_choice_box.currentText()!= '':
                self.show_sender()
            if(len(self.to_print) >= 1):
                self.show_cust(self.current_index)
        except Exception as err:
            logger.info(err, exc_info=True)
            print(err)

        # print('changed')

