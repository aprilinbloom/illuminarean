from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


# web driver 설정
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(1800, 1300)
driver.get('https://illuminarean.com/')

# 명시적 대기
wait = WebDriverWait(driver, 10)

# 인재 채용 팝업 닫기
popupClose = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/button[2]')))
popupClose.click()

# Work 클릭
headerWork = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/header/div/div/div/div/nav/ul/li[2]/a')))
headerWork.click()

# GOODVIVE WORKS 바로가기 클릭
goodviveWorks = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div/div[2]/div/div[3]/div/a')))
goodviveWorks.click()

# GOODVIVE WORKS 진입
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)

# 무료 체험 신청 클릭
# 무료 체험 신청 텍스트로 식별 가능하여, clickable 사용
trial = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '무료 체험 신청')]")))
trial.click()

# 회사명 입력
# companyName ID가 유일하므로 clickable 사용
companyName = wait.until(EC.element_to_be_clickable((By.ID, 'companyName')))
companyName.send_keys('주식회사김지유')
time.sleep(0.5)

# 대표자명 입력
# ceoName ID가 유일하므로 clickable 사용
ceoName = wait.until(EC.element_to_be_clickable((By.ID, 'ceoName')))
ceoName.send_keys('김지유')
time.sleep(0.5)

# 사업자 유형 선택
# businessType ID가 유일하므로 clickable 사용
businessType = wait.until(EC.element_to_be_clickable((By.ID, 'businessType')))
businessType.click()
time.sleep(0.5)

# '개인' 선택
# 개인에 할당된 ID가 유일하므로 clickable 사용
businessTypeOption = wait.until(EC.element_to_be_clickable((By.ID, 'react-select-businessType-option-0')))
businessTypeOption.click()
time.sleep(0.5)

# 직원수 선택
# scale ID가 유일하므로 clickable 사용
scale = wait.until(EC.element_to_be_clickable((By.ID, 'scale')))
scale.click()
time.sleep(0.5)

# '1000명 이상' 선택
# 1000명 이상에 할당된 ID가 유일하므로 clickable 사용
scaleOption = wait.until(EC.element_to_be_clickable((By.ID, 'react-select-scale-option-6')))
scaleOption.click()
time.sleep(0.5)

# 담당자명 입력
# name ID가 유일하므로 clickable 사용
name = wait.until(EC.element_to_be_clickable((By.ID, 'name')))
name.send_keys('김지유')
time.sleep(0.5)

# 이메일 입력
# email ID가 유일하므로 clickable 사용
email = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
email.send_keys('2applebeans@naver.com')
time.sleep(0.5)

# 휴대폰 번호 입력
# mobile ID가 유일하므로 clickable 사용
mobile = wait.until(EC.element_to_be_clickable((By.ID, 'mobile')))
mobile.send_keys('01027228722')
time.sleep(0.5)

# 담당 업무 선택
# duties class가 유일하므로 clickable 사용
# 정확하게 지정하기 위해 find_element 사용
duties = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'duties')))
dutiesButton = duties.find_element(By.TAG_NAME, 'button')
dutiesButton.click()
time.sleep(0.5)

# 업무명 검색
# 정확하게 지정하기 위해 find_element 사용
dutiesInput = dutiesButton.find_element(By.TAG_NAME, 'input')
dutiesInput.click()
dutiesInput.send_keys('통번역')
dutiesInput.send_keys(Keys.ENTER)
time.sleep(0.5)

# 불러온 담당 duties class 중 첫 번째 형제 찾기
# 정확하게 지정하기 위해 find_element 사용
dutiesDropDown = dutiesButton.find_elements(By.XPATH, 'following-sibling::*[1]')[0]

# 첫 번째 형제의 자식들 모두 찾기
# 정확하게 지정하기 위해 find_element 사용
dutiesDropDownChildren = dutiesDropDown.find_elements(By.XPATH, '*')

# 첫 번째 형제의 첫 번째 자식 찾기
dutiesList = dutiesDropDownChildren[0]

# 첫 번째 형제의 두 번째 자식 찾기
dutiesButtons = dutiesDropDownChildren[1]

# '통번역' 버튼 찾아 클릭
# '통번역' 텍스트로 찾기
# 정확하게 지정하기 위해 find_element 사용
translation = dutiesList.find_element(By.XPATH, "//button[contains(text(), '통번역')]")
translation.click()
time.sleep(0.5)

# 검색 후 검색어 지우기 버튼 찾아 클릭(dutiesButton 닫히지 않도록)
# dutiesInput의 첫 번째 형제
# 정확하게 지정하기 위해 find_element 사용
deleteButton = dutiesInput.find_elements(By.XPATH, 'following-sibling::*[1]')[0]
deleteButton.click()
time.sleep(0.5)

# dutiesButton 클릭
# dutiesButton의 첫 번째 형제
# 정확하게 지정하기 위해 find_element 사용
dutiesButton.click()
dutiesDropDown = dutiesButton.find_elements(By.XPATH, 'following-sibling::*[1]')[0]
time.sleep(0.5)

# '스타일리스트' 버튼 찾아 클릭
# '스타일리스트' 텍스트로 찾기
# 정확하게 지정하기 위해 find_element 사용
stylelist = dutiesList.find_element(By.XPATH, "//button[contains(text(), '스타일리스트')]")
stylelist.click()
time.sleep(0.5)

# 등록 버튼 클릭
# 정확하게 지정하기 위해 find_element 사용
submit = dutiesButtons.find_element(By.XPATH, "//button[contains(text(), '등록')]")
submit.click()
time.sleep(0.5)

# 신청 취소 클릭
# 정확하게 지정하기 위해 find_element 사용
cancel = wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[contains(text(), '신청 취소')]")))
cancel.click()
time.sleep(2)

# 종료
driver.quit()
