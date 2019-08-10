
import pyodbc


def show_odbc_sources():
	sources = pyodbc.dataSources()
	dsns = sources.keys()
	dsns.sort()
	sl = []
	for dsn in dsns:
		sl.append('%s [%s]' % (dsn, sources[dsn]))
	print('\n'.join(sl))


if __name__ == '__main__':
	show_odbc_sources()
