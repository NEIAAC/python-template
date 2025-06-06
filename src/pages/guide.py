from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtCore import Qt
from qfluentwidgets import (
    BodyLabel,
    SingleDirectionScrollArea,
)


class GuidePage(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Guide")

        self.helpText = BodyLabel(
            """
<h1>Overview</h1>

<p>
    The main page consists of a 2 simple inputs meant to demonstrate some data validation and persitence methods.
    The first input is set as required and the second is optional.
</p>

<p>
    Running the app will display the first input in the logs box and the second after 3 seconds, if it was entered.
    An example error will also be shown halfway through the process. If the app is minimized when the process ends a
    notification will be sent and the app will blink/jump in the taskbar depending on the operating system.
</p>

<p>
    The run logs box is also intended to serve as an example of how to pass data between worker threads and the main UI thread.
</p>

<h1>Tips</h1>

Improvements to build upon when using this template.

    <h3>Certification</h3>

    <ul>
        <li>Sign the app during the build process using a trusted certificate authority.</li>
        <li>These are usually paid services but having the app signed will remove the insecuriy warning from some operating systems.</li>
    </ul>

    <h3>Localization</h3>

    <ul>
        <li>Integrate the Qt translation system into the app.</li>
        <li>Automate some of the translation handling processes.</li>
    </ul>
""",
        )
        self.helpText.setWordWrap(True)

        self.contentWidget = QWidget()
        self.contentLayout = QVBoxLayout(self.contentWidget)
        self.contentLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.contentLayout.setContentsMargins(40, 40, 50, 40)
        self.contentLayout.setSpacing(40)
        self.contentLayout.addWidget(self.helpText)

        self.scrollArea = SingleDirectionScrollArea(
            orient=Qt.Orientation.Vertical
        )
        self.scrollArea.setWidget(self.contentWidget)
        self.scrollArea.setSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding
        )
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.enableTransparentBackground()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.scrollArea)

        self.setLayout(self.mainLayout)
