import enaml

from enaml.qt.qt_application import QtApplication


def main():
    with enaml.imports():
        from football_matchday_summarizer.view import Main
    app = QtApplication()
    view = Main()
    view.show()
    app.start()


if __name__ == '__main__':
    main()
