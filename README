This code is under the Apache License 2.0.  http://www.apache.org/licenses/LICENSE-2.0

This is a modfied for higher recall rate of famous python port(https://github.com/buriy/python-readability) a ruby port of arc90's readability project

http://lab.arc90.com/experiments/readability/
https://github.com/buriy/python-readability

In few words,
Given a html document, it pulls out the main body text and cleans it up.
It also can clean up title based on latest readability.js code.

Based on:
 - Latest readability.js ( https://github.com/MHordecki/readability-redux/blob/master/readability/readability.js )
 - Ruby port by starrhorne and iterationlabs
 - Python port by gfxmonk ( https://github.com/gfxmonk/python-readability , based on BeautifulSoup )
 - Python port by buriy (https://github.com/buriy/python-readability)
 - Decruft effort to move to lxml ( http://www.minvolai.com/blog/decruft-arc90s-readability-in-python/ )
 - "BR to P" fix from readability.js which improves quality for smaller texts.
 - Github users contributions.

Installation::

    pip install readability-dig

Usage::

    from readability.readability import Document
    import urllib
    html = urllib.urlopen(url).read()
    readable_article = Document(html).summary()
    readable_title = Document(html).short_title()

Command-line usage::

    python -m readability.readability -u http://pypi.python.org/pypi/readability-dig

To open resulting page in browser::

    python -m readability.readability -b -u http://pypi.python.org/pypi/readability-dig

Using positive/negative keywords example::

    python -m readability.readability -p intro -n newsindex,homepage-box,news-section -u http://python.org


Document() kwarg options:

 - attributes:
 - debug: output debug messages
 - min_text_length:
 - retry_length:
 - url: will allow adjusting links to be absolute
 - positive_keywords: the list of positive search patterns in classes and ids, for example: ["news-item", "block"]
 - negative_keywords: the list of negative search patterns in classes and ids, for example: ["mysidebar", "related", "ads"]
