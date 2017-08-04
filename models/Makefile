CLOUDY = /Users/Connor/Desktop/Research/cloudy/c17.00/source/cloudy.exe

SRC = $(wildcard ${name}*.in)
OBJ = $(SRC:.in=.out)

# Usage: make -j N name='NAME'
# N is the number of processors
# optional: NAME is a generic name, all models named NAME*.in will be run
# C. Morisset

all: $(OBJ)

%.out: %.in
	-$(CLOUDY) < $< > $@
# Notice the previous line has TAB in first column
