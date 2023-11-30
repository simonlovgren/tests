import Test.HUnit


myio :: IO String
myio = do
	return ("Lorem Ipsum")

assertEqualIO :: Eq a => a -> IO a -> Assertion
assertEqualIO base io = do
	ext <- io
	if (ext /= base) then
		assertFailure "Mismatch in IO"
	else
		return ()


test1 = TestCase $ assertBool "test1" (True)
test2 = TestCase $ assertEqualIO "Lorem Ipsum" myio 


tests = TestList [test1,test2]
runTests = runTestTT tests