import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://aplatamqa.com/portal-alumno/login/new-account?schoolId=36")
driver.maximize_window()

email = driver.find_element(By.XPATH, "//input[@formcontrolname='email']")
email.send_keys("2024070218@test.com")

password = driver.find_element(By.XPATH, "//input[@formcontrolname='password']")
password.send_keys("Test.123")

confirmPassword = driver.find_element(By.XPATH, "//input[@formcontrolname='confirmPassword']")
confirmPassword.send_keys("Test.123")

name = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='name']")))
name.send_keys("Test")

lastName = driver.find_element(By.XPATH, "//input[@formcontrolname='lastName']")
lastName.send_keys("Test")

driver.find_element(By.XPATH, "//a[@role='button']").click()

driver.find_element(By.XPATH, "//i[@class='flag-icon flag-icon-co']").click()

phone = driver.find_element(By.XPATH, "//input[@formcontrolname='phone']")
phone.send_keys("6016014564")

selectCountry = driver.find_element(By.XPATH, "//select[contains(@formcontrolname,'country')]")
country = Select(selectCountry)
country.select_by_value('4: Object')

selectStudyProgram = driver.find_element(By.XPATH, "//select[contains(@placeholder,'Programa')]")
studyProgram = Select(selectStudyProgram)
studyProgram.select_by_value('1: Object')

driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block'][contains(.,'Crear cuenta')]").click()

confirmForm = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='button'][contains(.,'Aceptar')]"))).click()

try:
    #Frame
    iframe = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, "//iframe")))
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe"))
    
except NoSuchElementException as ex:
    print("No se encontro el elemento Frame")

# SECCION DATOS PERSONALES

selectAdmissionType = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='PERSONAL_DATA_admissionType']")))
admissionType = Select(selectAdmissionType)
admissionType.select_by_value('0: Object')

secondName = driver.find_element(By.XPATH, "//input[@id='PERSONAL_DATA_secondName']")
secondName.send_keys("Test")

secondLastName = driver.find_element(By.XPATH, "//input[@id='PERSONAL_DATA_secondLastName']")
secondLastName.send_keys("Test")

selectDocumentType = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_documentType']")
documentType = Select(selectDocumentType)
documentType.select_by_value('0: Object')

documentNumber = driver.find_element(By.XPATH, "//input[contains(@id,'PERSONAL_DATA_documentNumber')]")
documentNumber.send_keys("2024070211")

driver.find_element(By.XPATH, "(//button[contains(@type,'button')])[1]").click() #Fecha de expedicion del documento
selectYear = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//select[@aria-label='Select year']")))
year = Select(selectYear)
year.select_by_value('2020')

selectMonth = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//select[@aria-label='Select month']")))
month = Select(selectMonth)
month.select_by_value('7')

day = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='btn-light ng-star-inserted'])[1]"))).click()

selectCountryDoc = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_countryDoc']")
countryDoc = Select(selectCountryDoc)
countryDoc.select_by_value('0: Object')

selectdeptoDoc = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_dptoDoc']")
deptoDoc = Select(selectdeptoDoc)
deptoDoc.select_by_value('59: Object')
time.sleep(.5)

selectProvDoc = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='PERSONAL_DATA_provDoc']")))
provDoc = Select(selectProvDoc)
provDoc.select_by_value('504: Object')

selectBirthCountry = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_birthCountry']")
birthCountry = Select(selectBirthCountry)
birthCountry.select_by_value('0: Object')

selectBirthDepto = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_birthDpto']")
birthDepto = Select(selectBirthDepto)
birthDepto.select_by_value('59: Object')
time.sleep(.5)

selectBirthProv = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='PERSONAL_DATA_birthProv']")))
birthProv = Select(selectBirthProv)
birthProv.select_by_value('504: Object')

driver.find_element(By.XPATH, "(//button[@type='button'])[2]").click() #Fecha de nacimiento
selectYear = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//select[@aria-label='Select year']")))
year = Select(selectYear)
year.select_by_value('2000')

