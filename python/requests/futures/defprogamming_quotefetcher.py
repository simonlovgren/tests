#!/usr/bin/env python3

import time, random, html
from requests_futures.sessions import FuturesSession


# Available tags
tags = [
    'agile',
    'api',
    'beta',
    'bugs',
    'collaboration',
    'commenting',
    'compatibility',
    'complexity',
    'computer science',
    'computers',
    'corporate',
    'creativity',
    'data',
    'deadlines',
    'debugging',
    'deploying',
    'diversity',
    'documentation',
    'dry',
    'education',
    'error',
    'estimating',
    'extreme programming',
    'features',
    'functions',
    'go',
    'hackers',
    'hacking',
    'hardware',
    'ideas',
    'innovation',
    'java',
    'javascript',
    'languages',
    'learning',
    'linux',
    'maintenance',
    'management',
    'metrics',
    'naming',
    'nodejs',
    'objects',
    'oop',
    'open source',
    'optimization',
    'pair programming',
    'perl',
    'php',
    'planning',
    'platform',
    'productivity',
    'programmers',
    'programming',
    'prototyping',
    'quality',
    'refactoring',
    'regexp',
    'releasing',
    'reusing',
    'ruby on rails',
    'scaling',
    'scrum',
    'security',
    'softwares',
    'specialization',
    'specification',
    'standards',
    'startups',
    'tdd',
    'teams',
    'technology',
    'testing',
    'theory',
    'threads',
    'unix',
    'users',
    'version-control',
    'xml'
]

session = FuturesSession()
# request is started in background
tag = random.choice(tags)
print( f'Selected tag: {tag}' )
future_quote = session.get( f'https://www.defprogramming.com/page-data/quotes-tagged-with/{tag}/page-data.json')
print( f'Quote request started.' )

# Do some other work
for i in range( 1,4 ):
    time.sleep( 1 )
    print( f'Working with other stuff for {i} second{"s" if i > 1 else ""}.' )

# wait for the request to complete, if it hasn't already
response = future_quote.result()
if ( response.status_code == 200 ):
    quote = random.choice( response.json()['result']['pageContext']['quotes'] )
    print( '' )
    print( f'    {html.unescape(quote["body"])}')
    if( len( quote['authors'] ) > 0 ):
        print( f'    - {", ".join(quote["authors"])} on {"/".join(quote["tags"])}.')
    print( '' )
else:
    print( f'Request failed (status {response.status_code})' )