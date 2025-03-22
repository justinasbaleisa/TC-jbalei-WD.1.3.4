class Logger:
    # File where game logs will be stored
    LOG_FILE_NAME = "game_log.txt"

    """
    Logs important game events and saves them for debugging.
    """

    def __init__(self):
        """
        Initialize the logger with an empty log list.
        """
        self.logs = []

    def log(self, message):
        """
        Append a message to the log and print it.

        Args:
            message (str): The message to be logged.
        """
        pass

    def save_to_file(self):
        """
        Write all log messages to the specified log file.
        """
        pass
