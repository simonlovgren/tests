#include <string>
#include <iterator>
#include <map>

#ifndef _OPTIONS_H
#define _OPTIONS_H

using namespace std;

class Options {
 public:
  Options();
  ~Options();

  int Size();

  /**
   * Add option to option parser.
   *
   * @param name            Name of flag with - or --   (ex. '-o' or '--out')
   * @param expect_value    Expect value to be paired with option (ex. -o myfile.txt)
   *
   * Example:
   *   myOptions.Add("--out", true);
   */
  void Add(string name, bool expect_value = false);

  /**
   * Parse argument list
   * 
   * @param argc  number of arguments in list
   * @param argv  list of arguments
   *
   * @return 0 if OK
   */
  int Parse(int argc, char **argv);
  
  /**
   * Get supplied value for option.
   *
   * @param name   Name of flag with - or --   (ex. '-o' or '--out')
   *
   * @return  Pointer to value in argument list, NULL if no argument supplied.
   */
  const char *Value(string name);

  /**
   * Check if a flag is present in arguments
   * @param name   Name of flag with - or --   (ex. '-o' or '--out')
   *
   * Example:
   *   if(myOptions.IsSet('-o'))
   *       filename = myOptions.Value('-o');
   */
  bool IsSet(string name);

 private:
  typedef struct {
    bool set;
    bool expect_value;
    char *value;
  } Option;
  
  map <string, Option> list;
  
};

#endif
