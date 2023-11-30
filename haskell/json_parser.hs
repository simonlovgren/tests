module JSON where

import Debug.Trace

data JSON a = JObject [(String, JSON a)] | JOArray [JSON a] | JArray [a] | JVar String a | Empty deriving (Show) 

{-
	jsonData = "{\"name\" : \"Simon\",\"Array\" : [123,456,789],\"embedded_object\" : {\"embedded_object\" : {\"gameName\" :  \"FallOut 3\"}}"


	this json-data should evaluate to:
		JObject "main" [JVar "name" "Simon", JVar "Array" (JArray [123,456,789]), JVar "embedded_object" (JObject [JVar "gameName" "FallOut 3"])]


-}

jsonData = "{\"name\" : \"Simon\",\"Array\" : [123,456,789],\"embedded_object\" : {\"embedded_object\" : {\"gameName\" :  \"FallOut 3\"}}"


{-
parseJson :: String -> JSON a
parseJson ('{':xs) = parseObject xs
parseJson ('[':xs) = parseArray xs
parseJson [] = Empty

parseObject :: String -> JSON a
parseObject ('"':xs) = JObject (parseString xs) [Empty]
parseObject (x:xs) = parseObject xs
parseObject [] = Empty

parseArray :: String -> JSON a
parseArray x = undefined

parseString :: String -> String
parseString ('"':xs) = []
parseString (x:xs) = x : parseString xs
-}

-- parseJsonVar :: String -> [Char]
-- parseJsonVar (x:xs) = 