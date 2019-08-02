
class Configuration(object):
    def __init__(self,
                host='0.0.0.0',
                port=5000,
                debug=True,
                db_uri='',
                track_mods=False):
        self.host = host
        self.port = port
        self.debug = debug
        self.db_uri = db_uri
        self.track_mods = track_mods

    def app_context(self):
        pass

    def create_app(self):
        pass

    def run_args(self):
        return dict(host=self.host,
                    port=self.port,
                    debug=self.debug)


if __name__ == '__main__':

    print('config = Configuration()')
    print('# for use in app.run()')
    print('app.run(**config.run_args())')
