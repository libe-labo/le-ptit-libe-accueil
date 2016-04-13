#!/usr/bin/env python

import json
import pystache


if __name__ == "__main__":
    with open('config.json', 'r') as dataFile:
        config = json.loads(dataFile.read())

        config['releases'] = sorted(config['releases'], key=lambda x: float(x['id']))
        for release in config['releases']:
            release['hasnum'] = isinstance(release['id'], int)
        config['releases'] = dict(
            current=config['releases'][-1],
            other=reversed(config['releases'][:-1])
        )

        with open('index.mustache', 'r') as templateFile:
            with open('index.html', 'w+') as indexFile:
                indexFile.write(pystache.render(templateFile.read(), config))

    print('OK!')
