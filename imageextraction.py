from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_image_urls(url):
    # Set up Selenium webdriver
    driver = webdriver.Chrome()
    driver.get(url)

    # Wait for the page to load (adjust this based on your page load time)
    driver.implicitly_wait(10)

    # Get the page source after it's loaded
    page_source = driver.page_source

    # Close the webdriver
    driver.quit()

    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract all image elements with 'src' attribute
    image_elements = soup.find_all('img', src=True)

    image_urls = [urljoin(url, img['src']) for img in image_elements]

    return image_urls

# Replace 'YOUR_WORDPRESS_URL' with the actual URL of the WordPress article
wordpress_url = 'https://www.accountancyage.com/2023/12/07/pwc-revolutionises-recruitment-process-to-foster-diversity-and-inclusion/'
extracted_image_urls = extract_image_urls(wordpress_url)

if extracted_image_urls:
    for i, image_url in enumerate(extracted_image_urls, start=1):
        print(f"Image {i} URL: {image_url}")
else:
    print("No images found.")