selectMonth = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//select[@aria-label='Select month']")))
month = Select(selectMonth)
month.select_by_value('7')

day = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='btn-light ng-star-inserted'])[1]"))).click()

selectGender = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_gender']")
gender = Select(selectGender)
gender.select_by_value('0: Object')

selectMaritalStatus = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_maritalStatus']")
maritalStatus = Select(selectMaritalStatus)
maritalStatus.select_by_value('0: Object')

selectHasHandicap = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_hasHandicap']")
hasHandicap = Select(selectHasHandicap)
hasHandicap.select_by_value('1: Object')

'''
selectHandicap = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_handicap']")
handicap = Select(selectHandicap)
handicap.select_by_value('8: Object')

supportRequired = driver.find_element(By.XPATH, "//textarea[@id='PERSONAL_DATA_supportRequired']")
supportRequired.send_keys("Silla de ruedas")

selectIsSignLangUser = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_isSignLangUser']")
isSignLangUser = Select(selectIsSignLangUser)
isSignLangUser.select_by_visible_text("Si")

selectSpecializedDiagnosis = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_specializedDiagnosis']")
specializedDiagnosis = Select(selectSpecializedDiagnosis)
specializedDiagnosis.select_by_value('1: Object')

selectHandicapCert = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_handicapCert']")
handicapCert = Select(selectHandicapCert)
handicapCert.select_by_value('1: Object')

selectHandicapMent = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_handicapMent']")
handicapMent = Select(selectHandicapMent)
handicapMent.select_by_value('1: Object')

selectHandicapPsycho = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_handicapPsycho']")
handicapPsycho = Select(selectHandicapPsycho)
handicapPsycho.select_by_value('1: Object')
'''

selectHasEthnicity = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_hasEthnicity']")
hasEthnicity = Select(selectHasEthnicity)
hasEthnicity.select_by_value('1: Object')

'''

selectEthnicity = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_ethnicity']")
ethnicity = Select(selectEthnicity)
ethnicity.select_by_value('0: Object')

ethnicityDesc = driver.find_element(By.XPATH, "//input[@id='PERSONAL_DATA_ethnicityDesc']")
ethnicityDesc.send_keys("Prueba Etnia")

ethnicityCommunity = driver.find_element(By.XPATH, "//input[@id='PERSONAL_DATA_ethnicityCommunity']")
ethnicityCommunity.send_keys("Prueba pueblo indigena")

selectHasNativeLanguage = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_hasNativeLanguage']")
hasNativeLanguage = Select(selectHasNativeLanguage)
hasNativeLanguage.select_by_value('0: Object')

nativeLanguageDesc = driver.find_element(By.XPATH, "//input[@id='PERSONAL_DATA_nativeLanguageDesc']")
nativeLanguageDesc.send_keys("Prueba lengua nativa")
'''

selectPersonPayment = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_personPayment']")
personPayment = Select(selectPersonPayment)
personPayment.select_by_value('0: Object')

selectIncomeSource = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_incomeSource']")
incomeSource = Select(selectIncomeSource)
incomeSource.select_by_value('0: Object')

driver.find_element(By.XPATH, "(//button[@type='button'])[3]").click()

# SECCION DATOS DE CONTACTO

time.sleep(.5)

selectCountry = driver.find_element(By.XPATH, "//select[@id='CONTACT_DATA_country']")
country = Select(selectCountry)
country.select_by_value('0: Object')

selectDepto = driver.find_element(By.XPATH, "//select[@id='CONTACT_DATA_dpto']")
depto = Select(selectDepto)
depto.select_by_value('59: Object')
time.sleep(.5)

selectProv = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='CONTACT_DATA_prov']")))
prov = Select(selectProv)
prov.select_by_value('504: Object')

driver.find_element(By.XPATH, "//input[@id='CONTACT_DATA_address']").click()

selectStreetType = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='container-basic-part']/div[1]/select")))
streetType = Select(selectStreetType)
streetType.select_by_value('CL')

