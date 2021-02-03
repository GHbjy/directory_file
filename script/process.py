import os
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class FileProcess:
    def __init__(self, input_dir=None):
        if input_dir:
            self.dir = input_dir
        else:
            self.dir = "../test"
        self.directories = []  # save directories and files in the input directory

    def get_directory_info(self):
        """
        Get the input directory info.
        :return:
        """
        print('\n')
        logger.info("get the input directory info")
        tri_info = os.walk(top=self.dir, topdown=True)
        directory_info = os.listdir(self.dir)
        print('list directory info:', directory_info)

        logger.info("save info data list")
        self.directories.append(
            tri_info
        )

    def display_info(self):
        """
        Display Directories and Files in the input directory.
        :return:
        """
        print('\n')
        logger.info("display the input directory info")
        print('directories info:\n', self.directories)


if __name__ == "__main__":
    print('file process')
    fp = FileProcess(input_dir='./test')  # absolute path: 'D:/Projects/directory_file/test'  path: '../test'
    fp.get_directory_info()
    fp.display_info()
