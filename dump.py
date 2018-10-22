#!/usr/bin/env python3

from __future__ import print_function
import argparse
import os
import sys
import glob

def main(args) :

    img_dir = args.in_dir
    if args.absolute :
        img_dir = os.path.abspath(img_dir)
    if not os.path.isdir(img_dir) :
        print('ERROR provided file directory (={}) is not found!'.format(img_dir))
        sys.exit()
    images = glob.glob('{}/*.png'.format(img_dir))
    if len(images) == 0 :
        print('WARNING found no (png) images in provided directory!')
        return

    print('in dir = {}'.format(args.in_dir))
    out_filename = [x for x in  args.in_dir.strip().split('/') if x][-1].replace('/','')
    title = out_filename
    if args.title != '' :
        title = args.title
    print(' > {}'.format(out_filename))
    out_filename = 'page_{}.html'.format(out_filename)
    print('INFO output HTML filename: {}'.format(out_filename))

    with open(out_filename, 'w') as out_file :
        out_file.write('<html>\n')
        out_file.write('<body>\n')
        out_file.write('<h1> {} </h1>\n'.format(title))
        out_file.write('<table border=1>\n')

        for idx, img in enumerate(images) :
            src_node = '<a href="{}"><img src="{}" width="350"/></a>'.format(img, img)
            start = ''
            end = ''
            if idx % 3 == 0 :
                start = '<tr><td>'
                end = '</td>'
            elif idx % 3 == 1 :
                start = '<td>'
                end = '</td>'
            elif idx % 3 == 2 :
                start = '<td>'
                end = '</td></tr>'
            line = '{}{}{}'.format(start, src_node, end)
            out_file.write(line + '\n')
        out_file.write('</table>\n')
        out_file.write('</body>\n')
        out_file.write('</html>\n')

#___________________________
if __name__ == '__main__' :

    parser = argparse.ArgumentParser(
        description = 'Provided a directory in the local path, build a simple HTML page presenting image files in that directory'
    )
    parser.add_argument('-i', '--in-dir', required = True,
        help = 'Provide a directory of plots'
    )
    parser.add_argument('-p', '--page-name', default = '',
        help = 'Provide a name for the output HTML file (default: based on input dir name)'
    )
    parser.add_argument('-t', '--title', default = '',
        help = 'Provide a header title for the plots'
    )
    parser.add_argument('--absolute', default = False, action = 'store_true',
        help = 'Use absolute (full) paths for image sources'
    )
    args = parser.parse_args()

    main(args)
