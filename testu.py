import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMenuBar, QAction, QMessageBox

class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Create labels and input fields for weight and height
        self.weight_label = QLabel('Weight (kg):')
        self.weight_input = QLineEdit()
        
        self.height_label = QLabel('Height (m):')
        self.height_input = QLineEdit()
        
        # Create a button to calculate BMI
        self.calc_button = QPushButton('Calculate BMI')
        self.calc_button.clicked.connect(self.calculate_bmi)
        
        # Create a label to display the BMI result
        self.result_label = QLabel('BMI: ')
        
        # Create a label to display the BMI status
        self.status_label = QLabel('Status: ')
        
        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.calc_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.status_label)
        
        # Create menu bar
        self.menu_bar = QMenuBar()
        file_menu = self.menu_bar.addMenu('File')
        clear_action = QAction('Clear', self)
        clear_action.triggered.connect(self.clear_fields)
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(clear_action)
        file_menu.addAction(exit_action)

        help_menu = self.menu_bar.addMenu('Help')
        help_action = QAction('How to Use', self)
        help_action.triggered.connect(self.show_help)
        help_menu.addAction(help_action)

        menu_layout = QHBoxLayout()
        menu_layout.addWidget(self.menu_bar)

        main_layout = QVBoxLayout()
        main_layout.addLayout(menu_layout)
        main_layout.addLayout(layout)
        
        self.setLayout(main_layout)
        self.setWindowTitle('BMI Calculator')
        self.show()
    
    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())
            bmi = weight / (height ** 2)
            self.result_label.setText(f'BMI: {bmi:.2f}')
            self.update_status(bmi)
        except ValueError:
            self.result_label.setText('Invalid input!')
            self.status_label.setText('')
    
    def update_status(self, bmi):
        if bmi < 18.5:
            status = 'Underweight'
        elif 18.5 <= bmi < 25:
            status = 'Normal'
        elif 25 <= bmi < 30:
            status = 'Overweight'
        else:
            status = 'Obese'
        self.status_label.setText(f'Status: {status}')
    
    def clear_fields(self):
        self.weight_input.clear()
        self.height_input.clear()
        self.result_label.setText('BMI: ')
        self.status_label.setText('Status: ')
    
    def show_help(self):
        help_text = """
        To use the BMI Calculator:
        1. Enter your weight in kilograms.
        2. Enter your height in meters.
        3. Click "Calculate BMI" to see your BMI and status.
        """
        QMessageBox.information(self, 'How to Use', help_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BMICalculator()
    sys.exit(app.exec_())
