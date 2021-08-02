from django.urls import path
from . import views
from .views import *
urlpatterns= [
    path('', views.main),
    path('filter/<str:filterVal>/catagory/<str:catVal>', views.filterView),
    path('search/ticker', views.searchT),
    # path('new/sector/<str:sectorVal>/average', views.newDividendAvrgForSector),
    path('stock/sector/<str:sectorVal>/ticker/<str:tickerVal>/page', views.stockPage),
    path('others/MarketCap/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_market_cap),
    path('others/EPS/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_EPS),
    path('others/Operating_EPS/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Operating_EPS),
    path('others/EBIT/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_EBIT),
    path('others/EBITDA/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_EBITDA),
    path('others/Non_Current_Assets/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Non_Current_Assets),
    path('others/Current_Assets/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Current_Assets),
    path('others/Total_Liabilities/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Total_Liabilities),
    path('others/Cash_Change/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Cash_Change),
    path('others/Book_Value/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Book_Value),
    path('others/Dividends_Per_Share/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Dividends_Per_Share),
    path('others/PE/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_PE),
    path('others/Operating_Profit_Multiple/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Operating_Profit_Multiple),
    path('others/PB/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_PB),
    path('others/PS/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_PS),
    path('others/Current_Ratio/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Current_Ratio),
    path('others/Dividend_Yield/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Dividend_Yield),
    path('others/Payout_Ratio/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Payout_Ratio),
    path('others/Operating_Profit_Margin/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Operating_Profit_Margin),
    path('others/Net_Margin/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Net_Margin),
    path('others/Equity_to_Capital/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Equity_to_Capital),
    path('others/Debt_Ratio/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Debt_Ratio),
    path('others/Debt_to_Equity/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Debt_to_Equity),
    path('others/Quick_Ratio/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Quick_Ratio),
    path('others/Cash_Ratio/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Cash_Ratio),
    path('others/ROA/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_ROA),
    path('others/ROTA/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_ROTA),
    path('others/ROE/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_ROE),
    path('others/Asset_Turnover_Ratio/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Asset_Turnover_Ratio),
    path('others/Net_Fixed_Asset_Turnover_Ratio/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Net_Fixed_Asset_Turnover_Ratio),
    path('others/Equity_Turnover_Ratio/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Equity_Turnover_Ratio),
    path('others/Receivables_Turnover_Ratio/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Receivables_Turnover_Ratio),
    path('others/Payable_Turnover_Ratio/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Payable_Turnover_Ratio),
    path('others/Inventory_Turnover_Ratio/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Inventory_Turnover_Ratio),
    path('others/Days_Inventory_Outstanding/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Days_Inventory_Outstanding),
    path('others/Days_Sales_Outstanding/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Days_Sales_Outstanding),
    path('others/Days_Payable_Outstanding/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Days_Payable_Outstanding),
    path('others/Operating_Cycle/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Operating_Cycle),
    path('others/Cash_Conversion_Cycle/sector/<str:sectorVal>/ticker/<str:tickerVal>', views.get_Cash_Conversion_Cycle),
]