import requests
from bs4 import BeautifulSoup
import pandas as pd
import html
import re
import os
import sys
import logging

# ----------------------------------------------------
# Configure logging to display clean messages in console
# ----------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

# ----------------------------------------------------
# Function to clean text (removes HTML entities, emojis, extra whitespace)
# ----------------------------------------------------
def clean_text(text):
    if not text:
        return "N/A"
    text = html.unescape(text)  # Convert HTML entities like &amp; to &
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Remove emojis / non-ASCII characters
    text = ' '.join(text.split())  # Remove extra spaces and newlines
    return text.strip()

# ----------------------------------------------------
# Main Scraper Class for extracting remote jobs
# ----------------------------------------------------
class RemoteJobScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/115.0.0.0 Safari/537.36"
        }
        self.jobs = []

    # ------------------------------------------------
    # Fetch HTML content from the provided URL
    # ------------------------------------------------
    def fetch_html(self):
        try:
            response = requests.get(self.url, headers=self.headers, timeout=10)
            response.raise_for_status()
            logging.info("Successfully fetched job page.")
            return response.text
        except requests.exceptions.HTTPError as e:
            logging.error(f"HTTP Error: {e}")
        except requests.exceptions.ConnectionError:
            logging.error("Connection Error: Internet issue or site down.")
        except requests.exceptions.Timeout:
            logging.error("Request timed out.")
        except requests.exceptions.RequestException as e:
            logging.error(f"Request Error: {e}")
        return None

    # ------------------------------------------------
    # Parse and clean job listings from HTML content
    # ------------------------------------------------
    def parse_jobs(self, html_text):
        try:
            soup = BeautifulSoup(html_text, "html.parser")
            for tr in soup.find_all("tr", class_="job"):
                try:
                    # Extract title and company
                    title = clean_text(tr.find("h2").text)
                    company = clean_text(tr.find("h3").text)
                    link = "https://remoteok.com" + tr.get("data-href", "")

                    # Extract job description or requirement
                    desc_tag = tr.find("td", class_="company_and_position")
                    requirement = clean_text(desc_tag.text if desc_tag else "")

                    # Extract location and salary
                    loc_salary_tag = tr.find("div", class_="location")
                    loc_salary = clean_text(loc_salary_tag.text if loc_salary_tag else "")

                    if "$" in loc_salary:
                        location, salary = loc_salary.split("$", 1)
                        location = location.strip()
                        salary = "$" + salary.strip()
                    else:
                        location = loc_salary or "Worldwide"
                        salary = "N/A"

                    # Add job data to the list
                    self.jobs.append({
                        "Title": title,
                        "Company": company,
                        "Location": location,
                        "Salary": salary,
                        "Requirement": requirement,
                        "Link": link
                    })

                except Exception as parse_err:
                    logging.warning(f"Error parsing a job entry: {parse_err}")
                    continue

            logging.info(f"Parsed {len(self.jobs)} job(s) successfully.")

        except Exception as soup_err:
            logging.error(f"Error parsing HTML: {soup_err}")

    # ------------------------------------------------
    # Save the job data to a CSV file
    # ------------------------------------------------
    def save_to_csv(self, filename="remote_jobs.csv"):
        try:
            if os.path.exists(filename):
                os.remove(filename)
                logging.info(f"Old file '{filename}' deleted.")

            df = pd.DataFrame(self.jobs)
            df.to_csv(filename, index=False)
            logging.info(f"Job data saved to '{filename}'.")

        except PermissionError:
            logging.error("Permission denied while saving the file.")
        except Exception as e:
            logging.error(f"Failed to save file: {e}")

    # ------------------------------------------------
    # Run the scraper (end-to-end process)
    # ------------------------------------------------
    def run(self):
        html_text = self.fetch_html()
        if html_text:
            self.parse_jobs(html_text)
            if self.jobs:
                self.save_to_csv()
            else:
                logging.warning("No jobs found.")
        else:
            logging.error("Failed to retrieve or parse job listings.")

# ----------------------------------------------------
# Entry point - Executes when script is run directly
# ----------------------------------------------------
if __name__ == "__main__":
    try:
        scraper = RemoteJobScraper("https://remoteok.com/remote-python-jobs")
        scraper.run()
    except KeyboardInterrupt:
        logging.warning("Script interrupted by user.")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
