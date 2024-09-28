from app import create_app

if __name__ == '__main__':
    api_server =create_app()
    api_server.run(host='0.0.0.0', port=5002)