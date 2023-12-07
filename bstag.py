from flask import Flask, request, jsonify
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin

app = Flask(__name__)

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

@app.route('/extract_images', methods=['POST'])
def handle_image_extraction():
    data = request.get_json()
    
    if 'url' not in data:
        return jsonify({'error': 'Missing URL parameter'}), 400

    url = data['url']
    extracted_image_urls = extract_image_urls(url)

    if extracted_image_urls:
        return jsonify({'image_urls': extracted_image_urls})
    else:
        return jsonify({'message': 'No images found.'})

if __name__ == '__main__':
    app.run(debug=True)
