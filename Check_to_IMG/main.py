from requirements import *

if not os.path.isdir("..\\OUTPUT"):
    os.mkdir("..\\OUTPUT")
with open('../INPUT.txt', 'r+') as file:
    url_list = file.read().split('\n')


headers = {
    'User-Agent': 'Mozilla/5.0 '
                  '(Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 '
                  '(KHTML, like Gecko) '
                  'Chrome/128.0.0.0 '
                  'Safari/537.36 '
                  'Edg/128.0.0.0',
    'Cookie': 'is_gdpr=0; receive-cookie-deprecation=1; yashr'
              '=1666291441721599112; yuidss=9377415061721599111; '
              'ymex=2036995598.yrts.1721635598; gdpr=0; _ym_uid'
              '=1722074401590219338; is_gdpr_b=CMfBHhDliQIoAg==; '
              'L=RlhcX1d2ZlxNU3NBeF17Wnp1XAxeWFFdHzEMFxpNGQ0ESlo'
              '=.1722074633.15820.393838'
              '.40a164a6586e49bc9ee782203a2ff03e; yandex_login'
              '=frank.ufa22; '
              'yp=2037434633.udn.cDpGcmFuayBieSDQkdCw0YHRgtCwIFVGQQ%3D%3D#2037434633'
              '.multib.1#1737858487.szm.1_25'
              ':1536x864:1519x730; my=YwA=; amcuid=2506127561722586319; '
              'yandexuid=9377415061721599111; '
              'i=gj7pZH2d4OglrwQo6U1sEXNBAiXPdEUgV2+fVAbqyInnzjuhGSjSm5bkYumnZkYsdG1M'
              '+AkgeAjyq6L3j/L3o7zegxc=; '
              '_ym_isad=2; Session_id=3:1725373215.5.1.1722074429350:bJi9WQ'
              ':c8.1.2:1|755564650.0.2.3:1722074429'
              '|1946916540.204.2.2:204.3:1722074633|3:10294741.479533'
              '.m9yktRmhL4wW_GDxEq-W3WexSGk; '
              'sessar=1.1193.CiCWmwxiPEqFXFjRSDzKUyeODlD9LTvujm-CuS3zEa5xAg'
              '.3qqx8xBct3r8TemkgK7s7qEedfLA9VdNfWVyUka5QZ0; '
              'sessionid2=3:1725373215.5.1.1722074429350:bJi9WQ:c8.1.2:1|'
              '755564650.0.2.3:1722074429|1946916540.204.2'
              '.2:204.3:1722074633|3:10294741.479533.fakesign0000000000000000000; yabs-vdrf=A0; '
              '_yasc=HRGS0RW7SuIuiYRLAX3M5pIXpV2m0IDvMFngSQm3GmDI22eYLvk4gSDQLWU2MK6cidEyMDVQYNeGdtUJ4Q==; '
              'bh'
              '=EkIiQ2hyb21pdW0iO3Y9IjEyOCIsICJOb3Q7QT1CcmFuZCI7dj0iMjQiLCAiTWljcm'
              '9zb2Z0IEVkZ2UiO3Y9IjEyOCIaBSJ4ODYiIh'
              'AiMTI2LjAuNjQ3OC4xODUiKgI/MDoJIldpbmRvd3MiQggiMTUuMC4wIkoEIjY0IlJbIk'
              '5vdC9BKUJyYW5kIjt2PSI4LjAuMC4wIiwiQ'
              '2hyb21pdW0iO3Y9IjEyNi4wLjY0NzguMTg1IiwiR29vZ2xlIENocm9tZSI7dj0iMTI2L'
              'jAuNjQ3OC4xODUiImCa0t22Bg=='
}

_name = '1234567890'
imgh = 1
for url in url_list:
    _config = imgkit.config(wkhtmltoimage='wkhtmltopdf\\bin\\wkhtmltoimage.exe')
    _name = str(abs(hash(_name)))
    r = requests.get(url, headers=headers)
    with open('temp.html', 'wb') as _file:
        _file.write(r.text.encode('utf-8'))
    imgkit.from_file('temp.html', f'..\\OUTPUT\\{_name}.jpg', config=_config)
    os.system('cls')
    print('Пожалуйста, не закрывайте это окно до окончания работы программы!')
    print(f'Завершено {imgh} из {len(url_list)}')
    imgh += 1
os.remove('temp.html')
os.system('cls')
input('Все готово!\n'
      'Закрыть консоль можно напрямую,\n'
      'либо нажать клавишу "Enter"')
