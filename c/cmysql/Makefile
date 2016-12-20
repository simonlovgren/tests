CC = gcc
#CFLAGS = 

.PHONY: all

all: main

main: main.c bin
	$(CC) -o bin/$@ $(shell mysql_config --cflags) $< $(shell mysql_config --libs)

bin:
	@mkdir bin
