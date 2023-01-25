# make start arg='guessing-game'
start:
	python ${arg}/${arg}.py
# make venv // deactivate (to end venv)
venv:
	source venv/bin/activate
