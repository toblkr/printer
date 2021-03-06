# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddCustomer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from DB import Customer, db_link
from sqlalchemy import create_engine, MetaData, Table, func
from sqlalchemy.orm import sessionmaker

import Print
from main import logger


class Ui_Dialog(QtWidgets.QDialog):
    the_signal = QtCore.pyqtSignal()
    the_signal2 = QtCore.pyqtSignal(str)
    original_id = ''

    def setupUi(self, Dialog, customer_id=None):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 500)
        Dialog.setMaximumSize(QtCore.QSize(700, 550))
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setMinimumSize(QtCore.QSize(80, 0))
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_7.addWidget(self.label_17)
        self.customer_id = QtWidgets.QLineEdit(self.frame_2)
        self.customer_id.setObjectName("customer_id")
        self.horizontalLayout_7.addWidget(self.customer_id)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_batch = QtWidgets.QHBoxLayout()
        self.horizontalLayout_batch.setObjectName("horizontalLayout_batch")

        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")

        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setMinimumSize(QtCore.QSize(84, 0))
        self.label_13.setMaximumSize(QtCore.QSize(84, 16777215))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_14.addWidget(self.label_13)

        self.label_batch = QtWidgets.QLabel(self.frame_2)
        self.label_batch.setMinimumSize(QtCore.QSize(84, 0))
        self.label_batch.setMaximumSize(QtCore.QSize(84, 16777215))
        self.label_batch.setObjectName("label_batch")
        self.horizontalLayout_batch.addWidget(self.label_batch)

        self.batch = QtWidgets.QLineEdit(self.frame_2)
        self.batch.setMaximumSize(QtCore.QSize(400, 16777215))
        self.batch.setObjectName("batch")
        self.horizontalLayout_batch.addWidget(self.batch)

        self.market_group = QtWidgets.QLineEdit(self.frame_2)
        self.market_group.setMaximumSize(QtCore.QSize(400, 16777215))
        self.market_group.setObjectName("market_group")
        self.horizontalLayout_14.addWidget(self.market_group)

        self.verticalLayout_5.addLayout(self.horizontalLayout_batch)

        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setMinimumSize(QtCore.QSize(84, 0))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.company_name = QtWidgets.QLineEdit(self.frame_2)
        self.company_name.setObjectName("company_name")
        self.horizontalLayout_6.addWidget(self.company_name)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMinimumSize(QtCore.QSize(84, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.addr1 = QtWidgets.QLineEdit(self.frame_2)
        self.addr1.setMaximumSize(QtCore.QSize(400, 16777215))
        self.addr1.setObjectName("addr1")
        self.horizontalLayout.addWidget(self.addr1)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setMinimumSize(QtCore.QSize(84, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.addr2 = QtWidgets.QLineEdit(self.frame_2)
        self.addr2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.addr2.setObjectName("addr2")
        self.horizontalLayout_2.addWidget(self.addr2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setMinimumSize(QtCore.QSize(84, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.addr3 = QtWidgets.QLineEdit(self.frame_2)
        self.addr3.setMaximumSize(QtCore.QSize(400, 16777215))
        self.addr3.setObjectName("addr3")
        self.horizontalLayout_3.addWidget(self.addr3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setMinimumSize(QtCore.QSize(84, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.city = QtWidgets.QLineEdit(self.frame_2)
        self.city.setObjectName("city")
        self.horizontalLayout_5.addWidget(self.city)
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.postcode = QtWidgets.QLineEdit(self.frame_2)
        self.postcode.setMaximumSize(QtCore.QSize(100, 16777215))
        self.postcode.setObjectName("postcode")
        self.horizontalLayout_5.addWidget(self.postcode)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.line_4 = QtWidgets.QFrame(self.frame_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_4.addWidget(self.line_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_19 = QtWidgets.QLabel(self.frame_2)
        self.label_19.setMinimumSize(QtCore.QSize(80, 0))
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_19.addWidget(self.label_19)
        self.title_box = QtWidgets.QComboBox(self.frame_2)
        self.title_box.setObjectName("title_box")
        self.title_box.addItem("")
        self.title_box.addItem("")
        self.title_box.addItem("")
        self.title_box.addItem("")
        self.horizontalLayout_19.addWidget(self.title_box)
        self.other_title = QtWidgets.QLineEdit(self.frame_2)
        self.other_title.setObjectName("other_title")
        self.horizontalLayout_19.addWidget(self.other_title)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setMinimumSize(QtCore.QSize(80, 0))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        self.full_name = QtWidgets.QLineEdit(self.frame_2)
        self.full_name.setMaximumSize(QtCore.QSize(400, 16777215))
        self.full_name.setObjectName("full_name")
        self.horizontalLayout_12.addWidget(self.full_name)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setMinimumSize(QtCore.QSize(80, 0))
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_15.addWidget(self.label_15)

        self.first_name = QtWidgets.QLineEdit(self.frame_2)
        self.first_name.setMaximumSize(QtCore.QSize(400, 16777215))
        self.first_name.setObjectName("first_name")
        self.horizontalLayout_15.addWidget(self.first_name)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setMinimumSize(QtCore.QSize(80, 0))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)

        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")

        self.label_country = QtWidgets.QLabel(self.frame_2)
        self.label_country.setMinimumSize(QtCore.QSize(80, 0))
        self.label_country.setObjectName("label_country")
        self.horizontalLayout_20.addWidget(self.label_country)

        self.last_name = QtWidgets.QLineEdit(self.frame_2)
        self.last_name.setMaximumSize(QtCore.QSize(400, 16777215))
        self.last_name.setObjectName("last_name")

        self.horizontalLayout_8.addWidget(self.last_name)


        self.country = QtWidgets.QLineEdit(self.frame_2)
        self.country.setMaximumSize(QtCore.QSize(400, 16777215))
        self.country.setObjectName("country")
        self.horizontalLayout_20.addWidget(self.country)

        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setMinimumSize(QtCore.QSize(80, 0))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.phone1 = QtWidgets.QLineEdit(self.frame_2)
        self.phone1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phone1.sizePolicy().hasHeightForWidth())
        self.phone1.setSizePolicy(sizePolicy)
        self.phone1.setMaximumSize(QtCore.QSize(40, 16777215))
        self.phone1.setObjectName("phone1")
        self.horizontalLayout_9.addWidget(self.phone1)
        self.phone2 = QtWidgets.QLineEdit(self.frame_2)
        self.phone2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.phone2.setText("")
        self.phone2.setObjectName("phone2")
        self.horizontalLayout_9.addWidget(self.phone2)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setMinimumSize(QtCore.QSize(80, 0))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.fax1 = QtWidgets.QLineEdit(self.frame_2)
        self.fax1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fax1.sizePolicy().hasHeightForWidth())
        self.fax1.setSizePolicy(sizePolicy)
        self.fax1.setMaximumSize(QtCore.QSize(40, 16777215))
        self.fax1.setObjectName("fax1")
        self.horizontalLayout_10.addWidget(self.fax1)
        self.fax2 = QtWidgets.QLineEdit(self.frame_2)
        self.fax2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fax2.setText("")
        self.fax2.setObjectName("fax2")
        self.horizontalLayout_10.addWidget(self.fax2)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout_7.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setMaximumSize(QtCore.QSize(670, 350))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setMinimumSize(QtCore.QSize(0, 15))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.notes = QtWidgets.QTextEdit(self.frame_3)
        self.notes.setMaximumSize(QtCore.QSize(433, 100))
        self.notes.setObjectName("notes")
        self.verticalLayout_2.addWidget(self.notes)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setMinimumSize(QtCore.QSize(120, 0))
        self.label_16.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_16.addWidget(self.label_16)
        self.email1 = QtWidgets.QLineEdit(self.frame_3)
        self.email1.setMaximumSize(QtCore.QSize(300, 16777215))
        self.email1.setObjectName("email1")
        self.horizontalLayout_16.addWidget(self.email1)
        self.gridLayout_5.addLayout(self.horizontalLayout_16, 1, 0, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_21 = QtWidgets.QLabel(self.frame_3)
        self.label_21.setMinimumSize(QtCore.QSize(120, 0))
        self.label_21.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_17.addWidget(self.label_21)
        self.email2 = QtWidgets.QLineEdit(self.frame_3)
        self.email2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.email2.setObjectName("email2")
        self.horizontalLayout_17.addWidget(self.email2)
        self.gridLayout_5.addLayout(self.horizontalLayout_17, 2, 0, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_22 = QtWidgets.QLabel(self.frame_3)
        self.label_22.setMinimumSize(QtCore.QSize(120, 0))
        self.label_22.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_18.addWidget(self.label_22)
        self.email3 = QtWidgets.QLineEdit(self.frame_3)
        self.email3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.email3.setObjectName("email3")
        self.horizontalLayout_18.addWidget(self.email3)
        self.gridLayout_5.addLayout(self.horizontalLayout_18, 3, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.line_3 = QtWidgets.QFrame(self.frame_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_13.addWidget(self.line_3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.print_button = QtWidgets.QPushButton(self.frame_3)
        self.print_button.setObjectName("print_button")
        # self.verticalLayout_4.addWidget(self.print_button)
        # self.add_another_button = QtWidgets.QPushButton(self.frame_3)
        # self.add_another_button.setObjectName("add_another_button")
        # self.verticalLayout_3.addWidget(self.add_another_button)
        self.horizontalLayout_11.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.save_button = QtWidgets.QPushButton(self.frame_3)
        self.save_button.setObjectName("save_button")
        self.verticalLayout_4.addWidget(self.save_button)
        self.verticalLayout_4.addWidget(self.print_button)
        self.delete_button = QtWidgets.QPushButton(self.frame_3)
        self.delete_button.setObjectName("delete_button")
        self.verticalLayout_4.addWidget(self.delete_button)
        self.horizontalLayout_11.addLayout(self.verticalLayout_4)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_11)
        self.gridLayout_6.addLayout(self.horizontalLayout_13, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 4, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setMinimumSize(QtCore.QSize(80, 0))
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 0, 1, 1, 1)
        self.lookup = QtWidgets.QLineEdit(Dialog)
        self.lookup.setObjectName("lookup")
        self.gridLayout_4.addWidget(self.lookup, 0, 2, 1, 1)
        self.find_button = QtWidgets.QPushButton(Dialog)
        self.find_button.setObjectName("find_button")
        self.gridLayout_4.addWidget(self.find_button, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 4, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setMaximumSize(QtCore.QSize(700, 500))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.selected_title = ""



        # print(self.title_box.currentText())
        # print(customer_id)
        self.original_id = customer_id

        if customer_id:
            print(self.original_id)
            print('yes id')
            try:
                self.edit = True
                self.customer_id.setText(self.original_id)
                print(self.customer_id.text())
                self.load_data(customer_id)

            # self.save_button.setText('Update / Save')
            except Exception as err:
                logger.info(err, exc_info=True)
                print(err)
        else:
            self.edit = False



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Customer"))

        self.label_17.setText(_translate("Dialog", "* Customer ID:"))
        self.label_batch.setText(_translate("Dialog", "Batch:"))
        self.label_13.setText(_translate("Dialog", "Market Group:"))
        self.label_6.setText(_translate("Dialog", "Company Name:"))
        self.label.setText(_translate("Dialog", "Address 1:"))
        self.label_2.setText(_translate("Dialog", "Address 2:"))
        self.label_3.setText(_translate("Dialog", "Address 3:"))
        self.label_5.setText(_translate("Dialog", "City:"))
        self.label_12.setText(_translate("Dialog", "Postcode"))
        self.label_19.setText(_translate("Dialog", "Title: "))
        self.title_box.setItemText(0, _translate("Dialog", "Mrs"))
        self.title_box.setItemText(1, _translate("Dialog", "Ms"))
        self.title_box.setItemText(2, _translate("Dialog", "Mr"))
        self.title_box.setItemText(3, _translate("Dialog", "Other"))
        self.label_10.setText(_translate("Dialog", "Full Name:"))
        self.label_15.setText(_translate("Dialog", "First Name:"))
        self.label_country.setText(_translate("Dialog", "Country:"))
        self.label_7.setText(_translate("Dialog", "Last Name:"))
        self.label_8.setText(_translate("Dialog", "Phone Number:"))
        self.label_9.setText(_translate("Dialog", "Fax Number:"))
        self.label_14.setText(_translate("Dialog", "Residential Delivery Instruction/Notes:"))
        self.notes.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_16.setText(_translate("Dialog", "Email Address 1:"))
        self.label_21.setText(_translate("Dialog", "Email Address 2:"))
        self.label_22.setText(_translate("Dialog", "Email Address 3:"))
        self.print_button.setText(_translate("Dialog", "Print"))
        # self.add_another_button.setText(_translate("Dialog", "Add Another"))
        self.save_button.setText(_translate("Dialog", "Save Customer"))
        self.delete_button.setText(_translate("Dialog", "Delete Customer"))
        self.label_18.setText(_translate("Dialog", "Lookup: "))
        self.find_button.setText(_translate("Dialog", "Find"))

        self.find_button.clicked.connect(self.find)

        self.title_box.activated[str].connect(self.title_selected)
        # self.add_another_button.clicked.connect(self.add_another)
        self.save_button.clicked.connect(self.save)
        # print(self.title_box.currentText())
        self.print_button.clicked.connect(self.print)
        # self.customer_id.textChanged.connect(self.customer_changed)
        # self.first_name.textChanged.connect(self.get_full_name)
        # self.last_name.textChanged.connect(self.get_full_name)
        #
        # #input limitation
        # self.addr3.textChanged.connect(self.limitation)
        # self.addr2.textChanged.connect(self.limitation)
        # self.addr1.textChanged.connect(self.limitation)
        # self.last_name.textChanged.connect(self.limitation)
        # self.first_name.textChanged.connect(self.limitation)
        # self.company_name.textChanged.connect(self.limitation)
        # self.country.textChanged.connect(self.limitation)
        # self.city.textChanged.connect(self.limitation)
        # # self.customer_id.textChanged.connect(self.limitation)
        # self.email3.textChanged.connect(self.limitation)
        # self.email2.textChanged.connect(self.limitation)
        # self.email1.textChanged.connect(self.limitation)
        #
        # self.other_title.textChanged.connect(self.limitation)
        # self.market_group.textChanged.connect(self.limitation)
        # self.phone2.textChanged.connect(self.limitation)
        # self.phone1.textChanged.connect(self.limitation)
        # self.fax2.textChanged.connect(self.limitation)
        # self.fax1.textChanged.connect(self.limitation)
        # self.phone2.textChanged.connect(self.limitation)
        # self.phone1.textChanged.connect(self.limitation)
        # self.customer_id.textChanged.connect(self.limitation)
        # self.batch.textChanged.connect(self.limitation)
        # self.notes.textChanged.connect(self.limitation)
        # self.full_name.textChanged.connect(self.limitation)

    @QtCore.pyqtSlot()
    def find(self):
        print(self.lookup.text())
        self.the_signal2.emit(self.lookup.text())

    def get_full_name(self):
        self.full_name.setText((self.first_name.text().strip() + ' ' + self.last_name.text().strip()).strip())

    def limitation(self):
        try:
            if len(self.addr3.text()) > 30:
                self.input_alert(1,'Address 3')
                self.addr3.setText(self.addr3.text()[:-1])
            if len(self.addr2.text()) > 30:
                self.input_alert(1, 'Address 2')
                self.addr2.setText(self.addr2.text()[:-1])
            if len(self.addr1.text()) > 30:
                self.input_alert(1, 'Address 1')
                self.addr1.setText(self.addr1.text()[:-1])

            if len(self.first_name.text()) > 17:
                self.input_alert(1, 'First Name')
                self.first_name.setText(self.first_name.text()[:-1])
            if len(self.last_name.text()) > 17:
                self.input_alert(1, 'Last Name')
                self.last_name.setText(self.last_name.text()[:-1])
            if len(self.company_name.text()) > 30:
                self.input_alert(1, 'Company Name')
                self.company_name.setText(self.company_name.text()[:-1])

            if len(self.fax1.text()) > 10:
                self.input_alert(1, 'Fax Prefix')
                self.fax1.setText(self.fax1.text()[:-1])
            if len(self.fax2.text()) > 20:
                self.input_alert(1, 'Fax Number')
                self.fax2.setText(self.fax2.text()[:-1])
            if len(self.phone2.text()) > 20:
                self.input_alert(1, 'Phone Number')
                self.phone2.setText(self.phone2.text()[:-1])

            if len(self.phone1.text()) > 10:
                self.input_alert(1, 'Phone Prefix')
                self.phone1.setText(self.phone1.text()[:-1])
            if len(self.other_title.text()) > 20:
                self.input_alert(1, 'Title')
                self.other_title.setText(self.other_title.text()[:-1])

            if len(self.city.text()) > 20:
                self.input_alert(1, 'City')
                self.city.setText(self.city.text()[:-1])
            if len(self.country.text()) > 20:
                self.input_alert(1, 'Country')
                self.country.setText(self.country.text()[:-1])
            if len(self.postcode.text()) > 10:
                self.input_alert(1, 'Postcode')
                self.postcode.setText(self.postcode.text()[:-1])
            if len(self.notes.toPlainText()) > 500:
                self.input_alert(1, 'Notes')
                self.notes.setText(self.notes.toPlainText()[:-1])

            if len(self.email1.text()) > 50:
                self.input_alert(1,'Email 1')
                self.email1.setText(self.email1.text()[:-1])
            if len(self.email2.text()) > 50:
                self.input_alert(1, 'Email 2')
                self.email2.setText(self.email2.text()[:-1])
            if len(self.email3.text()) > 50:
                self.input_alert(1, 'Email 3')
                self.email3.setText(self.email3.text()[:-1])


            if len(self.full_name.text()) > 34:
                self.input_alert(1, 'Full Name')
                self.full_name.setText(self.full_name.text()[:-1])
            if len(self.batch.text()) > 50:
                self.input_alert(1, 'Batch')
                self.batch.setText(self.batch.text()[:-1])
            if len(self.customer_id.text()) > 50:
                self.input_alert(1, 'Customer ID')
                self.customer_id.setText(self.customer_id.text()[:-1])
            if len(self.market_group.text()) > 50:
                self.input_alert(1, 'Market Group')
                self.market_group.setText(self.market_group.text()[:-1])
        except Exception as err:
            print(err)
            logger.info(err, exc_info=True)

    def input_alert(self, errno, item):
        if errno == 1:
            msg = QMessageBox()
            msg.setWindowTitle("{} too long".format(item))
            msg.setText('{} you entered is too long'.format(item))
            x = msg.exec_()

    def load_data(self, customer_id):
        engine = create_engine(db_link, echo=False)
        metadata = MetaData(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            # print('loading')
            cus = session.query(Customer).filter_by(id=customer_id).first()
            print('checking title in db:' + cus.title)
            if cus.title == 'ms':
                self.title_box.setCurrentIndex(1)
            elif cus.title == 'mr':
                self.title_box.setCurrentIndex(2)
            elif cus.title == 'other':
                self.title_box.setCurrentIndex(3)
            self.city.setText(cus.city)
            self.company_name.setText(cus.company_name)
            self.title_box.setCurrentText(cus.title)
            self.other_title.setText(cus.other_title)
            self.fax1.setText(cus.fax_number_prefix)
            self.fax2.setText(cus.fax_number)
            self.phone1.setText(cus.phone_number_prefix)
            self.phone2.setText(cus.phone_number)
            self.last_name.setText(cus.last_name)
            self.first_name.setText(cus.first_name)
            self.country.setText(cus.country)
            self.email1.setText(cus.email_one)
            self.email2.setText(cus.email_two)
            self.email3.setText(cus.email_three)
            self.full_name.setText(cus.contact_name)
            self.addr1.setText(cus.address_one)
            self.addr2.setText(cus.address_two)
            self.addr3.setText(cus.address_three)
            self.postcode.setText(cus.post_code)
            self.market_group.setText(cus.market_group)
            self.notes.setText(cus.notes)
            self.batch.setText(cus.batch)
        except Exception as err:
            logger.info(err, exc_info=True)
            print(err)

        self.first_name.textChanged.connect(self.get_full_name)
        self.last_name.textChanged.connect(self.get_full_name)

        # input limitation
        self.addr3.textChanged.connect(self.limitation)
        self.addr2.textChanged.connect(self.limitation)
        self.addr1.textChanged.connect(self.limitation)
        self.last_name.textChanged.connect(self.limitation)
        self.first_name.textChanged.connect(self.limitation)
        self.company_name.textChanged.connect(self.limitation)
        self.country.textChanged.connect(self.limitation)
        self.city.textChanged.connect(self.limitation)
        # self.customer_id.textChanged.connect(self.limitation)
        self.email3.textChanged.connect(self.limitation)
        self.email2.textChanged.connect(self.limitation)
        self.email1.textChanged.connect(self.limitation)

        self.other_title.textChanged.connect(self.limitation)
        self.market_group.textChanged.connect(self.limitation)
        self.phone2.textChanged.connect(self.limitation)
        self.phone1.textChanged.connect(self.limitation)
        self.fax2.textChanged.connect(self.limitation)
        self.fax1.textChanged.connect(self.limitation)
        self.phone2.textChanged.connect(self.limitation)
        self.phone1.textChanged.connect(self.limitation)
        self.customer_id.textChanged.connect(self.limitation)
        self.batch.textChanged.connect(self.limitation)
        self.notes.textChanged.connect(self.limitation)
        self.full_name.textChanged.connect(self.limitation)

    def title_selected(self, text):
        self.selected_title = text
        print(self.selected_title)

    def print(self):
        self.window = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
        self.ui = Print.Ui_Dialog()
        print('coming')
        customer_id = self.customer_id.text()
        if customer_id:
            # check if exist
            engine = create_engine(db_link, echo=False)
            metadata = MetaData(engine)
            Session = sessionmaker(bind=engine)
            session = Session()
            cus = session.query(Customer).filter_by(id=customer_id).first()
            if cus:
                try:
                    self.ui.setupUi(self.window, [customer_id])
                    self.window.show()
                    self.ui.init_data()
                except Exception as err:
                    logger.info(err, exc_info=True)
                    print(err)

            else:
                msg = QMessageBox()
                msg.setWindowTitle("Customer not found")
                msg.setText('Customer {} not found'.format(customer_id))
                x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Try again")
            msg.setText('Customer ID not specified')
            x = msg.exec_()

    def save(self):
        id = self.customer_id.text().strip()
        batch = self.batch.text().strip()
        company_name = self.company_name.text().strip()
        contact_name = self.full_name.text().strip()
        title = self.title_box.currentText().strip()
        other_title = self.other_title.text().strip()
        first_name = self.first_name.text().strip()
        last_name = self.last_name.text().strip()
        market_group = self.market_group.text().strip()
        address_one = self.addr1.text().strip()
        address_two = self.addr2.text().strip()
        address_three = self.addr3.text().strip()
        phone_number_prefix = self.phone1.text().strip()
        phone_number = self.phone2.text().strip()
        fax_number_prefix = self.fax1.text().strip()
        fax_number = self.fax2.text().strip()
        city = self.city.text().strip()
        country = self.country.text().strip()
        post_code = self.postcode.text().strip()
        notes = self.notes.toPlainText().strip()
        email_one = self.email1.text().strip()
        email_two = self.email2.text().strip()
        email_three = self.email3.text().strip()
        print(title)
        if self.edit == False:
            try:
                engine = create_engine(db_link, echo=False)
                metadata = MetaData(engine)
                Session = sessionmaker(bind=engine)
                session = Session()
                print('saving:' + title)
                if session.query(Customer).filter_by(id=id).first():
                    msg = QMessageBox()
                    msg.setWindowTitle("Duplicated Customer ID")
                    msg.setText('Please edit your customer ID')
                    x = msg.exec_()
                else:
                    # create_date = session.query(Customer).filter_by(id=id).first().create_date
                    # session.query(Customer).filter_by(id=id).first().delete(synchronize_session=False)
                    cus = Customer(id=id,batch=batch,company_name=company_name, contact_name=contact_name, title=title, other_title=other_title,
                             first_name=first_name, last_name=last_name, market_group=market_group, address_one=address_one,
                             address_two=address_two, address_three=address_three, phone_number_prefix=phone_number_prefix,
                             phone_number=phone_number, fax_number_prefix=fax_number_prefix, fax_number=fax_number, city=city,
                             post_code=post_code, notes=notes, email_one=email_one, email_two=email_two, email_three=email_three,country=country,
                             )
                    session.add(cus)
                    session.commit()
                    self.the_signal.emit()
            except Exception as err:
                print(err)
                logger.info(err, exc_info=True)
        else:
            try:
                print('sttst')
                engine = create_engine(db_link, echo=False)
                metadata = MetaData(engine)
                Session = sessionmaker(bind=engine)
                session = Session()
                exist = session.query(Customer).filter_by(id=id).first()
                if id == self.original_id:
                    cus = session.query(Customer).filter_by(id=id).first()
                    cus.company_name = company_name
                    cus.contact_name = contact_name
                    cus.batch = batch
                    cus.title, cus.other_title, cus.first_name, cus.last_name = title,other_title,first_name,last_name
                    cus.market_group, cus.address_one, cus.address_two, cus.address_three = market_group, address_one, address_two, address_three
                    cus.phone_number_prefix, cus.phone_number, cus.fax_number_prefix, cus.fax_number = phone_number_prefix,phone_number,fax_number_prefix,fax_number
                    cus.city,cus.post_code,cus.notes,cus.email_one,cus.email_two,cus.email_three = city,post_code,notes,email_one,email_two,email_three
                    cus.country = country

                elif exist:
                    msg = QMessageBox()
                    msg.setWindowTitle("Duplicated Customer ID")
                    msg.setText('Please edit your customer ID')
                    x = msg.exec_()
                else:
                    print('saving:' + title)
                    cus = Customer(id=id, company_name=company_name, contact_name=contact_name, title=title,batch=batch,
                                   other_title=other_title,
                                   first_name=first_name, last_name=last_name, market_group=market_group,
                                   address_one=address_one,
                                   address_two=address_two, address_three=address_three,
                                   phone_number_prefix=phone_number_prefix,
                                   phone_number=phone_number, fax_number_prefix=fax_number_prefix, fax_number=fax_number,
                                   city=city,
                                   post_code=post_code, notes=notes, email_one=email_one, email_two=email_two, country=country,
                                   email_three=email_three
                                   )
                    session.add(cus)
                session.commit()
                self.the_signal.emit()
            except Exception as err:
                print(err)
                logger.info(err, exc_info=True)


    def delete(self):
        msg = QMessageBox()
        msg.setWindowTitle("Delete")
        msg.setText("Do you want to delete this record? You will lose your data")
        msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.No)
        msg.buttonClicked.connect(self.popup_button)
        x = msg.exec_()

    def popup_button(self, i):
        print(i.text())
        if i.text() == '&Yes':
            print('deleting')
            try:
                print(self.selected)
                to_delete = self.customer_id.text()
                engine = create_engine(db_link, echo=False)
                metadata = MetaData(engine)
                Session = sessionmaker(bind=engine)
                session = Session()
                session.query(Customer).filter_by(id=to_delete).first().delete(synchronize_session=False)
                session.commit()
                # remove clicked status
                self.selected = []
                # self.tableWidget.row
                self.clear()
                self.init_data()
            except Exception as err:
                logger.info(err, exc_info=True)
                print(err)
            finally:
                session.close()
        else:
            pass

    def customer_changed(self):
        if self.customer_id.text() != self.original_id:
            self.save_button.setText('Save New')
        else:
            self.save_button.setText('Update')