INCLUDES = -I .

.PHONY: clean test

cfunctions.so: cfunctions.c
	$(CC) -g3 -fPIC -shared $(INCLUDES) -o $@ $^ -lm

test: cfunctions.so
	python3 -m pytest -v .

clean:
	rm -r cfunctions.so __pycache__ .pytest_cache