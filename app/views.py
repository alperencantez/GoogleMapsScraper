import time
from flask import jsonify, request, render_template, flash
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

from config import *


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        with sync_playwright() as p:
            keyword = request.form.get("keyword")
            city = request.form.get("city")
            district = request.form.get("district")
            result_qtn = int(request.form.get("qtn"))

            if keyword == "" or city == "" or district == "":
                flash("gerekli kısımlardan birisi doldurulmamış sanki...")
                return render_template("index.html")

            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.google.com/maps")

            # Put user-provided keywords and trigger search button
            page.locator("id=searchboxinput").fill(
                f"{keyword} nearby {district}/{city}")
            page.locator("id=searchbox-searchbutton").click()

            # Wait for the left side panel and pick all of the matching results as DOM elements
            page.wait_for_selector(
                'div[jsan="t-dgE5uNmzjiE,7.m6QErb,7.WNBkOb,0.role"]')

            businesses = page.query_selector_all('a[class="hfpxzc"]')
            businesses[0].click()

            while len(businesses) <= result_qtn:
                page.keyboard.press("End")
                page.wait_for_selector('div[class="qjESne veYFef"]')

                if len(businesses) == result_qtn:
                    break

                if len(businesses) >= 20 and result_qtn > 20:
                    page.keyboard.press("ArrowUp")
                    page.keyboard.press("ArrowUp")
                    page.keyboard.press("ArrowUp")
                    time.sleep(4)

                    businesses[-1].click()
                    page.keyboard.press("End")

                businesses = page.query_selector_all('a[class="hfpxzc"]')

            businesses = page.query_selector_all('a[class="hfpxzc"]')

            # The JSON file that'll be storing all of scraped data
            data = []

            for i in range(0, len(businesses)):
                businesses[i].click()

                page.wait_for_selector('div[class="bJzME Hu9e2e tTVLSc"]')
                html_of_all = page.query_selector(
                    'div[class="bJzME Hu9e2e tTVLSc"]')

                html_raw = html_of_all.inner_html()

                html_business = BeautifulSoup(html_raw, "html.parser")
                time.sleep(2)
                name = html_business.select_one(
                    'div[class="TIHn2"]').div.div.div.h1.span.string

                all = html_business.select(
                    'div[class="Io6YTe fontBodyMedium"]')
                mylist = []

                for k in all:
                    mylist.append(k.string)

                for names in data:
                    try:
                        if names["name"] == name:
                            data.remove(names)
                    except KeyError as e:
                        print(e)
                        pass

                for business in data:
                    for detail in business["details"]:
                        if detail is None:
                            pass
                        elif detail == "Bu işletmeyi sahiplenin" or detail == "Sahibi kadın olduğunu belirtiyor" or detail == "Telefonunuza gönderin":
                            if type(business["details"]) != str:
                                business["details"].remove(detail)
                        elif detail[0:2] == "05" or detail[0:2] == "(0" or detail[0:2] == "08":
                            business["phone"] = detail
                            if type(business["details"]) != str:
                                business["details"].remove(detail)

                data.append({
                    "name": name,
                    "address": mylist[0],
                    "details": mylist[1:]
                })

            return jsonify(data)
    else:
        return render_template("index.html")
