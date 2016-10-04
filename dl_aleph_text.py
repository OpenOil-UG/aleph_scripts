import requests # library for downloading pages
import urllib

APIKEY = 'your_key_here'

def download_file(file_number):
    page_number = 1
    extracted_text = u''
    while True: # loop forever
        url = 'http://aleph.openoil.net/api/1/documents/%s/pages/%s' % (file_number, page_number)
        response = requests.get(url)
        if response.status_code != 200: # this page doesn't exist
            break # exit the loop
        page_text = response.json()['text']
        extracted_text += u'\n' +  page_text
        page_number += 1
    return extracted_text


def output_file(docnum, text):
    basedir = '/tmp'
    filename = '/tmp/aleph_doc_%05d' % docnum
    with open(filename, 'wb') as outfile:
        outfile.write(text.encode('utf-8'))

def docids_matching_search(searchterm):
    params = {
        'q': searchterm or 'annual report',
        'apikey': APIKEY,
        'offset': 1000,
        'limit': 300}
    url ='http://aleph.openoil.net/aleph_api/1/query'
    response = requests.get(url, params=params).json()
    for jsondata in response['results']:
        docid = int(jsondata['viewer_url'].split('/')[-1])
        filetext = download_file(docid)
        output_file(docid, filetext)


if __name__ == '__main__':
    docids_matching_search('annual report')
