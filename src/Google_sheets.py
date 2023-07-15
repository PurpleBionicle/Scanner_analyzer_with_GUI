import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials



class Google_sheets():
    def __init__(self):
        """
        Конструктор реализует подключение и авторизацию
        """
        CREDENTIALS_FILE = 'creds.json'
        self.spreadsheet_id = '17M3TZf863oP0lsw3efMPXbZelDqlApPfUbBZn3AX_0U'
        # Авторизуемся и получаем service — экземпляр доступа к API
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        # self.service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)
        try:
            self.service = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials)
        except:
            DISCOVERY_SERVICE_URL = 'https://sheets.googleapis.com/$discovery/rest?version=v4'
            self.service = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials,
                                                           discoveryServiceUrl=DISCOVERY_SERVICE_URL)

    def write(self, page, params) -> None:
        """
        Чтение из файла для получения последней строки.
        В следующую запишем новую строку
        :param page: в какую страницу пишем
        :param params: что пишем
        :return: ничего
        """

        "Найдем число записей"
        values = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range=f'{page}!A1:B10000',
            majorDimension='COLUMNS'
        ).execute()
        count_records: int = len(values['values'][0])

        "Запись в файл на след строчку от имеющегося количества"
        values = self.service.spreadsheets().values().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={
                "valueInputOption": "USER_ENTERED",
                "data": [
                    {"range": f"{page}!A{count_records + 1}:H{count_records + 1}",
                     "majorDimension": "ROWS",
                     "values": [params]},

                ]
            }
        ).execute()
