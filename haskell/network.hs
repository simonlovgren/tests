module SteamAPI () where

import Network.HTTP
import Data.List

-- Data types --
type SteamID = [Char]
type AppID = [Char]

-- BASE SETTINGS --
key 	= "YOUR_KEY_HERE"
apiBase = "http://api.steampowered.com"

-- Core functionality --
get :: String -> IO String
get url = do
	resp <- simpleHTTP (getRequest url)
	getResponseBody resp

code :: String -> IO ResponseCode
code url = do
	resp <- simpleHTTP (getRequest url)
	getResponseCode resp



-- Specific API calls --
-- IPlayerService -- PLAYERINFO --
getPlayerSummaries :: [SteamID] -> IO String
getPlayerSummaries ids = do
	let url = apiBase ++ "/ISteamUser/GetPlayerSummaries/v0002/?key=" ++ key ++ "&steamids=" ++ (intercalate "," ids)
	resp <- simpleHTTP (getRequest url)
	getResponseBody resp

getFriendList :: SteamID -> IO String
getFriendList id = do
	let url = apiBase ++ "/ISteamUser/GetFriendList/v0001/?key=" ++ key ++ "&relationship=friend&steamid=" ++ id
	resp <- simpleHTTP (getRequest url)
	getResponseBody resp

getOwnedGames :: SteamID -> IO String
getOwnedGames id = do
	let url = apiBase ++ "/IPlayerService/GetOwnedGames/v0001/?key=" ++ key ++ "&steamid=" ++ id
	resp <- simpleHTTP (getRequest url)
	getResponseBody resp

getPlayerAchievements :: SteamID -> AppID -> IO String
getPlayerAchievements id appid = do
	let url = apiBase ++ "/ISteamUserStats/GetPlayerAchievements/v0001/?key=" ++ key ++ "&appid=" ++ appid ++ "&steamid=" ++ id
	resp <- simpleHTTP (getRequest url)
	getResponseBody resp

getUserStatsForGame :: SteamID -> AppID -> IO String
getUserStatsForGame id appid = do
	let url = apiBase ++ "/ISteamUserStats/GetUserStatsForGame/v0002/?key=" ++ key ++ "&appid=" ++ appid ++ "&steamid=" ++ id
	resp <- simpleHTTP (getRequest url)
	getResponseBody resp

getRecentlyPlayedGames :: SteamID -> IO String
getRecentlyPlayedGames id = do
	let url = apiBase ++ "/IPlayerService/GetRecentlyPlayedGames/v0001/?key=" ++ key ++ "&steamid=" ++ id
	resp <- simpleHTTP (getRequest url)
	getResponseBody resp

getPlayerBans :: [SteamID] -> IO String
getPlayerBans ids = do
	let url = apiBase ++ "/ISteamUser/GetPlayerBans/v1/?key=" ++ key ++ "&steamids=" ++ (intercalate "," ids)
	resp <- simpleHTTP (getRequest url)
	getResponseBody resp


-- ISteamApps -- App Info --
getSteamApps :: IO String
getSteamApps = do
	let url = apiBase ++ "/ISteamApps/GetAppList/v2"
	resp <- simpleHTTP (getRequest url)
	getResponseBody resp