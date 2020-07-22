import re
import configparser
import os
from argparse import ArgumentParser as ap

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.filename = '{}/categories.ini'.format(os.path.dirname(os.path.abspath(__file__)))
        self.extensions = {}
        self.categories = []
        self.path_patterns = {}

    def read_config(self, filename=None):
        if filename:
            self.filename = filename

        self.config.read(self.filename)

    def get_categories(self):
        self.categories = self.config.sections()

        for category in self.categories:
            self.extensions[category] = self.config[category]['extensions']

        return self.extensions

    def get_path_patterns(self):
        for category in self.categories:
            self.path_patterns[category] = re.compile('^.*\.({})$'.format(self.extensions[category])) 

        return self.path_patterns

    def print_path_patterns(self):
        for pattern in self.path_patterns:
            extensions = self.extensions[pattern].split('|')
            extensions = ['.{}'.format(e) for e in extensions]
            extensions = ', '.join(extensions)
            print('Category {}, extensions: {}'.format(pattern, extensions))

    def edit_path_pattern_name(self, pattern_name, new_name):
        self.add_path_pattern(pattern_name)
        
        # copy all items from old section
        self.config._sections[new_name] = self.config._sections[pattern_name]

        # delete old section
        self.config._sections.pop(pattern_name)

        self.rewrite_config()

    def edit_path_pattern_extensions(self, pattern_name, extensions):
        # put new extensions to section
        self.config._sections[pattern_name]['extensions'] = extensions

        self.rewrite_config()

    def add_path_pattern(self, pattern_name):
        # add new section
        if pattern_name not in self.categories:
            self.config.add_section(pattern_name)

        self.rewrite_config()

    def rewrite_config(self):
        # rewrite config
        f = open(self.filename, 'w')
        self.config.write(f)
        f.close()

        # re-read config
        self.read_config()


def edit_extensions(config, pattern_name):
    extensions = []

    while True:
        ext = input('Write new extension (without ".", like: "PDF") for {} (or Enter for quit):\n'.format(pattern_name))

        if not ext:
            break

        extensions.append(ext)

    extensions = '|'.join(extensions)

    config.edit_path_pattern_extensions(pattern_name, extensions)

    # re-read config
    config.read_config()
    config.get_categories()
    config.get_path_patterns()

    print('New config is: \n')
    config.print_path_patterns()


def main():
    parser = ap(description='File-sorter config utility')
    parser.add_argument('--show', action='store_true', help='Showing all path patterns')
    parser.add_argument('--edit-name', action='store', nargs=2,\
        help='Edit category name,\n usage: file-sorter-config --edit-name old_name new_name')
    parser.add_argument('--edit-ext', action='store', nargs=1,\
        help='Edit category extensions,\n usage: file-sorter-config --edit-ext category_name')
    parser.add_argument('--add', action='store', nargs=1,\
        help='Add new category,\n usage: file-sorter-config --add category_name')


    args = parser.parse_args()

    config = Config()
    config.read_config()
    config.get_categories()
    config.get_path_patterns()

    if args.show:
        config.print_path_patterns()

    if args.edit_name:
        pattern_name, new_name = args.edit_name

        config.edit_path_pattern_name(pattern_name, new_name)

    if args.edit_ext:
        pattern_name = args.edit_ext[0]

        edit_extensions(config, pattern_name)

    if args.add:
        pattern_name = args.add[0]

        config.add_path_pattern(pattern_name)
        edit_extensions(config, pattern_name)


if __name__ == '__main__':
    main()
