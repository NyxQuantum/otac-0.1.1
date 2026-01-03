.PHONY: install test demo clean

install:
	python3 -m pip install -r requirements.txt

test:
	python3 -m pytest tests/ -q

demo:
	@echo "=== OTAC 0.1.1 – demo 15 s ==="
	@python3 tools/verify_standalone.py examples/genesis.json

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
