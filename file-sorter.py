import os
import re

class FileSorter:
    def __init__(self):
        self.path_patterns = {
            'pictures': re.compile('^.*\.(jpg|JPG|gif|GIF|png|PNG|svg|SVG|webp|WEBP\
                |tiff|TIFF|psd|PSD|eps|EPS|ai|AI|indd|INDD|raw|RAW|heic|HEIC)$'),
            'videos': re.compile('^.*\.(mp4|MP4|m4a|M4A|m4v|M4V|f4v|F4V|webm|WEBM\
                |f4a|F4A|m4b|M4B|m4r|M4R|f4b|F4B|mov|MOV|3gp|3GP|3g2|3G2|3gpp|3GPP\
                |3gpp2|3GPP2|wmv|WMV|wma|WMA|flv|FLV|avi|AVI)$'),
            'audios': re.compile('^.*\.(mp3|MP3|wav|WAV|flac|FLAC|aac|AAC$)'),
            'documents': re.compile('^.*\.(pdf|PDF|doc|DOC|docx|DOCX|odt|ODT|rtf|RTF\
                htm|HTM|html|HTML|xml|XML)$'),
            'spreadsheets': re.compile('^.*\.(xls|XLS|xlsx|XLSX|ods|ODS)$'),
            'presentations': re.compile('^.*\.(ppt|PPT|pptx|PPTX)$'),
            'txt-files': re.compile('^.*\.(txt|TXT)$'),
            'archives': re.compile('^.*\.(zip|ZIP|7z|7Z|rar|RAR|gz|GZ|bz2|BZ2|xz|XZ)$')
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
        pass

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


if __name__ == "__main__":
    sorter = FileSorter()

    sorter.set_working_directory('/home/kantegory/Загрузки')
    all_files = sorter.get_all_files_from_dir()
    categorized_files = sorter.categorize_files(all_files)
    sorter.sort_files()
