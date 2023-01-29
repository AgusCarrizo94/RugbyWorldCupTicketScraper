import requests
from bs4 import BeautifulSoup
from msgWsp import whatsAppMessage

URL1 = "https://tickets.rugbyworldcup.com/en/resale_italy_uruguay"
URL2 = "https://tickets.rugbyworldcup.com/en/resale_quarter_final1"
URL3 = "https://tickets.rugbyworldcup.com/en/resale_semi_final2"
URL4 = "https://tickets.rugbyworldcup.com/en/resale_final"

URLs = [URL1, URL2, URL3, URL4]

for url in URLs:
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    title = soup.section.find(attrs={"class": "title"})
    # print(title.text)

    subtitle = soup.section.find(attrs={"class": "subtitle"})
    subtitleChildListd = []
    for child in subtitle:
        childText = child.string
        subtitleChildListd.append(childText)

    subtitleOutputText = subtitleChildListd[0] + " " + subtitleChildListd[1] + " " + subtitleChildListd[3] + " " + subtitleChildListd[5]
    # print(subtitleOutputText.strip())

    try:
        category = soup.table.td.div.find_all('span')
        categoryChildList = []
        for child in category:
            childText = child.string
            categoryChildList.append(childText)

        priceInfo = soup.table.td.find(attrs={"class": "price-info"})

        outputText = categoryChildList[0] + ", Tickets Available: " + categoryChildList[2] + ", Price per ticket: " + \
                     priceInfo.text.strip().replace("/ticket","")
        # print(outputText)

        messageText = title.text + "\n" + subtitleOutputText.strip() + "\n" + outputText
        # print(messageText)
        whatsAppMessage(messageText)

    except:
        messageText = title.text + "\n" + subtitleOutputText.strip() + "\n" + "No tickets available!\n"
        # print(messageText)
        whatsAppMessage(messageText)

