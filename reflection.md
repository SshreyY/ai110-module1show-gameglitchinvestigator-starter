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
  - for me, it was by going to the website and checking to see if it was really fixed or not and then
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
