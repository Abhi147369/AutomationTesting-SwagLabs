import configparser

config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def checkoutInformationName():
        checkoutInformationName = config.get('checkout info', 'checkoutInformationName')
        return checkoutInformationName

    @staticmethod
    def checkoutInformationLastName():
        checkoutInformationLastName = config.get('checkout info', 'checkoutInformationLastName')
        return checkoutInformationLastName

    @staticmethod
    def checkoutInformationZipcode():
        checkoutInformationZipcode = config.get('checkout info', 'checkoutInformationZipcode')
        return checkoutInformationZipcode

    @staticmethod
    def wrongUsername():
        wrongUsername = config.get('common info', 'wrongUsername')
        return wrongUsername

    @staticmethod
    def wrongPassword():
        wrongPassword = config.get('common info', 'wrongPassword')
        return wrongPassword
