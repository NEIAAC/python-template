from PySide6.QtCore import QThread, Signal

from utils.logger import LogLevel, logger


class ExampleThread(QThread):
    """Example thread to run tasks in the background and send events to the main UI thread."""

    outputSignal = Signal(str, str)

    def __init__(self, firstInput: str, secondInput: str | None = None):
        super().__init__()
        self.firstInput = firstInput
        self.secondInput = secondInput

    def output(self, text: str, level: LogLevel = LogLevel.INFO):
        logger.log(level.value, text)
        self.outputSignal.emit(text, level.value)

    def run(self):
        try:
            inputs = self.__dict__.copy()
            logger.info(
                f"Starting example thread with input parameters: {inputs}"
            )
            self.output("...")
            self.output("Your first input was: " + self.firstInput)
            self.output(
                "If you entered text in the second input it will be shown here after 3 seconds"
            )
            self.msleep(1500)
            try:
                raise Exception("This is an example error after 1.5 seconds")
            except Exception as e:
                self.output(str(e), LogLevel.ERROR)
            self.msleep(1500)
            if self.secondInput:
                self.output("Your second input was: " + self.secondInput)
        except Exception as error:
            self.output(
                f"An unexpected error occurred: {error}",
                LogLevel.ERROR,
            )
