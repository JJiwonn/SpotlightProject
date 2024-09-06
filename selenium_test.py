from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = './crawler/drivers/chromedriver.exe'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
#chrome_options.add_argument("--headless")  # 크롬창이 열리지 않음
#chrome_options.add_argument("--no-sandbox")  # GUI를 사용할 수 없는 환경에서 설정, linux, docker 등
#chrome_options.add_argument("--disable-gpu")  # GUI를 사용할 수 없는 환경에서 설정, linux, docker 등
#chrome_options.add_argument(f"--window-size={WINDOW_SIZE}")
#chrome_options.add_argument('Content-Type=application/json; charset=utf-8')

# Service 객체 생성
service = Service(executable_path=CHROMEDRIVER_PATH)

# WebDriver 초기화
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://section.blog.naver.com')

driver.quit()