nameStreet = driver.find_element(By.XPATH, "//input[contains(@id,'val0')]")
nameStreet.send_keys("Test")

houseNumber = driver.find_element(By.XPATH, "//input[@id='val1']")
houseNumber.send_keys("1-2")

selectAddressType = driver.find_element(By.XPATH, "(//select[@name='select'])[5]")
addressType = Select(selectAddressType)
addressType.select_by_value('BRR')

addressDetail = driver.find_element(By.XPATH, "//input[@id='val2']")
addressDetail.send_keys("Test")

driver.find_element(By.XPATH, "//button[contains(.,'Aceptar')]").click()

selectStratum = driver.find_element(By.XPATH, "//select[@id='CONTACT_DATA_stratum']")
stratum = Select(selectStratum)
stratum.select_by_value('0: Object')

driver.execute_script("window.scrollTo(0,200)")

driver.find_element(By.XPATH, "//a[@id='CONTACT_DATA_phoneArea']").click()

driver.find_element(By.XPATH, "(//i[@class='flag-icon flag-icon-co'])[3]").click()

phone = driver.find_element(By.XPATH, "//input[contains(@id,'CONTACT_DATA_phone')]")
phone.send_keys("6014567812")

emailAlternative = driver.find_element(By.XPATH, "//input[@id='CONTACT_DATA_emailAlternative']")
emailAlternative.send_keys("test@test.com")

driver.find_element(By.XPATH, "(//button[@type='button'])[12]").click()

# SECCION INFORMACION ACUDIENTE

time.sleep(.5)

namesCEmergency = driver.find_element(By.XPATH, "//input[contains(@id,'namesCEmergency')]")
namesCEmergency.send_keys("Test")

lastNameCEmergency = driver.find_element(By.XPATH, "//input[@id='EMERGENCY_CONTACT_lastNameCEmergency']")
lastNameCEmergency.send_keys("Test")

selectRelationshipCEmergency = driver.find_element(By.XPATH, "//select[@id='EMERGENCY_CONTACT_relationshipCEmergency']")
relationshipCEmergency = Select(selectRelationshipCEmergency)
relationshipCEmergency.select_by_value('0: Object')

selectDocumentCE = driver.find_element(By.XPATH, "//select[@id='EMERGENCY_CONTACT_documentCE']")
documentCE = Select(selectDocumentCE)
documentCE.select_by_value('0: Object')

documentDescCE = driver.find_element(By.XPATH, "//input[@id='EMERGENCY_CONTACT_documentDescCE']")
documentDescCE.send_keys("1234567890")

driver.find_element(By.XPATH, "//a[@id='EMERGENCY_CONTACT_phoneArea']").click()

driver.find_element(By.XPATH, "(//i[@class='flag-icon flag-icon-co'])[3]").click()

phoneCE = driver.find_element(By.XPATH, "//input[@id='EMERGENCY_CONTACT_phoneCe']")
phoneCE.send_keys("6017894561")

emailCEmergency = driver.find_element(By.XPATH, "//input[@id='EMERGENCY_CONTACT_emailCEmergency']")
emailCEmergency.send_keys("test@test.com")

selectCountryCEmergency = driver.find_element(By.XPATH, "//select[@id='EMERGENCY_CONTACT_countryCEmergency']")
countryCEmergency = Select(selectCountryCEmergency)
countryCEmergency.select_by_value('0: Object')

selectDepartmentCEmergency = driver.find_element(By.XPATH, "//select[contains(@id,'departmentCEmergency')]")
departmentCEmergency = Select(selectDepartmentCEmergency)
departmentCEmergency.select_by_value('59: Object')
time.sleep(.5)

selectCityCEmergency = driver.find_element(By.XPATH, "//select[@id='EMERGENCY_CONTACT_cityCEmergency']")
cityCEmergency = Select(selectCityCEmergency)
cityCEmergency.select_by_value('504: Object')

driver.find_element(By.XPATH, "(//button[@type='button'])[14]").click()

