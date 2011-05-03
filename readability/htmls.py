from cleaners import normalize_spaces, clean_attributes
from encodings import get_encoding
from lxml.html import tostring
import logging
import lxml.html
import re

logging.getLogger().setLevel(logging.DEBUG)

utf8_parser = lxml.html.HTMLParser(encoding='utf-8')

def build_doc(page):
    enc = get_encoding(page)
    page_enc = page.decode(enc, 'replace').encode('utf-8')
    doc = lxml.html.document_fromstring(page_enc, parser=utf8_parser)
    return doc

def js_re(src, pattern, flags, repl):
    return re.compile(pattern, flags).sub(src, repl.replace('$', '\\'))


def normalize_entities(cur_title):
    entities = {
        u'\u2014':'-',
        u'\u2013':'-',
        u'&mdash;': '-',
        u'&ndash;': '-',
        u'\u00A0': ' ',
        u'\u00AB': '"',
        u'\u00BB': '"',
        u'&quot;': '"',
    }
    for c, r in entities.iteritems():
        if c in cur_title:
            cur_title = cur_title.replace(c, r)

    return cur_title

def norm_title(title):
    return normalize_entities(normalize_spaces(title))

def get_title(doc):
    title = doc.find('.//title').text
    if not title:
        return '[no-title]'
    
    return norm_title(title)

def shortify_title(doc):
    title = doc.find('.//title').text
    if not title:
        return '[no-title]'
    
    title = orig = norm_title(title)
    
    for delimiter in [' | ', ' - ', ' :: ', ' / ']:
        if delimiter in title:
            parts = orig.split(delimiter)
            if len(parts[0].split()) >= 4:
                title = parts[0]
                break
            elif len(parts[-1].split()) >= 4:
                title = parts[-1]
                break
    else:
        if ': ' in title:
            parts = orig.split(': ')
            if len(parts[-1].split()) >= 4:
                title = parts[-1]
            else:
                title = orig.split(': ', 1)[1]

    if len(title.split()) <= 4:
        h1 = list(doc.iterfind('.//h1'))
        if len(h1) == 1:
            title = norm_title(h1[0].text)
        elif len(h1) == 0:
            h2 = list(doc.iterfind('.//h2'))
            if len(h1) == 1:
                title = norm_title(h2[1].text)

    if not 15 < len(title) < 150:
        return orig

    return title

def get_body(doc):
    [ elem.drop_tree() for elem in doc.xpath('.//script | .//link | .//style') ]
    raw_html = unicode(tostring(doc.body or doc))
    cleaned = clean_attributes(raw_html)
    try:
        #BeautifulSoup(cleaned) #FIXME do we really need to try loading it?
        return cleaned
    except Exception: #FIXME find the equivalent lxml error
        logging.error("cleansing broke html content: %s\n---------\n%s" % (raw_html, cleaned))
        return raw_html
