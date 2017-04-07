#include <iostream>

#include "options.h"

int main(int argc, char *argv[])
{

  // Set up options
  Options options;
  options.Add("-o", true);
  options.Add("--out", true);
  options.Add("-v");
  options.Add("--verbose");
  if(options.Parse(argc, argv))
    {
      std::cout << "usage:  opttest [-o|--out|-v|--verbose]\n";
      return 1;
    }
  
  
  std::cout << "Hello World!\n\n";
  std::cout << "# Available options: " << options.Size() << "\n";
  std::cout << "Arguments set:\n";
  if(options.IsSet("-o"))
    {
    std::cout << "-o " << options.Value("-o") << "\n";
    }
  if(options.IsSet("--out"))
    {
      std::cout << "--out ";
      if(options.Value("--out"))
        std::cout << options.Value("--out");
      std::cout << "\n";
    }
  if(options.IsSet("-v"))
    std::cout << "-v " << "\n";
  if(options.IsSet("--verbose"))
    std::cout << "-verbose " << "\n";

  return 0;
}
