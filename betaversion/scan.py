from aip import AipOcr

APP_ID = '10867219'
API_KEY = 'nD7DipMuUxm2XWPDVGyUAqa5'
SECRET_KEY = 'yweIEHFiaEsr66LZnlqGoO6OjrdltkOQ'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image=get_file_content(r'F:\图片\u=390994034,2039969572&fm=173&s=0450E433119EC5C80ED5C5DA000080B3&w=640&h=504&img.jpg')

res=client.general(image)
for i in res['words_result']:
    print(i['words'])

