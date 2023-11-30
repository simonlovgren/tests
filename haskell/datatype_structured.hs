data SteamProfile = SteamProfile {
		steamid :: Integer
		,	visibilityState :: Integer
		,	state :: Integer
		,	personaname :: String
		,	lastlogoff :: Integer
		,	profileUrl :: String
		,	avatar :: String
		,	avatarMedium :: String
		,	agatarFull :: String
		,	realName :: String
		,	timecreated :: Integer
		,	country	:: String
	} deriving (Show)