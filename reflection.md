# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  - Whenever I guessed it, it always gave me feedback saying that guess lower and then I entered 1 to see if it would say go higher but it said go lower, so immediately knew that this game is broken. Vice versa, when I guessed 99, it told me to go higher, so that was broken. the correct hint providing is broken in general, its very misleading.
  - the new game button seems to broken because once I run out of attempts and click on new game button to refresh, it doesn't start a new game.
  - when I switched to Hard difficulty, the sidebar said the range was 1 to 50, but the info box above the input still said "Guess a number between 1 and 100." I didn't know which one to actually trust, so I just guessed numbers above 50 and nothing happened differently, which made it obvious the difficulty range wasn't actually being applied to the game instructions.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used Claude Code to help me on this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - So in phase 1 or section 1 of the file, it had asked me to find two issues by playing the game, so I found the two issues but then on the courses page, it said to find at least three bugs. So I aksed the AI to find another bug for me that I might have missed or overlooked, and it correctly identified the issue with range now updating depending on the difficulty chosen, meaning it wasn;t affecting the guesses because it kept taking the guesses between 1 and 100 when on the hard difficulty it was between 1 and 50. So, it identified that bug and also another bug where the range of the hard difficulity should have been more than between 1 and 50, so it identified that and increased the difficulty range to between 1 and 200.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - When I wanted it to generate some test for me, it just assumed that pytest would work for me in the terminal but it didn't due to a path issue. So it didn't clearly think about it and it should've ran the test after creatin the test in the terminal that it always automaitcally tests commands in, so why didn't it do it this to fix the bug before I noticed was a bit misleading. Aside from the issues, the most important thing is that it fixed all the issues correctly and provided correct suggestions. So it wasn't incorrect or misleading in terms of the solutions it provided.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - for me, it was by going to the website and checking to see if it was really fixed or not. Like for the hint bug, I would guess a number I knew was lower than the secret and check if it actually said "go higher" now. If it did, I knew the fix worked. Then I also ran pytest to double check that the logic held up beyond just what I could see on the screen.
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
  - I ran the test file using pytest and one of the tests that really stood out was `test_hard_range_is_larger_than_normal`, which basically checks that the hard difficulty range is actually bigger than normal. Before the fix, hard was 1 to 50 and normal was 1 to 100, so that test would have failed, which proved the bug was real. After the fix I bumped hard to 1 to 200 and the test passed, so that confirmed the change was correct. The range tests for easy and normal also passed, which gave me confidence I didn't accidentally break anything else.
- Did AI help you design or understand any tests? How?
  - Yeah, AI helped me write most of the pytest tests since I wasn't super familiar with how to structure them. It suggested breaking the tests into groups by function, so one group for `check_guess`, one for `get_range_for_difficulty`, one for `parse_guess`, and one for `update_score`. That structure made it way easier to figure out which part of the code was broken when something failed.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - The original code had `secret = random.randint(low, high)` just sitting at the top of the script with no protection around it. So every single time you clicked a button or typed something, Streamlit would rerun the entire script from top to bottom, which meant it kept calling `random.randint` again and generating a brand new secret number. So every guess was basically against a moving target, which is why the hints never made sense.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Basically, every time you do anything on the page like click a button, type in a box, anything. Streamlit doesn't just update that one part, it reruns your entire Python file from scratch. So if you have a variable like `score = 0` just sitting there, it resets to 0 every single time. Session state is like a little backpack that survives those reruns. You store things in `st.session_state` and they stick around across reruns, so your score, your secret number, your attempts, they all stay in place.
- What change did you make that finally gave the game a stable secret number?
  - The fix was wrapping the secret generation in an `if "secret" not in st.session_state` check. So now it only generates the random number once. The very first time the app loads, and then just keeps using that same number for the whole game. Every rerun after that just skips over that block entirely.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - I want to keep the habit of playing through the app manually before I trust any fix. Like actually going through the game as a real user would, trying edge cases, not just running it once and assuming it works. That's what caught most of the bugs here in the first place, and it paired really well with having the pytest tests as a second layer of confirmation.
- What is one thing you would do differently next time you work with AI on a coding task?
  - I would actually test the AI's suggestions in the terminal before accepting them as done. Like with the pytest situation, the AI assumed it would just work without checking if the path or environment was set up correctly. Next time I'd ask the AI to also verify the command runs successfully, not just write the code and assume everything is fine.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - Before this I kind of assumed that if AI wrote code and it looked right, it probably was right. Now I see that AI can write code that looks totally clean and professional but has subtle logic bugs baked right in, like the secret number regenerating on every rerun or the hints being backwards, so I can't just read it and approve it. I have to actually read through what it wrote and if anything seems like its a work around or not best approach, then I would ask it to rework it.
