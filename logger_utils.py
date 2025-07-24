import logging

def get_logger():
    logger=logging.getLogger(__name__)  ##create object from getlogger  ##test case name --> __name__
    filehandler=logging.FileHandler(r"C:\Users\dell\PycharmProjects\Framework_OrangeHRM\logs\test_logs.log")
    formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)  ##filehandler object
    logger.setLevel(logging.DEBUG)   ###to start the execution from this level (optional)
    logger.debug("A debug statement is executed")
    logger.info("This is Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")

    return logger