# SECCION FORMACION ACADEMICA

time.sleep(.5)

selectDegree = driver.find_element(By.XPATH, "//select[@id='ACADEMIC_DATA_degree']")
degree = Select(selectDegree)
degree.select_by_value('0: Object')

selectGraduatesURosario = driver.find_element(By.XPATH, "//select[@id='ACADEMIC_DATA_graduatesURosario']")
graduatesURosario = Select(selectGraduatesURosario)
graduatesURosario.select_by_value('0: Object')

paisUltimaFormacion = driver.find_element(By.XPATH, "//select[@id='ACADEMIC_DATA_countryLastEducation']")
paisUlFor = Select(paisUltimaFormacion)
paisUlFor.select_by_value('0: Object')

departamentoEgresado = driver.find_element(By.XPATH, "//select[@id='ACADEMIC_DATA_departmentUGraduate']")
depEgre = Select(departamentoEgresado)
depEgre.select_by_value('59: Object')

selectCoterminalOption = driver.find_element(By.XPATH, "//select[@id='ACADEMIC_DATA_coterminalOption']")
coterminalOption = Select(selectCoterminalOption)
coterminalOption.select_by_value('0: Object')

program = driver.find_element(By.XPATH, "//input[@id='ACADEMIC_DATA_program']")
program.send_keys("Programa Test")

SelectAreaKnowledge = driver.find_element(By.XPATH, "//select[@id='ACADEMIC_DATA_areaKnowledge']")
areaKnowledge = Select(SelectAreaKnowledge)
areaKnowledge.select_by_value('0: Object')

selectProfession = driver.find_element(By.XPATH, "//select[@id='ACADEMIC_DATA_profession']")
profession = Select(selectProfession)
profession.select_by_value('0: Object')

driver.find_element(By.XPATH, "(//button[@type='button'])[15]").click()
selectYear = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//select[@aria-label='Select year']")))
year = Select(selectYear)
year.select_by_value('2020')
selectMonth = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//select[@aria-label='Select month']")))
month = Select(selectMonth)
month.select_by_value('7')
day = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='btn-light ng-star-inserted'])[1]"))).click()

driver.find_element(By.XPATH, "(//button[@type='button'])[17]").click()

# SECCION EXPERIENCIA LABORAL

time.sleep(.5)

selectHasJob = driver.find_element(By.XPATH, "//select[@id='JOB_DATA_hasJob']")
hasJob = Select(selectHasJob)
hasJob.select_by_value('0: Object')

selectActivityJob = driver.find_element(By.XPATH, "//select[@id='JOB_DATA_activityJob']")
activityJob = Select(selectActivityJob)
activityJob.select_by_value('0: Object')

companyName = driver.find_element(By.XPATH, "//input[@id='JOB_DATA_name']")
companyName.send_keys("Empresa Test")

role = driver.find_element(By.XPATH, "//input[@id='JOB_DATA_role']")
role.send_keys("Cargo Test")

selectSizeCompany = driver.find_element(By.XPATH, "//select[@id='JOB_DATA_sizeCompany']")
sizeCompany = Select(selectSizeCompany)
sizeCompany.select_by_value('0: Object')

selectRoleDesc = driver.find_element(By.XPATH, "//select[@id='JOB_DATA_roleDesc']")
roleDesc = Select(selectRoleDesc)
roleDesc.select_by_value('0: Object')

driver.find_element(By.XPATH, "(//button[@type='button'])[19]").click()

driver.execute_script("window.scrollTo(0,300)")

# SECCION HABEAS DATA

time.sleep(.5)

driver.find_element(By.XPATH, "//label[contains(@for,'acceptTerms0')]").click()

driver.find_element(By.XPATH, "//label[contains(@for,'acceptTerms1')]").click()

driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Guardar Solicitud')]").click()

confirmData = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, "(//button[contains(.,'Aceptar')])[2]"))).click()

time.sleep(.5)

saveData = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, "(//button[contains(@type,'button')])[23]"))).click()

time.sleep(2)
