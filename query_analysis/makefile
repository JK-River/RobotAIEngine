# query_analysis deploy

GIT=git
CTL=supervisorctl -s unix:///tmp/query_analysis.supervisor.sock
PYTHON=python
START_PORT=8700
END_PORT=8700

start:
	for i in {${START_PORT}..${END_PORT}}; do ${CTL} start 'web:service-'$${i}; done

stop:
	for i in {${START_PORT}..${END_PORT}}; do ${CTL} stop 'web:service-'$${i}; done

restart:
	for i in {${START_PORT}..${END_PORT}}; do ${CTL} restart 'web:service-'$${i}; done

.PHONY: test
test:
	${PYTHON} ./test/unit_test.py

env:
	${GIT} pull

