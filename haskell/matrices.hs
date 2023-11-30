{-
	REPRESENTATION CONVENTION:
		* Represents a matrix and it's rows
			Matrix rows columns [rows]
		* A row is represented by
			Row [value]
		  where the value of every column is an element in the list
		* I represents the identity matrix 

	REPRESENTATION INVARIANT:
		* Matrix must contain at least one row and one column
		* All Rows in a Matrix must be of equal length
		* rows must be equal to the length of the list of rows
		* columns must be equal to the length of the list in a Row
-}
data Matrices a = Matrix Int Int [Matrices a] | Row [a] | I a deriving  (Show, Eq)


{-
	mScalar scalar matrix 

	PURPOSE:
		Multiply a scalar to a matrix

	PRE:
		* TRUE

	POST:
		* Returns the matrix with the scalar multiplied to every element

	EXAMPLES:
		mScalar 2 (Matrix 2 2 [Row [1,2], Row [2,1]]) == Matrix 2 2 [Row [2,4], Row [4,2]]
		mScalar 65 (I 1) == I 65

-}

mScalar :: Num a => a -> Matrices a -> Matrices a
mScalar s (I n) = I (s*n) -- Multiply with identity matrix

mScalar s (Matrix i j (r:rs)) = 
	let 
		mScalarRow s (r:rs) [] =

		mScalarCol s  =  
	in
		mScalarRow s r rs



mScalar s  = undefined




--- Defined matrices for tests ---
m1 = Matrix 2 2 [Row [1,2], Row [2,1]]