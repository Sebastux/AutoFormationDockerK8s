import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, 
    QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)

class UserFormApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test Compilation PySide6")
        self.resize(400, 300)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Nom
        nom_layout = QHBoxLayout()
        self.nom_label = QLabel("Nom :")
        self.nom_input = QLineEdit()
        nom_layout.addWidget(self.nom_label)
        nom_layout.addWidget(self.nom_input)
        layout.addLayout(nom_layout)

        # Prénom
        prenom_layout = QHBoxLayout()
        self.prenom_label = QLabel("Prénom :")
        self.prenom_input = QLineEdit()
        prenom_layout.addWidget(self.prenom_label)
        prenom_layout.addWidget(self.prenom_input)
        layout.addLayout(prenom_layout)

        # Adresse postale
        adresse_layout = QVBoxLayout()
        self.adresse_label = QLabel("Adresse postale :")
        self.adresse_input = QTextEdit()
        adresse_layout.addWidget(self.adresse_label)
        adresse_layout.addWidget(self.adresse_input)
        layout.addLayout(adresse_layout)

        # Bouton de sauvegarde
        self.save_button = QPushButton("Enregistrer")
        self.save_button.clicked.connect(self.save_data)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_data(self):
        nom = self.nom_input.text()
        prenom = self.prenom_input.text()
        adresse = self.adresse_input.toPlainText()

        filename = "user_info.txt"
        
        # Écrasement direct sans confirmation comme demandé
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Nom : {nom}\n")
            f.write(f"Prénom : {prenom}\n")
            f.write(f"Adresse :\n{adresse}\n")
            
        QMessageBox.information(self, "Succès", f"Données enregistrées dans {filename}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = UserFormApp()
    form.show()
    sys.exit(app.exec())