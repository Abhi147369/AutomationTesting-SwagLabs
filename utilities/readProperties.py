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
    def getchceckoutInformationName():
        chceckoutInformationName = config.get('checkout info', 'chceckoutInformationName')
        return chceckoutInformationName

    @staticmethod
    def getchceckoutInformationLastName():
        chceckoutInformationLastName = config.get('checkout info', 'chceckoutInformationLastName')
        return chceckoutInformationLastName

    @staticmethod
    def getchceckoutInformationZipcode():
        chceckoutInformationZipcode = config.get('checkout info', 'chceckoutInformationZipcode')
        return chceckoutInformationZipcode


