# Άσκηση 20.2 Ανάκτηση τηλεφώνων από ιστοσελίδα τμήματος
import urllib.request
import urllib.error
import re
import os.path
pattern = 'faculty.html?id='
html = ''
prof_url = '/gr/personnel/faculty.html?id='
url = 'http://www.ece.upatras.gr/gr/personnel/faculty.html'

def search_faculty_tel(url):
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            char_set = response.headers.get_content_charset()
            html = response.read().decode(char_set)
    except urllib.error.HTTPError as e:
        print('Σφάλμα HTTP:', e.code)
        return False
    except urllib.error.URLError as e:
        print('Αποτυχία σύνδεσης στον server')
        print('Αιτία: ', e.reason)
        return False
    else:
        title = re.findall(r'<title\b[^>]*>(.*?)</title>', html.replace('\n', ''))
        if 'Τομέας ' in title: return False
        else: 
            td = re.findall(r'<td\b[^>]*>(.*?)</td>', html.replace('\n', ''))
            tel = ''
            for d in td:
                if 'τηλ' in d:
                    tel = td[td.index(d)+1]
                    tel = re.findall(r"[ 0-9+-/]*", tel)
                    for t in tel:
                        if len(t) > 5 :
                            tel_number = t
                            return (title[0], tel_number)
            return False
                    

    
if not os.path.isfile('faculty_web_page.txt'):
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            char_set = response.headers.get_content_charset()
            html = response.read().decode(char_set)
    except urllib.error.HTTPError as e:
        print('Σφάλμα HTTP:', e.code)
    except urllib.error.URLError as e:
            print('Αποτυχία σύνδεσης στον server')
            print('Αιτία: ', e.reason)
    else:
        with open('faculty_web_page.txt', 'w', encoding = 'utf-8') as f_faculty:
            f_faculty.write(html)
else:
    html = open('faculty_web_page.txt', 'r', encoding = 'utf-8').read()
faculty_url = []
if html:
    html = html.replace('\n', '')
    anchors = re.findall(r'<a href="(.*?)"', html)
    for a in anchors:
        if pattern in a:
            faculty_url.append('http://www.ece.upatras.gr'+a)
    for a in faculty_url :
        tel = search_faculty_tel(a)
        if tel: print (tel)


            
#prof_url = 'http://www.ece.upatras.gr/gr/personnel/faculty.html?id=288'
