#!/usr/bin/env python

'''
v0.01 - 23-Feb-2018 - BEGIN

autobonweb: A cheap front end to bon_csv2html.
Saves your HTMLified bonnie++ results with unified units.
'''

from bottle import request, route, run, template
from datetime import datetime
import envoy
import utils  # autobonweb/utils.py

conf = utils.get_config()


def bonnify(in_str=None):
    '''IN: textarea input.
      OUT: bon_csv2html output with unified units.
    '''
    r = envoy.run(conf['bon_csv2html'], data=in_str)
    print(r.std_err)
    unified_units = utils.html_us_to_ms(r.std_out)
    return unified_units


@route('/ingest', method='POST')
def ingest():
    # valid bonnie 1.97 output?
    # POST things here, run them through bon_csv2html, save stdout to file
    cleaned_input = utils.syslog_clean(request.forms.get('meat'))
    bon_results = bonnify(cleaned_input)
    if request.forms.get('write_to_disk') == '1':
        filename = '{0}_{1}_{2}_{3}_{4}.html'.format(
            request.forms.get('date'),
            request.forms.get('load_gen'),   # nfs-oriented
            request.forms.get('target'),     # delete at
            request.forms.get('sec_level'),  # will
            request.forms.get('tag'))        # comment appended to filename
        utils.save_to_disk(filename=filename,
                           in_html=bon_results)
    return bon_results


@route('/')
def index():
    now = datetime.now()
    date_str = datetime.strftime(now, '%Y-%m-%d')
    return template('input.tpl',
                    date=date_str,
                    bind_addr=conf['bind_addr'],
                    results_url_root=conf['results_url_root'])


def main():
    run(host=conf['bind_addr'],
        port=conf['bind_port'])
    return


if __name__ == "__main__":
    main()
