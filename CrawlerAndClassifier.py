import requests
from bs4 import BeautifulSoup
import grabLocation
import json
import joblib

# Load the trained TF-IDF vectorizer and RandomForestClassifier
vectorizer = joblib.load("tfidf_vectorizer.joblib")
classifier = joblib.load("random_forest_classifier.joblib")



crime = {}


def crawl_nigerian_news_sites():
    # Define the URLs of the Nigerian news websites you want to scrape
    urls = [

        'https://punchng.com/topics/metro-plus/',
        # add other urls
    ]

    # Loop through each URL
    for url in urls:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract crime information based on the HTML structure of the website
            crime_elements = soup.find_all('div', class_='post-content')

            # Process and print the extracted information
            for index, crime_element in enumerate(crime_elements):
                crime_info = crime_element.text.strip()

                # Test the model with a new crime description
                new_crime_description = crime_info

                new_description_tfidf = vectorizer.transform([new_crime_description])

                # Predict the danger level for the new description
                predicted_danger_level = classifier.predict(new_description_tfidf)[0]


                crime_location = grabLocation.extract_locations(crime_info)
                print(f"Crime Information: {crime_info} \n ------>>  {crime_location}")

                # crime[index] = ({'id':index,'location':crime_location,'news':crime_info})
                crime.update({index:{'id':int(index), 'location':crime_location,'news':crime_info,'danger':int(predicted_danger_level),'timeStamp':f'{datetime.datetime.now()}'}})
                print(crime)


        else:
            print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")



if __name__ == "__main__":

    crawl_nigerian_news_sites()

