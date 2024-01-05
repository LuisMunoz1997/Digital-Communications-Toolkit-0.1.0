import sys
import numpy as np
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import adi

# Configuración del Adalm Pluto SDR
sdr = adi.Pluto()

# Configuración de la ventana de la aplicación PyQt
app = QtGui.QApplication(sys.argv)
win = pg.GraphicsWindow(title="Gráfica en tiempo real")
p = win.addPlot(title="Datos en tiempo real")
curve = p.plot(pen='y')

# Variables para la adquisición de datos
samples = None
data_ready = False

# Función para recibir muestras en un hilo separado
def receive_samples():
    global samples, data_ready
    while True:
        if not stop_flag:
            samples = sdr.rx()
            data_ready = True
        else:
            break

# Función para actualizar la gráfica en un hilo separado
def update_plot():
    while True:
        if not stop_flag:
            if data_ready:
                curve.setData(samples)
                data_ready = False
        else:
            break

# Crear e iniciar los hilos
receive_thread = QtCore.QThread()
receive_worker = QtCore.QRunnable(receive_samples)
receive_worker.moveToThread(receive_thread)
receive_thread.started.connect(receive_worker.run)
receive_thread.start()

update_thread = QtCore.QThread()
update_worker = QtCore.QRunnable(update_plot)
update_worker.moveToThread(update_thread)
update_thread.started.connect(update_worker.run)
update_thread.start()

# Crear botón de detener
stop_flag = False

def stop_threads():
    global stop_flag
    stop_flag = True

button = QtGui.QPushButton('Detener')
button.clicked.connect(stop_threads)
win.addWidget(button)

# Iniciar la aplicación PyQt
if __name__ == '__main__':
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
