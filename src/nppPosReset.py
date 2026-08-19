"""
A small tiny application resetting the start position of the
Notepad++ application to a position always reachable on the screen
"""
import os
import re


def npp_pos_reset():
    """
    Resets the start position ot x=10, y=10
    :return: na
    """

    # build the fully qualfied path to the config.xml file
    homedrive = os.getenv("HOMEDRIVE")
    homepath = os.getenv("HOMEPATH")

    path_name_config = os.path.join(homedrive,
                                    homepath,
                                    'AppData',
                                    'Roaming',
                                    'Notepad++',
                                    'config.xml')

    # open file, read text
    config_file = open(path_name_config, 'r+', encoding='utf-8')
    config_text = config_file.read()

    # replace the position info
    config_text = re.sub(r'"AppPosition" x="-?\d*" y="-?\d*"',
                         '"AppPosition" x="10" y="10"'
                         , config_text)

    # write the text back to the file
    config_file.seek(0)  # Got to start of file
    config_file.truncate()  # Delete all content
    config_file.write(config_text)
    config_file.close()


if __name__ == '__main__':
    npp_pos_reset()
