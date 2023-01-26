# make start arg='guessing-game'
start:
	python ${arg}/${arg}.py
# make venv // deactivate (to end venv)
env:
	source venv/bin/activate
