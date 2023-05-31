import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication,QMainWindow,
QVBoxLayout,QHBoxLayout,QPushButton,QStackedLayout,
QWidget,QLabel,QLineEdit,QGridLayout,QComboBox,QSpinBox)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reserva")
        self.setFixedSize(QSize(600,300))
        window=QVBoxLayout()
        Header=QHBoxLayout()
        self.body=QStackedLayout()

        boton1=QPushButton("Normal")
        boton2=QPushButton("Evento")
        Header.addWidget(boton1)
        Header.addWidget(boton2)

        boton1.clicked.connect(self.cambiar_a_layout_1)
        boton2.clicked.connect(self.cambiar_a_layout_2)

        contenedor1 = QWidget()
        layout1 = QVBoxLayout(contenedor1)
        contenedor2 = QWidget()
        layout2 = QVBoxLayout(contenedor2)

        grid1=QGridLayout()
        normal=QLabel("Reserva de tipo normal")        
        nor_nombre_reserva=QLabel("Nombre de la reserva:")
        self.nor_nombre=QLineEdit()
        nor_area_reserva=QLabel("Area de la Reserva:")
        self.nor_area=QComboBox()
        self.nor_area.insertItem(0,"Gran salon Central")
        self.nor_area.insertItem(1,"Sala Varas")
        self.nor_area.insertItem(2,"Sala Montt")
        self.nor_area.insertItem(3,"Terraza")
        nor_hora_reserva=QLabel("Hora de la reserva:")
        self.nor_hora=QLineEdit("dia/mes")
        nor_tipo_reserva=QLabel("Plan de comida:")
        self.nor_tipo=QComboBox()
        self.nor_tipo.insertItem(0,"Inicial-$20000")
        self.nor_tipo.insertItem(1,"Intermedio-$45000")
        self.nor_tipo.insertItem(2,"Avanzado-$60000")
        nor_cantidad_reserva=QLabel("Cantidad de comensales:")
        self.nor_cantidad=QSpinBox()
        normal_btn=QPushButton("Hacer reserva")
        normal_btn.clicked.connect(self.guardar_reserva_nor)

        grid1.addWidget(nor_nombre_reserva,0,0)
        grid1.addWidget(self.nor_nombre,0,1)
        grid1.addWidget(nor_area_reserva,1,0)
        grid1.addWidget(self.nor_area,1,1)
        grid1.addWidget(nor_hora_reserva,2,0)
        grid1.addWidget(self.nor_hora,2,1)
        grid1.addWidget(nor_tipo_reserva,3,0)
        grid1.addWidget(self.nor_tipo,3,1)
        grid1.addWidget(nor_cantidad_reserva,4,0)
        grid1.addWidget(self.nor_cantidad,4,1)
        grid1.addWidget(normal_btn,5,1)

        layout1.addWidget(normal)
        layout1.addLayout(grid1)

        grid2=QGridLayout()
        evento=QLabel("Reserva de tipo evento")
        ev_nombre_reserva=QLabel("Nombre de la reserva:")
        self.ev_nombre=QLineEdit()
        ev_area_reserva=QLabel("Area de la Reserva:")
        self.ev_area=QComboBox()
        self.ev_area.insertItem(0,"Gran salon Central")
        self.ev_area.insertItem(1,"Sala Varas")
        self.ev_area.insertItem(2,"Sala Montt")
        self.ev_area.insertItem(3,"Terraza")
        ev_hora_reserva=QLabel("Hora de la reserva:")
        self.ev_hora=QLineEdit()
        ev_tipo_reserva=QLabel("Tipo de reserva:")
        self.ev_tipo=QComboBox()
        self.ev_tipo.insertItem(0,"Cerrada")
        self.ev_tipo.insertItem(1,"Semi-Cerrada")
        self.ev_tipo.insertItem(2,"Abierta")
        ev_cantidad_reserva=QLabel("Cantidad de asistentes:")
        self.ev_cantidad=QSpinBox()
        event_btn=QPushButton("Hacer reserva")

        grid2.addWidget(ev_nombre_reserva,0,0)
        grid2.addWidget(self.ev_nombre,0,1)
        grid2.addWidget(ev_area_reserva,1,0)
        grid2.addWidget(self.ev_area,1,1)
        grid2.addWidget(ev_hora_reserva,2,0)
        grid2.addWidget(self.ev_hora,2,1)
        grid2.addWidget(ev_tipo_reserva,3,0)
        grid2.addWidget(self.ev_tipo,3,1)
        grid2.addWidget(ev_cantidad_reserva,4,0)
        grid2.addWidget(self.ev_cantidad,4,1)
        grid2.addWidget(event_btn,5,1)
        
        layout2.addWidget(evento)
        layout2.addLayout(grid2)

        self.body.addWidget(contenedor1)
        self.body.addWidget(contenedor2)

        window.addLayout(Header)
        window.addLayout(self.body)

        ventana = QWidget()
        ventana.setLayout(window)
        self.setCentralWidget(ventana)

    def cambiar_a_layout_1(self):
        self.body.setCurrentIndex(0)
        
    def cambiar_a_layout_2(self):
        self.body.setCurrentIndex(1)
    def guardar_reserva_nor(self):
        nombre=self.nor_nombre.text()
        area=self.nor_area.currentText()
        hora=self.nor_hora.text()
        tipo=self.nor_tipo.currentText()
        cantidad=self.nor_cantidad.text()
        print(f"{nombre},{area},{hora},{tipo},{cantidad}")

if __name__ == "__main__":
    
    lista_usuario = [] # list()
    
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()