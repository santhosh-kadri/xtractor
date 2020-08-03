import scraper
import importlib
import subprocess
import sys
from core.xtractor import BaseExtractor
from scraper.mc_scraper import MoneyControl
from requests.exceptions import ProxyError

sys.path.append(scraper.__path__)
print(scraper.__path__)

scraper_dict = {'money_control': (MoneyControl, ())

}
def main():
    print(sys.argv)
    # # subprocess.run(['python3.7', f'{scraper.__path__[0]}/mc_scraper.py'])
    package = importlib.import_module(f'{scraper.__package__}.{sys.argv[1]}')
    for class_name in dir(package):
        if class_name.startswith('__') or class_name in ['BaseExtractor', 'sys']:
            continue
        scraper_obj = getattr(package, class_name)
        obj = scraper_obj()
        if isinstance(obj, BaseExtractor):
            try:
                obj.run()
            except ProxyError:
                obj.run()


if __name__ == '__main__':
    main()



