import uvicorn
from fastapi import FastAPI

import config
from servers import serve_offer, serve_order

app = FastAPI(debug=config.DEBUG,
              title='PyTradingSystem',
              description='Python交易系统',
              version='0.1.0',
              on_startup=[serve_order, serve_offer])

if __name__ == '__main__':
    host, port = config.WEB_SERVER.split(':')
    uvicorn.run(app,
                host=host,
                port=int(port),
                loop='uvloop')
