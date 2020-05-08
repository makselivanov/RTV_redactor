CXX = g++
#flags for compile files
FLAGS =
#flags for link objects files
LFLAGS = -shared
DEBUGFLAGS = -O0 -D _DEBUG
RELEASEFLAGS = -03 -D NDEBUG

TARGET_LIB = rtv_figures.pyd
SRCDIR = src
SOURCES = $(wildcard $(SRCDIR)/*.cpp)
INCDIR = include
OBJDIR = obj
OBJECTS = $(patsubst $(SRCDIR)/%.cpp,$(OBJDIR)/%.o,$(SOURCES))

PHONY += all
all: $(TARGET_LIB)

$(TARGET_LIB): $(OBJECTS)
	$(CXX) $(OBJECTS) -o $(TARGET_LIB) $(LDFLAGS)

$(OBJDIR)/%.o: $(SRCDIR)/%.cpp | $(OBJDIR)
	$(CXX) $(FLAGS) $(RELEASEFLAGS) -c -MMD -o $@ $<

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

