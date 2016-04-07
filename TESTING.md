# Part 3 - Testing

### Who:
Joshua Zepf  
Devon Jones  
Griffin Smith  
Harry Hinch  
Landon Ledbetter

### Title: 
WanderMap

### Vision Statement:
We want to make a map to visualize the most interesting locations on the planet.

## Automated Tests:
[Todo: figure out what we can automate...]

## User Acceptance Tests:
      | UC-01
----- | -----
Use Case Name: | Clickable Marker
Description | User can find a marker by scrolling on google maps and click on it. Doing so will bring up a photo of the location as well as the title of and link to the reddit post.
Users: | Guests to the website (no logins)
Pre-conditions | Marker data must be loaded to the google maps javascript API.
Post-conditions | The bootstrap modal must become visible to the user, and it must show the correct image and title.
Flow of events: | 1. __Action__: User finds a marker on the map <br /> 2. __Action__: User clicks on the marker. __System response__: Show the modal.
Test/Pass? | Pass / Fail
Notes and Issues |  

      | UC-02
----- | -----
Use Case Name: | Search Bar
Description | User can click "Search.." and type in a location. They will find posts from the subreddit that are nearby to the place that they searched.
Users: | Guests to the website (no logins)
Pre-conditions | Latitude and Longitude of the markers should be known in the database.
Post-conditions | A variable number of markers should be added to the map depending on the location that the user searched. These markers should all be nearby a certain latitude + longitude.
Flow of events: | 1. __Action__: User clicks 'Search...' on the navbar. <br /> 2. __Action__: User types a location and presses the search button. __System response__: Google Maps Geocode API call is made to determine the latitude and longitude of the user's search location. Compare these coordinates and find all markers within a certain distance to the user's coordinates. These markers are displayed on the map.
Test/Pass? | Pass / Fail
Notes and Issues |  

      | UC-03
----- | -----
Use Case Name: | Top 50
Description | User can click "Show me.." and then click "Top 50". This will grab the Top 50 posts from the subreddit and push their data into to markers for them to explore.
Users: | Guests to the website (no logins)
Pre-conditions | Redditbot must be running.
Post-conditions | 50 Markers will be created and displayed on the map corresponding to the top 50 on the subreddit.
Flow of events: | 1. __Action__: User clicks 'Show me..' on the navbar. <br /> 2. __Action__: User clicks on 'Top 50' in the dropdown menu. __System response__: Redditbot will grab the top 50 posts from the subreddit. Google Maps Geocode API calls will be used to find latitude and longitude of each picture's title. Only 50 markers will be added to the map, corresponding to each post.
Test/Pass? | Pass / Fail
Notes and Issues |  
