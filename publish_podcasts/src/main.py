from publish_podcasts.src.produser import Manager

manager = Manager()

def main():
    manager.publish_messages('podcasts')

if __name__ == '__main__':
    main()