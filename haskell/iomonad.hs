
echo :: [[char]]
echo =
  do
    line <- getLine
    case line of "" -> []
                 l -> l : echo
