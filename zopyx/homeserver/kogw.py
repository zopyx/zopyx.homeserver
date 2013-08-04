
import requests
import lxml.etree

URL = 'http://192.168.0.11/hscl?sys/cobjects.xml'

def get_cobjects():
    """ Fetch cobject descriptions from homeserver """

    result = requests.get(URL)
    if result.status_code != 200:
        raise RuntimeError('Could not fetch cobjects.xml')
    xml = result.text.encode('utf-8')
    root = lxml.etree.fromstring(xml)
    return (dict(node.attrib)
            for node in root.xpath('//cobject'))

def main():

    cobjects = get_cobjects()
    for cobject in cobjects:
        print cobject

if __name__ == '__main__':
    main()
