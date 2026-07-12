
from PySide6.QtWidgets import *
import sys

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LifeOS Demo")
        c=QWidget(); self.setCentralWidget(c)
        v=QVBoxLayout(c)
        v.addWidget(QLabel("<h1>LifeOS Dashboard</h1><h3>Welcome Abhiyank 👋</h3>"))
        grid=QGridLayout()
        cards=[("Weight","62.4 kg"),("Goal","65 kg"),("Workout","Completed"),
               ("Sleep","7h 45m"),("Water","2.8 L"),("Hair","Done")]
        for i,(k,val) in enumerate(cards):
            g=QGroupBox(k)
            gv=QVBoxLayout(g)
            gv.addWidget(QLabel(f"<b>{val}</b>"))
            grid.addWidget(g,i//3,i%3)
        v.addLayout(grid)
        for label,val in [("Protein",82),("Calories",74),("AI-103",63)]:
            v.addWidget(QLabel(label))
            p=QProgressBar(); p.setValue(val)
            v.addWidget(p)

app=QApplication(sys.argv)
w=Main()
w.resize(700,500)
w.show()
app.exec()
