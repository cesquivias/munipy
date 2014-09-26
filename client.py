import contextlib
import urllib

from xml.dom.minidom import parseString

def predictions_url(stop_id):
    return 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=sf-muni&useShortTitles=true&stopId=' + str(stop_id)

def predictions(url):
    with contextlib.closing(urllib.urlopen(url)) as f:
        dom =  parseString(f.read())
    predictions = dom.getElementsByTagName('predictions')
    return [{'title': ps.getAttribute('routeTitle'),
             'predictions': sorted([int(p.getAttribute('minutes'), 10)
                                    for p
                                    in ps.getElementsByTagName('prediction')])[:2]
             } for ps in predictions]

def main(stop_ids):
    predictions(predictions_url(stop_ids))

if __name__ == '__main__':
    import sys

    main(int(e) for e in sys.argv[1:])
