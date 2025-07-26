import requests
from bs4 import BeautifulSoup
import pandas as pd
import html
import re

# Text Cleaner Function
def clean_text(text):
    if not text:
        return "N/A"
    text = html.unescape(text)  # Convert HTML entities
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Remove emojis and non-ASCII
    text = ' '.join(text.split())  # Remove extra spaces and newlines
    return text.strip()

# Scraper Function
def get_remote_jobs():
    url = "https://remoteok.com/remote-python-jobs"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(" Failed to fetch data. Status code:", response.status_code)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    for tr in soup.find_all("tr", class_="job"):
        try:
            title = clean_text(tr.find("h2").text)
            company = clean_text(tr.find("h3").text)
            link = "https://remoteok.com" + tr.get("data-href", "")

            #  Requirement / Short Description
            desc_tag = tr.find("td", class_="company_and_position")
            requirement = clean_text(desc_tag.text if desc_tag else "")

            #  Location + Salary (in div or span)
            loc_salary_tag = tr.find("div", class_="location")
            loc_salary = clean_text(loc_salary_tag.text if loc_salary_tag else "")
            
            # Split location & salary if possible
            if "$" in loc_salary:
                location, salary = loc_salary.split("$", 1)
                location = location.strip()
                salary = "$" + salary.strip()
            else:
                location = loc_salary
                salary = "N/A"

            jobs.append({
                "Title": title,
                "Company": company,
                "Location": location if location else "Worldwide",
                "Salary": salary,
                "Requirement": requirement,
                "Link": link
            })

        except Exception as e:
            print(" Error parsing a job:", e)
            continue

    if jobs:
        df = pd.DataFrame(jobs)
        df.to_csv("remote_jobs.csv", index=False)
        print(" Job data saved to 'remote_jobs.csv'")
    else:
        print(" No jobs found.")

# Run
get_remote_jobs()
