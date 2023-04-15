import requests
from bs4 import BeautifulSoup
import streamlit as st
import matplotlib
import pandas as pd


# set streamlit config to wide mode
st.set_page_config(layout="wide")

st.title("Sector Fundamentals App")
st.text("Select a sector to scrape data from FinViz and display in a heatmapped table.")

# fmt: off
telecom_services = ["VZ", "T", "TMUS", "LUMN"]
industrials_specialty_machinery = ["HON", "MMM", "GE", "ITW", "ROP", "EMR", "ETN", "CMI", "PNR", "ROK", "PH", "TT", "AME", "DOV", "IR", "XYL", "IEX", "AOS", "HWM"]
healthcare_medical_devices = ["ABT", "MDT", "SYK", "BSX", "EW", "ZBH", "ALGN"]
healthcare_drug_manufacturers_general = ["JNJ", "PFE", "MRK", "LLY", "AMGN", "BMY", "GILD", "ABBV", "BIIB"]
apd_linde = ["APD", "LIN"]
materials_specialty_chemicals = ["LIN", "ECL", "PPG", "SHW", "LYB", "IFF", "ALB"]
consumer_cyclical_packaging_and_containers = ["AMCR", "PKG", "WRK", "IP", "SEE"]
consumer_defensive_farm_products = ["ADM", "TSN"]
healthcare_medical_instruments_and_supplies = ["BAX", "ISRG", "TFX", "COO", "HOLX", "RMD", "STE", "XRAY", "WST"]
consumer_defensive_beverages_wineries_and_distilleries = ["BF-B", "STZ"]
energy_oil_and_gas_integrated = ["CVX", "XOM", "BP"]
consumer_defensive_beverages_nonalcoholic = ["KO", "PEP", "MNST"]
consumer_defensive_household_and_personal_products = ["CLX", "PG", "EL", "KMB", "CL", "CHD", "NWL", "COTY"]
industrials_integrated_freight_and_logistics = ["UPS", "FDX", "EXPD", "JBHT", "CHRW"]
reit_retail = ["FRT", "SPG", "O", "KIM", "REG"]
industrials_aerospace_and_defense = ["LMT", "RTX", "BA", "LHX", "GD", "TDG", "NOC", "HII", "TXT"]
consumer_cyclical_specialty_retail = ["GPC", "ORLY", "AZO", "BBY", "TSCO", "ULTA", "AAP"]
consumer_defensive_packaged_foods = ["HRL", "KHC", "GIS", "MKC", "K", "CAG", "SJM", "LW", "CPB"]
technology_information_technology_services = ["ACN", "IBM", "FIS", "FISV", "CTSH", "FLT", "CDW", "LDOS", "BR", "JKHY"]
consumer_cyclical_furnishings_fixtures_and_appliances = ["LEG", "WHR", "FBHS", "MHK"]
consumer_cyclical_home_improvement_retail = ["LOW", "HD"]
consumer_cyclical_restaurants = ["MCD", "SBUX", "YUM", "DRI", "CMG", "WEN", "QSR"]
financials_banks_regional = ["USB", "TFC", "PNC", "FRC", "FITB", "MTB", "SIVB", "KEY", "CFG", "HBAN", "CMA", "ZION", "PBCT"]
financial_financial_data_and_stock_exhanges = ["SPGI", "CME", "ICE", "MCO", "MSCI", "NDAQ", "CBOE"]
industrials_tools_accessories = ["SWK", "SNA"]
consumer_defensive_food_distribution = ["SYY", "USFD", "PFGC"]
consumer_defensive_discount_stores = ["TGT", "WMT", "COST", "DG", "DLTR"]
consumer_cyclical_apparel_manufacturing = ["VFC", "RL", "UAA", "PVH", "HBI", "CPRI"]
healthcare_pharmaceutical_retailers = ["WBA", "CVX", "RAD"]
semiconductors = ["NVDA", "AVGO", "QCOM", "INTC", "TXN", "MU", "ADI", "AMD", "XLNX", "MCHP", "SWKS", "QRVO"]
cyber_security = ["AKAM", "FFIV", "FTNT", "NLOK", "CRWD", "PANW", "FEYE", "ZS"]
gold_miners = ["NEM", "GOLD", "AEM", "KL", "AU", "KGC"]
entertainment = ["DIS", "CMCSA", "NFLX", "CHTR", "VIAC", "DISH", "LYV", "DISCA"]
grocery_stores = ["KR", "ACI", "CASY", "GO", "SFM"]
technology_software_infrastructure = ["MSFT", "ADBE", "ORCL", "SNPS"]
technology_software_application = ["CRM", "INTU", "NOW", "ADSK", "ANSS", "PAYC", "TYL", "CTXS", "PTC", "CDNS",]
technology_information_technology_services = ["ACN", "IBM", "FIS", "FISV", "CTSH", "IT", "CDW", "BR", "LDOS"]
technology_communication_equipment = ["CSCO", "ZBRA", "MSI", "HPE", "JNPR"]
technology_semiconductor_equipment = ["AMAT", "LRCX", "KLAC", "TER", "IPGP"]
technology_scientific_instruments = ["GRMN", "KEYS", "FTV", "TRMB", "TDY"]
technology_computer_hardware = ["HPQ", "ANET", "STX", "WDC", "NTAP"]
technology_electronic_components = ["TEL", "APH", "GLW"]
healthcare_biotech = ["MRNA", "REGN", "VRTX", "INCY"]
healthcare_plans = ["UNH", "CVS", "ANTM", "CI", "HUM", "CNC"]
# fmt: on

