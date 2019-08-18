import enaml
from enaml.qt.qt_application import QtApplication


def main():
    import pdb; pdb.set_trace()
    with enaml.imports():
        from football_matchday_summarizer import view
    app = QtApplication()
    view = view.Main()
    view.show()
    app.start()


if __name__ == '__main__':
    main()
