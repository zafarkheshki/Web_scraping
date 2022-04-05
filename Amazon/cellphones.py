from requests_html import HTMLSession

urllist = ['https://www.amazon.com/Apple-iPhone-12-Pro-Max/dp/B09JFGT21S/ref=sr_1_6?qid=1649189165&refinements=p_89%3AApple&rnid=2528832011&s=wireless&sr=1-6',
            'https://www.amazon.com/Apple-iPhone-12-Pro-Max/dp/B09JFFG8D7/ref=sr_1_3?crid=32BX0NEAOV1MT&keywords=apple+iPhone&qid=1649113923&sprefix=apple+iphone+%2Caps%2C217&sr=8-3',
            'https://www.amazon.com/Apple-iPhone-12-Pro-Max/dp/B09JFQ9G5Z/ref=sr_1_2?qid=1649189165&refinements=p_89%3AApple&rnid=2528832011&s=wireless&sr=1-2']

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    
    product = {
        'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
        'price': r.html.xpath('//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]', first=True).text
    }
    print(product)
    return product

mobileprices = []
for url in urllist:
    mobileprices.append(getPrice(url))

print(len(mobileprices))