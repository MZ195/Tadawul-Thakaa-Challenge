import sys
from selenium import webdriver
from time import sleep
import pymongo


def setup():
    client = pymongo.MongoClient(
        "mongodb+srv://Mezo:Almazni2013@tadawul-test.wkg8i.mongodb.net/Tadawul?retryWrites=true&w=majority")
    mydb = client["Tadawul"]

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
                res["{}".format(el_text)] = []

    table_body = content.find_element_by_tag_name("tbody")
    table_rows = table_body.find_elements_by_tag_name("tr")

    for row in table_rows:
        row_content = row.find_elements_by_tag_name("td")
        for i in range(len(row_content)):
            current_res = {}
            if i > 0:
                if len(str(row_content[i].text).strip()) > 1:
                    value_text = str(row_content[i].text).replace(",", "")
                else:
                    value_text = str(row_content[i].text).replace("-", "0")
                tab_text = str(row_content[0].text).strip().replace(".", "")
                current_res["{}".format(tab_text)] = value_text
                res[years[i-1]].append(current_res)
    return res


def main():
    driver, mydb = setup()
    company_code_list = ['2222', '4220']

    for comany in company_code_list:
        mycol = mydb["{}".format(comany)]
        current_company = {}
        current_company["{}".format(comany)] = {}
        driver.get(
            f'https://www.saudiexchange.sa/wps/portal/tadawul/market-participants/issuers/issuers-directory/company-details/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zi_Tx8nD0MLIy83V1DjA0czVx8nYP8PI0MDAz0I4EKzBEKDEJDLYEKjJ0DA11MjQzcTfXDCSkoyE7zBAC-SKhH/?companySymbol={comany}')

        sleep(1)

        comany_name_component = driver.find_element_by_class_name("clear_lft")
        comany_name_text = str(comany_name_component.text).split('\n')
        comany_name = comany_name_text[0].strip()
        comany_sector = comany_name_text[2].split("|")[0].split(":")[1].strip()
        price_table = driver.find_element_by_id("chart_tab1")
        comany_price_component = price_table.find_element_by_tag_name("dd")
        comany_price = comany_price_component.text

        current_company[comany]["NAME"] = comany_name
        current_company[comany]["PRICE"] = comany_price
        current_company[comany]["SECTOR"] = comany_sector

        profile_component = driver.find_element_by_id("profileTab")
        profile_component.click()
        sleep(1)

        equity_component = driver.find_element_by_id("chart_tab5")
        header = equity_component.find_element_by_tag_name("thead")
        header_elements = header.find_elements_by_tag_name("th")

        equity_statements = []
        for el in header_elements:
            el_text = str(el.text).strip()
            equity_statements.append(el_text)
            current_company[comany]["{}".format(el_text)] = {}

        table_body = equity_component.find_element_by_tag_name("tbody")
        table_rows = table_body.find_elements_by_tag_name("tr")
        rows_content = str(table_rows[0].text).split(" ")

        for i in range(len(equity_statements)):
            current_company[comany][equity_statements[i]] = rows_content[i]

        home_button = driver.find_element_by_id("logo")
        driver.execute_script(
            "return arguments[0].scrollIntoView(true);", home_button)
        sleep(1.5)

        statements_component = driver.find_element_by_id("statementsTab")
        statements_component.click()
        sleep(1)

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

            current_company[comany]["{}".format(tab.text)] = {}

            current_company[comany]["{}".format(tab.text)]["ANNUALLY"] = scrape_table(
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

            current_company[comany]["{}".format(tab.text)]["QUARTERLY"] = scrape_table(
                quaterly_table)
            table_count += 1
        mycol.insert_one(current_company)


if __name__ == '__main__':
    main()
