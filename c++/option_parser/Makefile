CXX=g++
CXX_FLAGS=-Wall
LXX_FLAGS=


all: opttest

opttest: main.cc options.o
	$(CXX) $(CXX_FLAGS) -o $@ $^ $(LXX_FLAGS)

options.o: options.cc options.h
	$(CXX) $(CXX_FLAGS) -c -o $@ $< $(LXX_FLAGS)

clean:
	rm -f options.o opttest
