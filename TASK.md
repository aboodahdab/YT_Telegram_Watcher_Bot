# Project: YouTube Watcher Bot

## What you're building

A program that watches your favorite YouTubers for you. You give it a list of channels. It runs on its own, and whenever one of them posts a new video, it sends you a message on Telegram with the link. You don't have to open YouTube or check anything — the program does the watching.

When it's finished, it should:

- Know a list of YouTube channels you care about
- Notice on its own when any of them posts something new
- Send that video's link to you on Telegram
- Never tell you about the same video twice
- Keep doing this forever, checking every so often
- Keep running even when your computer is off

That last one is the real goal. Anyone can write a script that runs once. You're building something that _stays alive_ and does a job in the background — like a real app.

---

## How to use this document

Every challenge and every concept below has a **question** with it. These aren't homework — they're how you check that you actually understand what you built instead of just pasting something that worked. Keep a file called `answers.md` next to your code and write your answer to each one _in your own words_. If you can't answer it, you don't understand that part yet — go back. Being able to explain it is the whole point.

---

## The challenges

Don't think of this as one big program. Think of it as a series of walls to climb. Beat them one at a time, in this order. Each one works on its own before you move to the next.

**1. See the latest video.**
Get your program to find the most recent video from _one_ channel you pick. Just print it to the screen for now.

> **Answer this:** Which method did you use to get the video — the official API or the simpler feed? Why did you pick it? What did the one you _didn't_ pick cost you?
> **And this:** What format did the data come back in? How is it different from JSON, which you already know?

**2. Send yourself a message.**
Separately, get your program to send _you_ a message on Telegram. Any message. "hello" is fine. Just prove you can make a message appear on your phone from code.

> **Answer this:** Besides the text of the message, what _two_ other things does Telegram need before it will send anything? What is each one, and where did you get it?

**3. Wire them together.**
Now combine 1 and 2: your program finds the latest video and sends _that_ to your Telegram.

> **Answer this:** The feed gave you some info about the video. How did you turn that into a link a human can actually click? What did you have to build yourself?

**4. Don't repeat yourself.**
Right now, every time you run it, it'll send you the same video again. Fix that. Your program should only message you about a video it _hasn't_ sent before.

> **Answer this:** What exactly does your program need to _remember_ to know whether a video is new?
> **And this:** Where does that memory live when the program is closed? Why can't it just be a normal variable in your code?
> **And this:** If you deleted that memory, what would happen the next time it ran?

**5. Watch many channels, forever.**
Make it handle a whole list of channels, not just one. And make it check again on its own every 15 minutes, without you restarting it.

> **Answer this:** When you have many channels, does each one need its own separate memory, or can they all share one? Why?
> **And this:** What is `time.sleep` actually doing to your program during those 15 minutes — is it working, or not?

**6. Set it free.**
Get it running somewhere that isn't your laptop, so it keeps working when your computer is off.

> **Answer this:** Why does closing your laptop kill the bot right now? What's different about the place you deployed it to?
> **And this:** Why did you choose a "background worker" and not a "web service"? What does each one assume your program is?

If you get challenges 1–4 done in one sitting, you're doing great. Challenge 6 is the hardest and the most impressive — that's where it stops being a script and becomes a real thing.

---

## Things to look into

Here are the topics and tools you'll need. I'm giving you the _names_, not how to use them — finding out how is your job. Search them, read their docs, experiment. Each one has a question to answer once you've figured it out.

**Finding new videos**

- There's an official _YouTube Data API_. There's also a simpler _feed_ of a channel's recent videos that needs no signup. Look into both, then choose.
- Whatever you pick returns data in some format your program has to read. Find out what format and how Python reads it.
- A channel has a hidden _channel ID_ starting with `UC`. It is **not** the `@name` in the URL. Figure out how to find a channel's real ID. _(Genuinely annoying — okay to look this up.)_
  > **Answer this:** In one sentence each — what does the API give you that the feed doesn't, and what does the feed save you that the API doesn't?

**Sending messages**

- _Telegram bots_ — how do you make one? Look up _BotFather_.
- Once you have a bot, how does your program tell it to send a message, and who does it send to?
  > **Answer this:** Your bot has a _token_ and you have a _chat ID_. What is each one for? What would go wrong if you mixed them up?

**Remembering things**

- When your program closes and reopens, it forgets everything. You already know how to read and write files — that's your tool. The hard part is deciding _what_ to store.
  > **Answer this:** Describe, in words, exactly what you save to the file and what shape it's in. Why that shape and not something simpler?

**Running forever**

- How do you make a program pause before repeating? Look into `time.sleep`.
- How do you keep a program running 24/7 without your own computer? Look into _Railway_ or _Render_, and the difference between a "web service" and a "background worker." _(Okay to look this up — it's unguessable.)_
  > **Answer this:** What's the difference between your program _running_ and your program being _deployed_? Why isn't running it on your laptop enough?

**Habits worth picking up now**

- Your bot has a secret token. If your code ever goes on the internet (GitHub), that token must **not** be visible in it. Look into `.env` files.
- Look into _git_ and _GitHub_ — a way to save versions and undo mistakes.
  > **Answer this:** If someone got your bot token, what could they actually do with it? Now explain why hardcoding it into your file is risky.
  > **And this:** What does git let you do that just saving the file normally doesn't?

---

## The rules

- **Struggle first, search second.** When you're stuck, sit with it and think before looking it up. But if you've been stuck 30 minutes and you're frustrated, searching is smart. The goal is to _not quit_ — not to suffer.
- **Read the error.** When something breaks, the error tells you the file, the line, and often the reason. Read it before doing anything else. This one habit is the whole difference between fixing things yourself and being stuck forever.
- **Type it, don't paste it.** When you find code online, type it out. You learn nothing from pasting.
- **Make it work, then make it better.** Get the ugly version running first. Don't make it clean or clever until it runs at all.
- **Answer the questions honestly.** If your answer is "it just worked, I don't know why," that's your signal to go back. That question is pointing at a hole in what you understand.

---

## Also worth knowing

- **The first run will spam you.** The first time it works, it'll message you every channel's latest video at once. That's expected — figuring out how to handle it is a good puzzle, not a mistake.
- **The feed only shows recent videos** and can lag a few minutes behind an upload. Fine for this — it doesn't need to be instant.
- **Free hosting can be weird.** Free plans sometimes pause your app. Part of the challenge is reading their docs to keep yours running.
- **This is never "done."** Once it works, keep adding: better message formatting, adding channels by texting the bot, watching for livestreams, whatever you want. That's the fun part.
