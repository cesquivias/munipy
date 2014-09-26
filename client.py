"""Display NextBus predictions on LED sign.

Basic data flow:
stop_id -> url -> next_bus_dom -> {route_tag: Predictions} -> [(str/title, str/msg)]
"""

import contextlib
import urllib

from collections import namedtuple
from functools import partial
from xml.dom.minidom import parseString


Prediction = namedtuple('Prediction', ['route_tag', 'direction', 'minutes'])


def predictions_url(stop_id):
    return 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=sf-muni&useShortTitles=true&stopId=' + str(stop_id)

def next_bus_dom(url):
    with contextlib.closing(urllib.urlopen(url)) as f:
        return parseString(f.read())

def predictions(dom):
    predictionses = dom.getElementsByTagName('predictions')

    directions = {p.getAttribute('routeTag'):
                  p.getElementsByTagName('direction')
                  for p in predictionses}

    predictions = {}
    for route, direction in directions.iteritems():
        for d in direction:
            direction = d.getAttribute('title').split()[0]
            result = []
            for p in d.getElementsByTagName('prediction'):
                result.append(
                    Prediction(route, direction,
                               int(p.getAttribute('minutes'))))
                predictions[route] = sorted(result,
                                            key=lambda pred: pred.minutes)[:2]
    return predictions

def prediction_messages(predictions):
    return [('{0}-{1}'.format(route, preds[0].direction),
             ' & '.join('{0} min'.format(p.minutes) for p in preds))
            for route, preds
            in predictions.iteritems()]

def main(stop_ids):
    predictions(predictions_url(stop_ids))

if __name__ == '__main__':
    import sys

    main(int(e) for e in sys.argv[1:])
