import time
from seleniumwire.utils import decode
from seleniumwire import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

def response_interceptor(request, response):  # A response interceptor takes two args
    print(request.url,
          " " + request.method,
          "\nrequestDate: " + f"{request.date:%d/%m/%Y, %H:%M:%S}.{request.date.microsecond // 1000:03d}",
          "\nresponseDate: " + f"{response.date:%d/%m/%Y, %H:%M:%S}.{response.date.microsecond // 1000:03d}",
          "\nhost: " + request.host,
          "\npath: " + request.path,
          "\nquery: " + request.querystring,
          "\nparams: " + str(request.params),
          "\nstatusCode: " + str(response.status_code),
          "\nreason: " + response.reason,
          "\nbody bytes count: " + str(len(response.body)))
          # "\nbody partial: " + response.body.decode('utf-8')[:20])

# f"{response.date:%Y-%m-%d %H:%M:%S}.{response.date.microsecond // 1000:03d}"
# request.date.strftime("%m/%d/%Y, %H:%M:%S.%f")[:-3]
# decode(response.body, response.headers.get('Content-Encoding', 'identity'))
# request.body.decode('utf-8')

def inspected(request):
    print(request.url)

# driver.request_interceptor = inspected
driver.response_interceptor = response_interceptor

driver.get('https://piter-online.net/')
# time.sleep(3)
driver.quit()
