from time import sleep
import psycopg2
import requests
from API_ENDPOINTS import API_END_POINTS


# finished_list = [4220, 1320, 2360, 4050, 2300, 6050, 4006, 2130, 4031, 2190, 4140, 2010,
#                  4270, 2070, 4003, 4008, 5110, 4040, 2270, 2200, 4020, 2230, 4260, 4090,
#                  4160, 2330, 4030, 2220, 2002, 4291, 6010, 4005, 4210, 2250, 1330, 3091,
#                  3040, 3003, 3050, 3080, 3004, 3020, 3005, 3090, 3001, 3002, 3060, 4001,
#                  2160, 2140, 7020, 7040, 1301, 3030, 3010, 4320, 7010, 7030, 2320, 4230,
#                  2060, 1211, 2090, 6070, 1214, 4007, 2081, 2040, 6004, 4290, 4200, 4150,
#                  2240, 2222, 1202, 4009, 2370, 6060, 2310, 2150, 1303, 1210, 2340, 4141,
#                  2080, 6020, 2110, 3008, 2170, 2280, 4321, 4170, 2030, 7200, 4002, 1304,
#                  4110, 4051, 7201, 4161, 1302, 6040, 2180, 1201, 4070, 4012, 6090, 4250,
#                  4190, 6001, 4300, 4004, 4010, 4261, 2380, 6012, 3007, 2020, 1832, 4091,
#                  4292, 4240, 2350, 2001, 4011, 1830, 4100, 1831, 1213, 2210, 6002, 2100,
#                  2290, 1212, 4061, 4013, 1810, 2050, 1820, 1480, 4310]


def setup():
    # Create database connection  postgres://ytvwlxfp:DQWgHzUZE_ormYbJ1UHzBJ_yatJCcss6@chunee.db.elephantsql.com/ytvwlxfp
    postgresSQL = psycopg2.connect(database="ytvwlxfp",
                                   user="ytvwlxfp",
                                   password="DQWgHzUZE_ormYbJ1UHzBJ_yatJCcss6",
                                   host="chunee.db.elephantsql.com",
                                   port="5432")

    return postgresSQL


def main():
    conn = setup()
    cur = conn.cursor()
    cur.execute(
        '''SELECT TICKER, NAME, SECTOR FROM "public"."companies_general"''')
    rows = cur.fetchall()
    conn.commit()

    for (ticker, name, sector) in rows:
        # if "Financials" in sector or int(ticker) in finished_list:
        #     continue
        # else:
        print(f"Start working with {name}, {ticker}")
        for api_endpoint in API_END_POINTS:
            url = api_endpoint + f"?sector={sector}&ticker={ticker}"
            api_res = requests.get(url=url).json()
            api_res_keys = list(api_res.keys())
            table_name = api_endpoint.split('/')[4]

            cur = conn.cursor()

            if len(api_res_keys) == 1:
                cur.execute(f'''
                CREATE TABLE IF NOT EXISTS {table_name} (
                  TICKER INT PRIMARY KEY,
                  {api_res_keys[0]} FLOAT
                  )
                  ''')
                cur.execute(
                    f"INSERT INTO {table_name} (TICKER,{api_res_keys[0]}) VALUES ({ticker},{api_res[api_res_keys[0]]})")
            else:
                api_res_annually = api_res["ANNUALLY"]
                for year_res in api_res_annually:
                    api_res_keys = list(year_res.keys())
                    cur.execute(f'''
                    CREATE TABLE IF NOT EXISTS {table_name} (
                      ID SERIAL,
                      TICKER INT,
                      YEAR TEXT,
                      VALUE FLOAT
                      )
                      ''')
                    cur.execute(
                        f"INSERT INTO {table_name} (TICKER,YEAR,VALUE) VALUES ({ticker},'{api_res_keys[0]}',{year_res[api_res_keys[0]]})")
            conn.commit()
            sleep(0.5)
        print(f"Done with {name}, {ticker}")
        sleep(1)


if __name__ == "__main__":
    main()
