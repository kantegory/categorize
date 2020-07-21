import os
import re
from argparse import ArgumentParser as ap

class FileSorter:
    def __init__(self):
        self.extensions = {
            'pictures': 'jpg|JPG|gif|GIF|png|PNG|svg|SVG|webp|WEBP|tiff|TIFF|psd|PSD|eps|EPS|ai|AI|indd|INDD|raw|RAW|heic|HEIC',
            'videos': 'mp4|MP4|m4a|M4A|m4v|M4V|f4v|F4V|webm|WEBM|f4a|F4A|m4b|M4B|m4r|M4R|f4b|F4B|mov|MOV|3gp|3GP|3g2|3G2|3gpp|3GPP|3gpp2|3GPP2|wmv|WMV|wma|WMA|flv|FLV|avi|AVI',
            'audios': 'mp3|MP3|wav|WAV|flac|FLAC|aac|AAC',
            'documents': 'pdf|PDF|doc|DOC|docx|DOCX|odt|ODT|rtf|RTF|htm|HTM|html|HTML|xml|XML',
            'spreadsheets': 'xls|XLS|xlsx|XLSX|ods|ODS',
            'presentations': 'ppt|PPT|pptx|PPTX',
            'txt-files': 'txt|TXT',
            'archives': 'zip|ZIP|7z|7Z|rar|RAR|gz|GZ|bz2|BZ2|xz|XZ'
        }

        self.path_patterns = {
            'pictures': re.compile('^.*\.({})$'.format(self.extensions['pictures'])),
            'videos': re.compile('^.*\.({})$'.format(self.extensions['videos'])),
            'audios': re.compile('^.*\.({})$'.format(self.extensions['audios'])),
            'documents': re.compile('^.*\.({})$'.format(self.extensions['documents'])),
            'spreadsheets': re.compile('^.*\.({})$'.format(self.extensions['spreadsheets'])),
            'presentations': re.compile('^.*\.({})$'.format(self.extensions['presentations'])),
            'txt-files': re.compile('^.*\.({})$'.format(self.extensions['txt-files'])),
            'archives': re.compile('^.*\.({})$'.format(self.extensions['archives']))
        }

        self.categorized_files = {
            'pictures': [],
            'videos': [],
            'audios': [],
            'documents': [],
            'spreadsheets': [],
            'presentations': [],
            'txt-files': [],
            'archives': []
        }

        self.working_directory = ''

    def set_working_directory(self, directory):
        self.working_directory = directory

    def get_path_patterns(self):
        print(self.path_patterns)
        for pattern in self.path_patterns:
            extensions = self.extensions[pattern].split('|')
            extensions = ['.{}'.format(e) for e in extensions]
            extensions = ', '.join(extensions)
            print('Category {}, extensions: {}'.format(pattern, extensions))

    def get_all_files_from_dir(self):
        all_files = [file for file in os.listdir(self.working_directory)\
                    if os.path.isfile(os.path.join(self.working_directory, file))]

        return all_files

    def categorize_files(self, files):
        for file in files:
            for pattern in self.path_patterns:
                if re.match(self.path_patterns[pattern], file):
                    self.categorized_files[pattern].append(file)

        return self.categorized_files

    def sort_files(self):
        for category in self.categorized_files:
            # create directory for category
            path = os.path.join(self.working_directory, category)
            if not os.path.exists(path) and len(self.categorized_files[category]):
                os.mkdir(path)

            # get all files for this category
            files = self.categorized_files[category]

            for file in files:
                source_path = os.path.join(self.working_directory, file)
                dest_path = os.path.join(path, file)

                # move files
                os.replace(source_path, dest_path)


def main():
    parser = ap(description='Sort all of your files in any directory')
    parser.add_argument('--directory', action='store', dest='directory', type=str, help='The name of the directory in which to sort the files')
    parser.add_argument('--show', action='store_true', help='Showing all path_patterns')

    args = parser.parse_args()

    sorter = FileSorter()

    if args.directory:
        sorter.set_working_directory(args.directory)
        all_files = sorter.get_all_files_from_dir()
        categorized_files = sorter.categorize_files(all_files)
        sorter.sort_files()

    if args.show:
        sorter.get_path_patterns()


if __name__ == "__main__":
    main()
