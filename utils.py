import re
import os


def get_config():
    from ConfigParser import ConfigParser
    parent_dir = os.path.dirname(os.path.abspath(__file__))

    tmp_conf = ConfigParser()
    tmp_conf.read('{0}/autobonweb.conf'.format(parent_dir))
    c = {}
    c.update(tmp_conf.items('main'))
    return c


def syslog_clean(meat=None):
    '''
IN: bon_csv2html output (one long string with newlines)
    possibly prefixed with syslog timestamps and identifiers

OUT: pure bon_csv2html (one long string with newlines)
    '''
    conf = get_config()

    out_list = []
    bonnie_ver_id = conf['bonnie_version_string']
    lines = meat.split('\n')
    for line in lines:
        if bonnie_ver_id not in line:
            continue
        # strip all text before BONNIE_VER_STR
        # e.g., Feb 19 08:01:12 foohost something-bonnie: 1.97,1.97,foohost...
        tmp_str = re.sub('^.*' + bonnie_ver_id, bonnie_ver_id, line)
        out_list.append(tmp_str)
    # filter out all empty/None items
    out_list = list(filter(None, out_list))
    return '\n'.join(out_list)


def html_us_to_ms(meat=None):
    ''' bonnie outputs numbers in both ms and us.
        bon_csv2html colours table cells based on these values.
        transform all figures into ms _after_ running the output through
          bon_csv2html.
    '''
    tag_num = 0
    soup = meat.split('</td>')
    for tag in meat.split('</td>'):
        tag.replace('\n', '')
        if 'us' in tag:
            soup[tag_num] = ms_munge(tag)
        tag_num += 1
    out_soup = '</td>'.join(soup)
    return out_soup


def ms_munge(in_str=None):
    tag_chunks = in_str.split('>')
    # e.g., ['<td bgcolor="#11EE00" colspan="2"', '20709us']

    measurement = tag_chunks[-1]
    # e.g., 20709us

    # returns ['20709', ''], so just pick the first element
    us_int = int(measurement.split('us')[0])
    # 20709

    # just the tenths, please
    ms = us_int/1000
    # 21

    tag_chunks[-1] = str(ms) + 'ms'
    out_str = '>'.join(tag_chunks)
    return out_str


def save_to_disk(filename=None, in_html=None):
    conf = get_config()
    pathname = '{0}/{1}'.format(conf['results_dir'],
                                filename)
    f = open(pathname, 'w')
    f.write(in_html)
    f.close()
    return
