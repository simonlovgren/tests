
data Status = Green | Red deriving (Show)
data Tree = Void | Node Status Int Tree Tree deriving (Show)


insert :: Int -> Tree -> Tree
insert v Void = Node Green v Void Void
insert v (Node s vt l r) 	| v > vt	= Node s vt l (insert v r)
							| v < vt	= Node s vt (insert v l) r
							| v == vt	= Node s vt l r


balance :: Tree -> Tree