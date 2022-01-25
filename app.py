import os
__version__ = '0.1'
from public import app
from module.instances import Instances


if __name__ == '__main__':
    try:
        Instances.load_instaces()
    except Exception as e:
        print(f"unable lunch service. {e}") 
        exit(1)
    port = int(os.environ.get("PORT", 8080))
    app.run('0.0.0.0', port=port)