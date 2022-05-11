import requests
from bs4 import BeautifulSoup
import json #to store

all_data = []
#to get page 1 and 2
item_counter = 0
total_pages = range(0,2)

for item_counter in total_pages:

    url = "https://collection.sciencemuseumgroup.org.uk/search/objects/images/image_license?q=psychology&page[size]=100&page[number]="

    url = url + str(item_counter)

    page_request_results = requests.get(url)

    page_html = page_request_results.text

    soup = BeautifulSoup(page_html, features="html.parser")

    all_divs = soup.find_all("div", attrs = {'class':'searchresults__column'})

    for a_div in all_divs:

        #looping through each object div

        #titles
        card_head = a_div.find_all('h2')
        titles = []
        for headings in card_head:
            titles.append(headings.text.strip())
        
        #DATES
        card_dates = a_div.findChildren("p")
        thedates = []
        thedates.append(card_dates[1].text)
                



        #links URLS
        a_link = a_div.find('a')
        link = a_link['href']

        #all photos img src
        image_tags = a_div.find_all('img')
        imagelinks = []
        for image_tag in image_tags:
            imagelinks.append(image_tag['src'])



    #creating a python dictionary to make new object w each iteration
        object = {
            'titles': titles,
            'url': link,
            'imagelinks': imagelinks,
            'date': thedates
        }   

        all_data.append(object)
    print(all_data)
    item_counter = item_counter + 1



#     # print(titles, link)
json.dump(all_data, open('psychobjects4.json','w'), indent=2)

#print(all_data)


# # print(all_divs)

# # for a_div in all_divs:
# #     print(a_div)
# #     print("----")