sector_dict = {
    "Telecom Services": telecom_services,
    "Industrials - Specialty Machinery": industrials_specialty_machinery,
    "Healthcare - Medical Devices": healthcare_medical_devices,
    "Healthcare - Drug Manufacturers General": healthcare_drug_manufacturers_general,
    "Materials - Specialty Chemicals": materials_specialty_chemicals,
    "Consumer Cyclical - Packaging & Containers": consumer_cyclical_packaging_and_containers,
    "Consumer Defensive - Farm Products": consumer_defensive_farm_products,
    "Healthcare - Medical Instruments & Supplies": healthcare_medical_instruments_and_supplies,
    "Consumer Defensive - Beverages, Wineries, Distilleries": consumer_defensive_beverages_wineries_and_distilleries,
    "Energy - Oil & Gas Integrated": energy_oil_and_gas_integrated,
    "Consumer Defensive - Beverages Non-Alcoholic": consumer_defensive_beverages_nonalcoholic,
    "Consumer Defensive - Household Products": consumer_defensive_household_and_personal_products,
    "Industrials - Integrated Freight & Logistics": industrials_integrated_freight_and_logistics,
    "Consumer Defensive - Packaged Foods": consumer_defensive_packaged_foods,
    "Industrials - Tools & Accessories": industrials_tools_accessories,
    "Consumer Defensive - Food Distribution": consumer_defensive_food_distribution,
    "Consumer Defensive - Discount Stores": consumer_defensive_discount_stores,
    "Technology - Information Technology Services": technology_information_technology_services,
    "Technology - Communication Equipment": technology_communication_equipment,
    "Technology - Semiconductor Equipment": technology_semiconductor_equipment,
    "Technology - Scientific Instruments": technology_scientific_instruments,
    "Technology - Electronic Components": technology_electronic_components,
    "Healthcare - Biotech": healthcare_biotech,
}

sector_select = st.selectbox("Select a sector", list(sector_dict.keys()))
sector = sector_dict[sector_select]


