# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error


class Ui_MainWindow(object):
    def __init__(self):
        # Setup koneksi ke database MySQL
        try:
            self.conn = mysql.connector.connect(
                host='localhost',  # Sesuaikan dengan host database Anda
                user='root',       # Sesuaikan dengan username Anda
                password='',       # Sesuaikan dengan password Anda
                database='db_kampus'
            )
            self.cursor = self.conn.cursor()
            print("Koneksi berhasil!")
        except Error as e:
            print(f"Error: {e}")
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(616, 618)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(41, 171, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(31, 241, 521, 261))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(31, 1, 201, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(32, 170, 320, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_isi = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_isi.setObjectName("pushButton_isi")
        self.pushButton_isi.clicked.connect(self.insert_data)  # Connect Insert
        self.horizontalLayout.addWidget(self.pushButton_isi)
        self.pushButton_hapus = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_hapus.setObjectName("pushButton_hapus")
        self.pushButton_hapus.clicked.connect(self.delete_data)  # Connect Delete
        self.horizontalLayout.addWidget(self.pushButton_hapus)
        self.pushButton_ubah = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_ubah.setObjectName("pushButton_ubah")
        self.pushButton_ubah.clicked.connect(self.update_data)  # Connect Update
        self.horizontalLayout.addWidget(self.pushButton_ubah)
        self.pushButton_baca = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_baca.setObjectName("pushButton_baca")
        self.pushButton_baca.clicked.connect(self.read_data)  # Connect Read
        self.horizontalLayout.addWidget(self.pushButton_baca)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(31, 241, 521, 259))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
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
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(41, 531, 511, 25))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_cari = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_cari.setObjectName("pushButton_cari")
        self.pushButton_cari.clicked.connect(self.search_data)  # Connect Search
        self.horizontalLayout_2.addWidget(self.pushButton_cari)
        self.lineEdit_cari = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_cari.setObjectName("lineEdit_cari")
        self.horizontalLayout_2.addWidget(self.lineEdit_cari)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(250, 0, 301, 126))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_npm = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_npm.setObjectName("lineEdit_npm")
        self.verticalLayout_4.addWidget(self.lineEdit_npm)
        self.lineEdit_nama = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_nama.setObjectName("lineEdit_nama")
        self.verticalLayout_4.addWidget(self.lineEdit_nama)
        self.lineEdit_kelas = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_kelas.setObjectName("lineEdit_kelas")
        self.verticalLayout_4.addWidget(self.lineEdit_kelas)
        self.lineEdit_jurusan = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_jurusan.setObjectName("lineEdit_jurusan")
        self.verticalLayout_4.addWidget(self.lineEdit_jurusan)
        self.lineEdit_tgl = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_tgl.setObjectName("lineEdit_tgl")
        self.verticalLayout_4.addWidget(self.lineEdit_tgl)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 616, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Mahasiswa", "From Mahasiswa"))
        self.label_3.setText(_translate("MainWindow", "insert data"))
        self.label.setText(_translate("MainWindow", "NPM"))
        self.label_4.setText(_translate("MainWindow", "Nama"))
        self.label_2.setText(_translate("MainWindow", "Kelas"))
        self.label_5.setText(_translate("MainWindow", "Jurusan"))
        self.label_6.setText(_translate("MainWindow", "Tanggal Lahir"))
        self.pushButton_isi.setText(_translate("MainWindow", "Insert Data"))
        self.pushButton_hapus.setText(_translate("MainWindow", "Delete Data"))
        self.pushButton_ubah.setText(_translate("MainWindow", "Update Data"))
        self.pushButton_baca.setText(_translate("MainWindow", "load Data"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NPM"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NAMA"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "KELAS"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "JURUSAN"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "TANGGAL LAHIR"))
        self.pushButton_cari.setText(_translate("MainWindow", "Search"))

    # Fungsi Insert Data
    def insert_data(self):
        npm = self.lineEdit_npm.text()
        nama = self.lineEdit_nama.text()
        kelas = self.lineEdit_kelas.text()
        jurusan = self.lineEdit_jurusan.text()
        tgl = self.lineEdit_tgl.text()

        try:
            query = "INSERT INTO mahasiswa (npm, nama, kelas, jurusan, tanggal_lahir) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(query, (npm, nama, kelas, jurusan, tgl))
            self.conn.commit()
            print("Data berhasil disimpan.")
        except Error as e:
            print(f"Error: {e}")

    # Fungsi Read Data
    def read_data(self):
        try:
            query = "SELECT * FROM mahasiswa"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()

            self.tableWidget.setRowCount(len(rows))
            for i, row in enumerate(rows):
                for j, val in enumerate(row):
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))
            print("Data berhasil dibaca.")
        except Error as e:
            print(f"Error: {e}")

    # Fungsi Update Data
    def update_data(self):
        npm = self.lineEdit_npm.text()
        nama = self.lineEdit_nama.text()
        kelas = self.lineEdit_kelas.text()
        jurusan = self.lineEdit_jurusan.text()
        tgl = self.lineEdit_tgl.text()

        try:
            query = "UPDATE mahasiswa SET nama = %s, kelas = %s, jurusan = %s, tanggal_lahir = %s WHERE npm = %s"
            self.cursor.execute(query, (nama, kelas, jurusan, tgl, npm))
            self.conn.commit()
            print("Data berhasil diupdate.")
        except Error as e:
            print(f"Error: {e}")

    # Fungsi Delete Data
    def delete_data(self):
        npm = self.lineEdit_npm.text()
        try:
            query = "DELETE FROM mahasiswa WHERE npm = %s"
            self.cursor.execute(query, (npm,))
            self.conn.commit()
            print("Data berhasil dihapus.")
        except Error as e:
            print(f"Error: {e}")

    # Fungsi Search Data
    def search_data(self):
        keyword = self.lineEdit_cari.text()
        try:
            query = f"SELECT * FROM mahasiswa WHERE npm LIKE '%{keyword}%' OR nama LIKE '%{keyword}%'"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()

            self.tableWidget.setRowCount(len(rows))
            for i, row in enumerate(rows):
                for j, val in enumerate(row):
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))
            print("Data pencarian selesai.")
        except Error as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
