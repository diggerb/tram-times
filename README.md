# tram-times

Google Assistant asks WayScript to run tram-times.py. The resulting times are saved as strangely named variables and following some simple logic (to ensure the correct number of times are read out to the user), the times get read out. 

To update the script for yourself ideally you'd use your own cookie (I think a cookie ID is required for the request to be processed) You can find this by digging through the header information in the GET requests in the network monitor on your web browser on the following page for example, https://www.robinhoodnetwork.co.uk/stops/9400ZZNOMID2. 

You also need to find the ID for the correct tram stop. eg: https://www.robinhoodnetwork.co.uk/explore?marker=Middle%20Street%20Tram%20Stop&center=52.92783%2C-1.209046&type=stop&id=9400ZZNOMID2 is the away-from-city bound stop at Middle Street. However because the API is incorrectly built, this ID (9400ZZNOMID2) would return the in-to-city bound live tram times.
