import os
from argparse import ArgumentParser as ap
from categorize.config import Config
import re


class FileSorter:
    def __init__(self):
        self.config = Config()
        self.config.read_config()

        self.extensions = {}
        self.path_patterns = {}
        self.categorized_files = {}

        self.working_directory = ''

    def configure(self):
        self.extensions = self.config.get_categories()
        self.path_patterns = self.config.get_path_patterns()

        for category in self.extensions:
            self.categorized_files[category] = []

    def set_working_directory(self, directory):
        self.working_directory = directory

    def get_all_files_from_dir(self):
        all_files = []

        files_from_dir = os.listdir(self.working_directory)

        for file in files_from_dir:
            if os.path.isfile(os.path.join(self.working_directory, file)):
                all_files.append(file)

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

    args = parser.parse_args()

    sorter = FileSorter()

    if args.directory:
        sorter.set_working_directory(args.directory)

        # configure sorter
        sorter.configure()

        all_files = sorter.get_all_files_from_dir()
        categorized_files = sorter.categorize_files(all_files)

        sorter.sort_files()


if __name__ == "__main__":
    main()
