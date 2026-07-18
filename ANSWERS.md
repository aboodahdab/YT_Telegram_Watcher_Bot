# Answers for TASK.md steps.
## Step 1:
## "Which method did you use to get the video": 
### I used two apis from youtube first is channels api to get the content creator's UPLOAD PLAYLIST then I used the playlistItems api endpoint to get videos inside it (I used the official API)
## "Why did you pick it":
### cuz It's the official also there was another way using search api (still from offical api of youtube) but I did NOT use that becuase that would search results and get you the uploads by searching NOT by going inside the playlist.
## "What did the one you didn't pick cost you":
### (I don't know) They are basically the same BUT the only difference is quota spending (the currency of google api that if you finished it you can't call any api of theirs)
## "What format did the data come back in": 
### It came in json.
## "How is it different from JSON, which you already know":
### 0 out of 10 (brother it's json), bruh 
# Step 2:
## "Besides the text of the message, what two other things does Telegram need before it will send anything?":
### Telegram needs a TOKEN and CHAT ID before sending anything.
## What is each one, and where did you get it?":
### They are needed because the token makes Telegram now that this is YOUR bot and the chat id is used because telegram needs to know where to send this message. I got the token when I created the bot and I got the chat id from ```https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates```.
# Step 3: 
## "The feed gave you some info about the video. How did you turn that into a link a human can actually click? What did you have to build yourself?" 
### The playlist items api I used returned the video's id like this "I5-dI74zxPg" 
### and then I added it to a ```https://www.youtube.com/watch?v=``` so it became a clickable link.
# Step 4:
## "What exactly does your program need to remember to know whether a video is new? And this: Where does that memory live when the program is closed?"
### It needs to remember it's ID.
## "Why can't it just be a normal variable in your code?"
### Cuz it will just get deleted everytime the code finishes (cuz this way it will live in ram NOT storage).
## "If you deleted that memory, what would happen the next time it ran?"
### If you delete it it will just run again and give you the same video repeatedly.
# Step 5:
## "When you have many channels, does each one need its own separate memory, or can they all share one? Why?":
### They can share one memory because all the video IDs are stored in a .txt file ```storageFile.txt```. Becasue I'm using a file to store video IDs .
## "What is time.sleep actually doing to your program during those 15 minutes — is it working, or not?"
### It's just stopping the program from doing anything (literally sleeping). then when the time finishes (15 mins) it will start running the code.
# Step 6:
## "Why does closing your laptop kill the bot right now?":
### Cuz when I close my laptop I close ALL running things (apps, scripts, os .etc) so everything will get automatically closed.
## "What's different about the place you deployed it to?":
### I deployed the script to an EC2 aws python server and the different part is that it's running 24/7 so It does not get closed and even if it get's closed you can program it to automatically run the script again.
## "Why did you choose a "background worker" and not a "web service"?":
### because a web service is used when your script needs someone to call it or do something so it can reply to it
### BUT a background worker works all day even if now one called it.It's even seen in the name LOL.
## "What does each one assume your program is?": 
### A background worker assumes that my program is something that needs to be working all day and it does not need anyone to trigger it 
### (for example call an api,send a message,or even trigger something like an alert)
### but a web service assumes that my program is something that needs someone to call it to return value, like an API endpoint handler
