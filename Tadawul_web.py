import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pymongo

# All values most be multiplied by 1,000


def setup():
    client = pymongo.MongoClient(
        "mongodb+srv://Mezo:Almazni2013@tadawul-test.wkg8i.mongodb.net/Tadawul?retryWrites=true&w=majority")
    mydb = client["Tadawul_v2"]

    options = webdriver.ChromeOptions()
    options.add_argument('--disable-backgrounding-occluded-windows')
    options.add_argument("start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/59.0.3071.115 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(executable_path=r"./chromedriver")

    return driver, mydb


def scrape_table(content):
    header = content.find_element_by_tag_name("thead")
    header_elements = header.find_elements_by_tag_name("th")
    years = []
    res = {}
    for i in range(len(header_elements)):
        el_text = str(header_elements[i].text).strip()
        if el_text != "":
            if i > 0:
                years.append(el_text)
                res["{}".format(el_text)] = {}

    table_body = content.find_element_by_tag_name("tbody")
    table_rows = table_body.find_elements_by_tag_name("tr")

    for row in table_rows:
        row_content = row.find_elements_by_tag_name("td")
        for i in range(len(row_content)):
            current_res = {}
            if i > 0:
                if len(str(row_content[i].text).strip()) > 1:
                    value_text = str(row_content[i].text).replace(",", "")
                    if str(value_text).isnumeric():
                        value_text = float(value_text)*1000
                else:
                    value_text = str(row_content[i].text).replace("-", "0")
                tab_text = str(row_content[0].text).strip().replace(".", "")
                current_res["{}".format(tab_text)] = value_text
                if i < 5:
                    res[years[i-1]]["{}".format(tab_text)] = value_text
    return res


def main():
    driver, mydb = setup()
    company_code_list = ['2270', '8280', '8100',
                         '2200', '4020', '2230', '4260', '4003', '8190', '2330', '4030', '2220', '2002', '8300', '4291', '4160', '6010', '4005',
                         '4210', '2250', '8150', '1140', '1020', '1010', '1330', '3091', '3040', '3003', '3050', '3080', '3004', '3020', '3005',
                         '3090', '3001', '3002', '3060', '4001', '8250', '8040', '8310', '1182', '2160', '2140', '7020', '8120', '7040', '1301',
                         '3030', '3010', '4320', '8130', '7010', '7030', '8312', '8170', '2320', '4130', '4230', '8160', '2060', '1211', '2090',
                         '8012', '6070', '1214', '4007', '2040', '6004', '4290', '8070', '4200', '8230', '4150', '2240', '2222', '1202',
                         '4009', '2370', '6060', '2310', '8180', '2150', '1303', '1210', '2340', '4141', '2080', '6020', '2110', '3008', '2170',
                         '8030', '2280', '4321', '4170', '2030', '7200', '4280', '4002', '1304', '4110', '4051', '7201', '8270', '4161', '1302',
                         '8210', '6040', '2180', '1201', '4070', '8240', '4012', '6090', '4250', '4190', '6001', '4300', '4004', '4010', '4261',
                         '2380', '6012', '3007', '8080', '2020', '8050', '1832', '4090', '4191', '4080', '4292', '8311', '4240', '2350', '2001',
                         '4011', '1830', '4100', '8020', '1831', '1213', '2210', '6002', '2100', '8060', '2290', '4338', '4331', '4348', '4340',
                         '4330', '4337', '4334', '4347', '4333', '4332', '4342', '4339', '4344', '4345', '4335', '4336', '4346', '1212', '4061',
                         '4013', '1810', '2050', '1820', '4180', '4310', '1150', '1120']

    for comany in company_code_list:
        current_company = {}
        current_company["_id"] = comany
        driver.get(
            f'https://www.saudiexchange.sa/wps/portal/tadawul/market-participants/issuers/issuers-directory/company-details/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zi_Tx8nD0MLIy83V1DjA0czVx8nYP8PI0MDAz0I4EKzBEKDEJDLYEKjJ0DA11MjQzcTfXDCSkoyE7zBAC-SKhH/?companySymbol={comany}#chart_tab1')

        sleep(1.5)

        home_button = driver.find_element_by_id("logo")
        driver.execute_script(
            "return arguments[0].scrollIntoView(true);", home_button)
        sleep(1.5)

        comany_name_component = driver.find_element_by_class_name("clear_lft")
        comany_name_text = str(comany_name_component.text).split('\n')
        comany_name = comany_name_text[0].strip()
        comany_sector = comany_name_text[2].split("|")[0].split(":")[1].strip()
        price_table = driver.find_element_by_id("chart_tab1")
        comany_price_component = price_table.find_element_by_tag_name("dd")
        comany_price = comany_price_component.text

        mycol = mydb["{}".format(comany_sector)]

        current_company["NAME"] = comany_name
        current_company["PRICE"] = comany_price
        current_company["SECTOR"] = comany_sector

        # WebDriverWait(driver, 200).until(
        #     EC.presence_of_element_located((By.ID, "profileTab")))

        profile_component = driver.find_element_by_id("profileTab")
        profile_component.click()
        sleep(1.5)

        # chart_tab5
        WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.ID, "chart_tab5")))

        equity_component = driver.find_element_by_id("chart_tab5")
        header = equity_component.find_element_by_tag_name("thead")
        header_elements = header.find_elements_by_tag_name("th")

        equity_statements = []
        for el in header_elements:
            el_text = str(el.text).strip()
            equity_statements.append(el_text)
            current_company["{}".format(el_text)] = {}

        table_body = equity_component.find_element_by_tag_name("tbody")
        table_rows = table_body.find_elements_by_tag_name("tr")
        rows_content = str(table_rows[0].text).split(" ")

        for i in range(len(equity_statements)):
            current_company[equity_statements[i]] = str(
                rows_content[i]).replace(",", "")

        home_button = driver.find_element_by_id("logo")
        driver.execute_script(
            "return arguments[0].scrollIntoView(true);", home_button)
        sleep(1.5)

        statements_component = driver.find_element_by_id("statementsTab")
        statements_component.click()
        sleep(1.5)

        WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.ID, "chart_sub_tab1")))
        content = driver.find_element_by_id("chart_sub_tab1")

        tabs = content.find_elements_by_tag_name("li")
        table_count = 0

        for tab in tabs[0:3]:
            # 0 - BALANCE SHEET
            # 1 - STATEMENT OF INCOME
            # 2 - CASH FLOW
            # 3 - XBRL
            # 4 - DETAILED REPORTS AND STATEMENTS
            # 5 - ANNUALLY
            # 6 - QUARTERLY

            try:
                link = tab.find_elements_by_tag_name("span")[0]
                home_button = driver.find_element_by_id("logo")
                driver.execute_script(
                    "return arguments[0].scrollIntoView(true);", home_button)
                sleep(1.5)
                driver.execute_script(
                    "return arguments[0].scrollIntoView(true);", link)
                sleep(1.5)
                if str(tab.text) == "XBRL":
                    break
                link.click()
                sleep(1)
            except:
                print(sys.exc_info()[0])
                print("Error when clicking next tab")
                driver.quit()
                exit(0)

            current_company["{}".format(tab.text)] = {}

            current_company["{}".format(tab.text)]["ANNUALLY"] = scrape_table(
                content)

            try:
                QUARTERLY = content.find_element_by_xpath(
                    "//span[contains(text(), 'Quarterly')]")
                driver.execute_script(
                    "return arguments[0].scrollIntoView(true);", QUARTERLY)
                sleep(1.5)
                QUARTERLY.click()
            except:
                print(sys.exc_info()[0])
                print("Error when clicking Quarterly")
                driver.quit()
                exit(0)

            quaterly_table = content.find_element_by_id(
                f"quaterlyStmtTable{table_count}")

            current_company["{}".format(tab.text)]["QUARTERLY"] = scrape_table(
                quaterly_table)
            table_count += 1
        mycol.insert_one(current_company)


if __name__ == '__main__':
    main()
