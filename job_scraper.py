import pandas as pd
from bs4 import BeautifulSoup

# Read HTML file
with open("python_jobs.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file.read(), 'html.parser')

# Extract data
jobs = []
for job in soup.find_all("div", class_="job_seen_beacon"):
    try:
        title = job.find("h2", class_="jobTitle").find("span").text.strip()
        company = job.find("span", {"data-testid": "company-name"})
        location = job.find("div", {"data-testid": "text-location"})
        link = job.find("a", class_="jcs-JobTitle")

        jobs.append({
            "Title": title,
            "Company": company.text.strip() if company else "N/A",
            "Location": location.text.strip() if location else "N/A",
            "URL": "https://pk.indeed.com" + link['href'] if link else "N/A"
        })
    except:
        continue

# Save to CSV
df = pd.DataFrame(jobs)
df.to_csv("python_jobs_output.csv", index=False)
