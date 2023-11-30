myDelete :: Ord a => a -> [a] -> [a]
myDelete _ [] = []
myDelete search (x:xs)
	|(x == search) = myDelete search xs
	| otherwise   = x : myDelete search xs