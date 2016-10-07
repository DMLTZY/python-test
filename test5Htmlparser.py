from html.parser import HTMLParser
from html.entities import name2codepoint


class My(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('start tag is <{}>'.format(tag))
        print('start attrs is : {}'.format(attrs))

    def handle_endtag(self, tag):
        print('end tag is <{}>'.format(tag))

    def handle_startendtag(self, tag, attrs):
        print('startend tag is <{}/>'.format(tag))
        print('startend tag attr is : {}'.format(attrs))

    def handle_data(self, data):
        print('data is: {}'.format(data))


parser = My()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br/>END</p>
</body></html>'''
            )