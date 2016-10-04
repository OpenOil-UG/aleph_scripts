import requests # library for downloading pages

def download_file(file_number):
    page_number = 1
    extracted_text = ''
    while True: # loop forever
        url = 'http://aleph.openoil.net/api/1/documents/%s/pages/%s' % (file_number, page_number)
        response = requests.get(url)
        if response.status_code != 200: # this page doesn't exist
            break # exit the loop
        page_text = response.json()['text']
        extracted_text += page_text
    return extracted_text


if __name__ == '__main__':
    print(download_file(2593083))
