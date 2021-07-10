import sys
from selenium import webdriver
from time import sleep


def setup():
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

    return driver


def scrape_table(content):
    header = content.find_element_by_tag_name("thead")
    header_elements = header.find_elements_by_tag_name("th")
    for el in header_elements:
        el_text = str(el.text).strip()
        if el_text != "":
            print(el_text)

        table_body = content.find_element_by_tag_name("tbody")
        table_rows = table_body.find_elements_by_tag_name("tr")

        for row in table_rows:
            row_content = row.find_elements_by_tag_name("td")
            for i in range(len(row_content)):
                print(row_content[i].text)
            print("\n")


def main():
    driver = setup()
    company_code_list = ['4220', '1180']

    for comany in company_code_list:
        driver.get(
            f'https://www.saudiexchange.sa/wps/portal/tadawul/market-participants/issuers/issuers-directory/company-details/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zi_Tx8nD0MLIy83V1DjA0czVx8nYP8PI0MDAz0I4EKzBEKDEJDLYEKjJ0DA11MjQzcTfXDCSkoyE7zBAC-SKhH/?companySymbol={comany}#chart_tab3')

        sleep(1)

        content = driver.find_element_by_id("chart_sub_tab1")

        tabs = content.find_elements_by_tag_name("li")
        table_count = 0

        for tab in tabs[1:4]:
            # 0 - BALANCE SHEET
            # 1 - STATEMENT OF INCOME
            # 2 - CASH FLOW
            # 3 - XBRL
            # 4 - DETAILED REPORTS AND STATEMENTS
            # 5 - ANNUALLY
            # 6 - QUARTERLY

            scrape_table(content)

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
            scrape_table(quaterly_table)

            try:
                link = tab.find_elements_by_tag_name("span")[0]
                print(link.text)
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
            table_count += 1


if __name__ == '__main__':
    main()
