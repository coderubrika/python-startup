import xml.etree.ElementTree as ET
import os


def create_env_files():
    tree = ET.parse('.idea/workspace.xml')
    root = tree.getroot()

    for configuration in root.iter('configuration'):
        try:
            name = configuration.attrib['name']

            name = name.lower().replace(' ', '-')

            for env in configuration.iter('env'):
                if env.attrib['name'] == 'PY_ENV':
                    if not os.path.exists(f'env/{name}.env'):
                        with open(f'env/{name}.env', 'w'): pass


        except Exception:
            pass



def init(cfg):
    print('startup by "Init" mode')

    create_env_files()




