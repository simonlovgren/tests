#include "options.h"

Options::Options()
  : list()
{
  // TODO: Implement me
}

Options::~Options()
{
  // TODO: Implement me
  list.empty();  
}

int Options::Size() {
  return list.size();
}

void Options::Add(string name, bool _expect_value)
{
  // TODO: Implement me
  if(list.find(name) == list.end()) {
    // not in list
    list[name] = {false, _expect_value, NULL};
    return;
  }
}

int Options::Parse(int argc, char **argv)
{
  int status = 0;
  for(int i = 1; i < argc; ++i)
    {
      if(list.find(argv[i]) != list.end())
        {
          // Argument found
          list[argv[i]].set = true;
          if(list[argv[i]].expect_value)
            {
              // Value expected
              if(i != argc-1)
                {
                  list[argv[i]].value = argv[i+1];
                  ++i; // Skip value
                }
              else
                {
                  // Log missing value
                  status |= 0x2;
                }
            }
        }
      else
        {
          // Log unexpected argument
          status |= 0x1;
        }
    }
  return status;
}
  
const char *Options::Value(string name)
{
  if(list.find(name) != list.end())
    return list[name].value;
  return NULL;
}

bool Options::IsSet(string name) {
  // TODO: Implement me
  if(list.find(name) != list.end())
    return list[name].set;
  return false;
}
