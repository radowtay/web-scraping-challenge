#import
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager

#scrape data
def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit visitcostarica.herokuapp.com
    redplanet = "https://redplanetscience.com/"
    browser.visit(redplanet)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    slide_elem = soup.select_one('div', class_='list_text')
    news_title = slide_elem.find('div', class_='content_title').get_text()
    news_blurb = slide_elem.find('div', class_='article_teaser_body').get_text()


    #visit jpl
    jpl_url='https://spaceimages-mars.com'
    browser.visit(jpl_url)
    # Scrape page into Soup
    jpl_html=browser.html
    jpl_soup=bs(jpl_html, 'html.parser')
    jpl_soup
    featured_image_url='https://spaceimages-mars.com/image/featured/mars1.jpg'

    #visit facts
    facts_url="https://galaxyfacts-mars.com"
    tables=pd.read_html(facts_url)
    df=tables[0]
    new_header=df.iloc[0]
    df=df[1:]
    df.columns=new_header
    df=df.drop(['Earth'], axis=1)
    df=df.reset_index(drop=True)
    df=df.rename(columns={'Mars - Earth Comparison':" "})
    mars_html_table=df.to_html()


    hemispheres = [
        {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"},
        {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"}

    ]


    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_blurb": news_blurb,
        "featured_image_url": featured_image_url,
        "mars_html_table":mars_html_table,
        "hemispheres":hemispheres
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data