def sector_fundamentals(sector):
    current_ratio_list = []
    quick_ratio_list = []
    cash_per_share_list = []
    debt_to_eq_list = []
    LTdebt_to_eq_list = []
    roa_list = []
    roi_list = []
    gross_margin_list = []
    operating_margin_list = []
    profit_margin_list = []
    five_year_sales_list = []
    five_earnings_list = []
    index_list = [
        " ",
        "Current Ratio",
        "Quick Ratio",
        "Cash per Share",
        "Debt to Equity",
        "LT Debt to Equity",
        "ROA",
        "ROI",
        "Gross Margin",
        "Oper. Margin",
        "Profit Margin",
        "5y EPS Growth",
        "5y Sales Growth",
    ]
    final_list = [
        sector,
        current_ratio_list,
        quick_ratio_list,
        cash_per_share_list,
        debt_to_eq_list,
        LTdebt_to_eq_list,
        roa_list,
        roi_list,
        gross_margin_list,
        operating_margin_list,
        profit_margin_list,
        five_earnings_list,
        five_year_sales_list,
    ]

    for each_aristocrat in sector:
        url = "https://finviz.com/quote.ashx?t={}".format(each_aristocrat)
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "lxml")

        current_ratio = soup.find("td", string="Current Ratio").find_next("td").text
        if current_ratio != "-":
            current_ratio_list.append(float(current_ratio))
        else:
            current_ratio_list.append(current_ratio)

        quick_ratio = soup.find("td", string="Quick Ratio").find_next("td").text
        if quick_ratio != "-":
            quick_ratio_list.append(float(quick_ratio))
        else:
            quick_ratio_list.append(quick_ratio)

        cash_per_share = soup.find("td", string="Cash/sh").find_next("td").text
        if cash_per_share != "-":
            cash_per_share_list.append(float(cash_per_share))
        else:
            cash_per_share_list.append(cash_per_share)

        debt_to_eq = soup.find("td", string="Debt/Eq").find_next("td").text
        if debt_to_eq != "-":
            debt_to_eq_list.append(float(debt_to_eq))
        else:
            debt_to_eq_list.append(debt_to_eq)

        LTdebt_to_eq = soup.find("td", string="LT Debt/Eq").find_next("td").text
        if LTdebt_to_eq != "-":
            LTdebt_to_eq_list.append(float(LTdebt_to_eq))
        else:
            LTdebt_to_eq_list.append(LTdebt_to_eq)

        roa = soup.find("td", string="ROA").find_next("td").text.strip("%")
        if roa != "-":
            roa_list.append(float(roa))
        else:
            roa_list.append(roa)

        roi = soup.find("td", string="ROI").find_next("td").text.strip("%")
        if roi != "-":
            roi_list.append(float(roi))
        else:
            roi_list.append(roi)

        gross_margin = (
            soup.find("td", string="Gross Margin").find_next("td").text.strip("%")
        )
        if gross_margin != "-":
            gross_margin_list.append(float(gross_margin))
        else:
            gross_margin_list.append(gross_margin)

        op_margin = (
            soup.find("td", string="Oper. Margin").find_next("td").text.strip("%")
        )
        if op_margin != "-":
            operating_margin_list.append(float(op_margin))
        else:
            operating_margin_list.append(op_margin)

        profit_margin = (
            soup.find("td", string="Profit Margin").find_next("td").text.strip("%")
        )
        if profit_margin != "-":
            profit_margin_list.append(float(profit_margin))
        else:
            profit_margin_list.append(profit_margin)

        five_year_sales = (
            soup.find("td", string="Sales past 5Y").find_next("td").text.strip("%")
        )
        if five_year_sales != "-":
            five_year_sales_list.append(float(five_year_sales))
        else:
            five_year_sales_list.append(five_year_sales)

        five_earnings = (
            soup.find("td", string="EPS past 5Y").find_next("td").text.strip("%")
        )
        if five_earnings != "-":
            five_earnings_list.append(float(five_earnings))
        else:
            five_earnings_list.append(five_earnings)

    df = pd.DataFrame(final_list)
    df[" "] = index_list

    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    df.set_index(" ", inplace=True, drop=True)
    df.reset_index()

    return df


df = sector_fundamentals(sector)

data = (
    df.style.background_gradient(
        axis=1, cmap="RdYlGn", subset=(df.index[0], df.columns)
    )
    .background_gradient(axis=1, cmap="RdYlGn", subset=(df.index[1], df.columns))
    .background_gradient(axis=1, cmap="RdYlGn", subset=(df.index[2], df.columns))
    .background_gradient(axis=1, cmap="RdYlGn_r", subset=(df.index[3], df.columns))
    .background_gradient(axis=1, cmap="RdYlGn_r", subset=(df.index[4], df.columns))
    .background_gradient(axis=1, cmap="RdYlGn", subset=(df.index[5], df.columns))
    .background_gradient(axis=1, cmap="RdYlGn", subset=(df.index[6], df.columns))
    .background_gradient(axis=1, cmap="RdYlGn", subset=(df.index[7], df.columns))
    .background_gradient(axis=1, cmap="RdYlGn", subset=(df.index[8], df.columns))
    .background_gradient(axis=1, cmap="RdYlGn", subset=(df.index[9], df.columns))
    .background_gradient(axis=1, cmap="RdYlGn", subset=(df.index[10], df.columns))
    .background_gradient(axis=1, cmap="RdYlGn", subset=(df.index[11], df.columns))
    .set_precision(2)
)


st.write(data)
