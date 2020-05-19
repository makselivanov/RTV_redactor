CXX = g++
#flags for compile files
FLAGS =
#flags for link objects files
LFLAGS = -shared -lboost_python -lboost_system
DEBUGFLAGS = -O0 -D _DEBUG
RELEASEFLAGS = -O3 -D NDEBUG

TARGET_LIB = rtv_figures.pyd
SRCDIR = src
SOURCES = $(wildcard $(SRCDIR)/*.cpp)
INCDIR = -Iinclude -I/usr/include/python3.6m
OBJDIR = obj
OBJECTS = $(patsubst $(SRCDIR)/%.cpp,$(OBJDIR)/%.o,$(SOURCES))

PHONY += all

all: $(TARGET_LIB)

$(TARGET_LIB): $(OBJECTS)
	echo $(PY_VERSION_HEX)
	$(CXX) $(OBJECTS) -o $(TARGET_LIB) $(LFLAGS)

$(OBJDIR)/%.o: $(SRCDIR)/%.cpp | $(OBJDIR)
	$(CXX) -fPIC $(FLAGS) $(RELEASEFLAGS) -c -MMD -o $@ $< $(INCDIR)

$(OBJDIR):
	mkdir -p $(OBJDIR)

PHONY += test
test: $(TARGET_LIB)_test

$(TARGET_LIB)_test:
	:

PHONY += clear
clear:
	rm -rf $(OBJDIR) $(TARGET_LIB)


.PHONY: $(PHONY)

