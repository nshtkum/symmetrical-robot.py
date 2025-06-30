import requests
from bs4 import BeautifulSoup

def scrape_magicbricks_project(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": f"Failed to fetch page: {response.status_code}"}

    soup = BeautifulSoup(response.content, 'html.parser')

    data = {}


    try:
        title = soup.find("h1").get_text(strip=True)
        data["Project Title"] = title
    except:
        data["Project Title"] = "N/A"


    try:
        price_block = soup.find("div", text=lambda x: x and "₹" in x).get_text(strip=True)
        data["Price"] = price_block
    except:
        data["Price"] = "N/A"

    
    try:
        bhk_info = soup.find("div", class_="mb-srp__card__title").get_text(strip=True)
        data["BHK Type"] = bhk_info
    except:
        data["BHK Type"] = "N/A"

    
    try:
        location = soup.find("div", class_="project-location").get_text(strip=True)
        data["Location"] = location
    except:
        data["Location"] = "N/A"


    try:
        amenities_section = soup.find_all("div", class_="amenities-info")
        amenities = [a.get_text(strip=True) for a in amenities_section]
        data["Amenities"] = amenities if amenities else "N/A"
    except:
        data["Amenities"] = "N/A"

    return data
