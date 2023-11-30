myhead :: [a] -> a
myhead [] = error "Not a populated list."
myhead (x:_) = x

trd :: [a] -> a
trd [] = error "Not a populated list."
trd (_:_:x:_) = x