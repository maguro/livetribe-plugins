from livetribe.plugins import Factory


class MockFactory(Factory):
    def Z(self):
        print 'MOCK'