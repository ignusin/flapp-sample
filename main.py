import sys

from config import config
from webapp import app
    
def main(argv):
    app.run(host=config['dev']['host'], port=config['dev']['port'], debug=True)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
