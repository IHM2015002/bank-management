import uvicorn
from bank import app

if __name__ == '__main__':
    uvicorn.run(app, port=8000, reload=False)
