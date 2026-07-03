# Git & GitHub for Two Absolute Beginners

A follow-along tutorial. You'll build a tiny Python game together and learn the real workflow two people use to share code without stepping on each other's toes.

Work through **Part 0 → Part 3** each on your own machines. From **Part 4** onward, one of you is **Person A** (created the project) and the other is **Person B** (joining it). Swap roles later so you both practice everything.

---

## Part 0 — What are these things? (2-minute mental model)

- **Git** is a program on *your computer*. It takes snapshots of your project so you can save progress, see what changed, and go back in time. Each snapshot is called a **commit**.
- **GitHub** is a *website* that stores a copy of your project online so you and your friend can share commits. Think of Git as the camera and GitHub as the shared photo album.
- A project folder that Git is tracking is called a **repository** (or **repo**).

The loop you'll repeat forever: **edit files → `add` them → `commit` a snapshot → `push` to GitHub**. Your friend then **pulls** your commits down.

---

## Part 1 — One-time setup (both of you)

### 1a. Install Git

- **Windows:** download from <https://git-scm.com/download/win>. Accept all the default options in the installer.
- **Mac:** open the Terminal app and type `git --version`. If Git isn't installed, macOS will offer to install it. (Or install [Homebrew](https://brew.sh) and run `brew install git`.)
- **Linux:** `sudo apt install git` (Debian/Ubuntu) or your distro's equivalent.

Check it worked. Open a terminal (Windows: search for "Git Bash", which the installer added) and run:

```bash
git --version
```

You should see a version number.

### 1b. Make a GitHub account

Both of you go to <https://github.com> and sign up. Pick a username you don't mind other people seeing.

### 1c. Tell Git who you are

This name and email get stamped on every commit. Run these two commands (use your own name and the email tied to your GitHub account):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

While we're here, set the default branch name to `main` (the modern standard) so your setup matches this tutorial:

```bash
git config --global init.defaultBranch main
```

### 1d. Log in so pushing works

> ⚠️ **Read this — it's the #1 thing that trips up beginners.** GitHub no longer accepts your account password from the command line. If you try to push and type your password, it will just fail. You need to log in *once* using the tool below, and after that everything "just works."

The easiest way is the **GitHub CLI**:

1. Install it from <https://cli.github.com> (Windows/Mac/Linux all supported; accept the defaults).
2. Run this and follow the prompts:

```bash
gh auth login
```

3. Choose **GitHub.com** → **HTTPS** → **Login with a web browser**. It shows you a short code, opens your browser, you paste the code, click authorize. Done.

That's it — the CLI now handles your credentials in the background, so `git push` and `git clone` will work without ever asking for a password again.

<details>
<summary><b>Alternative if you don't want the CLI (Personal Access Token)</b></summary>

Instead of a password, GitHub uses a **token** — a long random string. To create one: on GitHub, click your avatar → **Settings** → **Developer settings** → **Personal access tokens** → **Fine-grained tokens** → **Generate new token**. Give it repo read/write access and an expiry date. Copy the token somewhere safe (you only see it once). When Git asks for a "password" during a push, paste the **token** instead. Your system's credential manager will remember it after the first time.
</details>

---

## Part 2 — Solo basics: build the project (Person A does this)

**Person A**, make a folder for the project and go into it:

```bash
mkdir guessing-game
cd guessing-game
```

Turn this folder into a Git repository:

```bash
git init
```

Now create the game. Make a file called `main.py` with this content (use any text editor — VS Code, Notepad, whatever):

```python
import random

def play():
    secret = random.randint(1, 100)
    guesses = 0
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Your guess: "))
        guesses += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"You got it in {guesses} guesses!")
            break

if __name__ == "__main__":
    play()
```

Test that it runs (type `python main.py`, or `python3 main.py` on Mac/Linux, and play a round).

Now let's take your first snapshot. Check the status first — get in the habit of running this constantly, it tells you exactly where you stand:

```bash
git status
```

Git will say `main.py` is "untracked." Let's fix that. **Stage** the file (tell Git you want it in the next snapshot), then **commit** it (take the snapshot) with a message describing what you did:

```bash
git add main.py
git commit -m "Add number guessing game"
```

🎉 You just made your first commit. Run `git log` to see it (press `q` to exit that screen). Everything so far is still only on your computer.

> **The three states, in plain English:** a file you edited is *modified*. When you `git add` it, it's *staged* (on deck for the next commit). When you `git commit`, it becomes a permanent *snapshot*. `git status` shows you which state everything is in.

---

## Part 3 — Put it on GitHub (Person A)

1. Go to <https://github.com>, click the **+** in the top-right → **New repository**.
2. Name it `guessing-game`. Leave it **empty** — do *not* tick "Add a README" or add a .gitignore (you already have local files, and adding them here causes an annoying conflict for beginners).
3. Click **Create repository**.

GitHub now shows you a page with commands. Since you already have a repo with commits, use the **"…or push an existing repository"** section. It looks like this (GitHub fills in *your* username):

```bash
git remote add origin https://github.com/YOUR-USERNAME/guessing-game.git
git branch -M main
git push -u origin main
```

- `git remote add origin ...` saves GitHub's address under the nickname **origin**.
- `git push -u origin main` uploads your commits. The `-u` links your local `main` to GitHub's `main` so future pushes are just `git push`.

Refresh the GitHub page — your code is now online. **Person A, send Person B the repo URL** (the `https://github.com/YOUR-USERNAME/guessing-game` page).

### Add Person B as a collaborator

So Person B can push too: on the repo page, go to **Settings → Collaborators → Add people**, and enter Person B's GitHub username. Person B will get an email/notification to accept.

---

## Part 4 — Person B joins: clone the repo

**Person B**, once you've accepted the invite, go to a folder where you keep projects and **clone** (download a full copy of) the repo:

```bash
git clone https://github.com/PERSON-A-USERNAME/guessing-game.git
cd guessing-game
```

You now have the exact same project, full history and all. Run the game to confirm it works.

---

## Part 5 — The everyday loop: both of you make a change

Let's have **Person B** make the first change. Add a friendly title. Open `main.py` and add a line at the top of the `play()` function, right after `def play():`:

```python
    print("=== GUESS THE NUMBER ===")
```

Now the loop you'll do a thousand times:

```bash
git status                          # see what changed
git add main.py                     # stage it
git commit -m "Add game title"      # snapshot it
git push                            # send to GitHub
```

Refresh GitHub — Person B's change is there.

**Person A**, you don't have that change yet. Pull it down:

```bash
git pull
```

`git pull` fetches your friend's commits and merges them into your copy. Now you're back in sync.

> **Golden rule of two-person work:** `git pull` *before* you start working, and `git push` when you finish. This alone prevents most headaches.

---

## Part 6 — The professional workflow: branches & Pull Requests

Editing `main` directly is fine for two people messing around, but the real workflow uses **branches**. A branch is a parallel copy where you can experiment without affecting `main` until you're ready. Let's have **Person A** add a "play again" feature this way.

**Person A**, create and switch to a new branch:

```bash
git switch -c play-again
```

(`-c` means "create." To just switch to an existing branch, drop the `-c`.)

Edit `main.py`. Replace the whole bottom part (`if __name__ == "__main__":`) with a loop that offers another round:

```python
if __name__ == "__main__":
    again = "y"
    while again.lower() == "y":
        play()
        again = input("Play again? (y/n): ")
    print("Thanks for playing!")
```

Commit and push the **branch**:

```bash
git add main.py
git commit -m "Add play-again loop"
git push -u origin play-again
```

Now open a **Pull Request (PR)** — a request to merge your branch into `main`, where your friend can review it first:

1. Go to the repo on GitHub. You'll see a yellow banner: **"Compare & pull request."** Click it.
2. Write a short description of what you changed. Click **Create pull request**.

**Person B**, you're the reviewer. Open the PR on GitHub, click the **Files changed** tab to see exactly what's different (green = added, red = removed). If it looks good, go to the **Conversation** tab and click **Merge pull request** → **Confirm merge**. Optionally click **Delete branch** to tidy up.

The feature is now part of `main` on GitHub. **Both of you** update your local copies:

```bash
git switch main     # make sure you're on main
git pull            # grab the merged changes
```

That "branch → push → pull request → review → merge → pull" cycle is exactly how professional teams work. You just did it.

---

## Part 7 — Merge conflicts (the scary part, defused)

A **merge conflict** happens when both people change *the same line* differently, and Git can't decide which version wins. It looks alarming the first time but it's genuinely simple to fix. Let's cause one *on purpose* so it never surprises you.

**Both of you**, first make sure you're on an up-to-date `main`:

```bash
git switch main
git pull
```

Now:

- **Person A**: change the first print line inside `play()` to:
  ```python
      print("Welcome, human. Prepare to guess!")
  ```
  Then: `git add main.py` → `git commit -m "Change welcome (A)"` → `git push`

- **Person B**: change the *same* line to something *different*:
  ```python
      print("Hello friend! Let's play a guessing game.")
  ```
  Then: `git add main.py` → `git commit -m "Change welcome (B)"` → try `git push`

Whoever pushes **second** gets rejected with a message about the remote having changes you don't have. That's expected. That person runs:

```bash
git pull
```

Git announces a **CONFLICT** in `main.py`. Open the file — Git has inserted markers showing both versions:

```
<<<<<<< HEAD
    print("Hello friend! Let's play a guessing game.")
=======
    print("Welcome, human. Prepare to guess!")
>>>>>>> abc1234
```

To resolve it, **you** decide what the final line should be. Delete the marker lines (`<<<<<<<`, `=======`, `>>>>>>>`) and everything you *don't* want, leaving just the version you want to keep (or a brand-new combined line). For example, delete it all down to a single:

```python
    print("Welcome friend! Let's play a guessing game.")
```

Save the file, then tell Git the conflict is resolved and finish the merge:

```bash
git add main.py
git commit -m "Resolve welcome message conflict"
git push
```

Done. **The other person** runs `git pull` to get the resolved version. That's a merge conflict — no magic, you just pick the winning text and commit. Doing branches + PRs (Part 6) makes these rare, because you review before merging.

---

## Part 8 — Command cheat sheet

| Command | What it does |
|---|---|
| `git status` | Show what's changed / staged. **Run this constantly.** |
| `git add <file>` | Stage a file for the next commit (`git add .` stages everything) |
| `git commit -m "msg"` | Take a snapshot of staged changes |
| `git push` | Upload your commits to GitHub |
| `git pull` | Download and merge your friend's commits |
| `git clone <url>` | Download a repo for the first time |
| `git log --oneline` | See commit history, one line each (`q` to quit) |
| `git switch <branch>` | Move to another branch |
| `git switch -c <branch>` | Create a new branch and move to it |
| `git diff` | See exactly what you changed but haven't staged yet |

---

## Part 9 — When things go wrong

- **`fatal: not a git repository`** — you're not inside the project folder, or you forgot `git init`. `cd` into the right folder.
- **Push rejected / "updates were rejected"** — your friend pushed something you don't have. Run `git pull`, resolve any conflict, then `git push` again.
- **It's asking for a username & password and won't accept my password** — you skipped Part 1d. Run `gh auth login` (or use a token). Your account password never works here.
- **"Please tell me who you are"** — you skipped the `git config` commands in Part 1c.
- **Committed to the wrong branch / want to undo the last commit but keep the changes** — `git reset --soft HEAD~1` un-commits the last commit while leaving your file edits intact.
- **I'm scared I'll break everything** — you basically can't. Git keeps every snapshot; almost anything can be recovered. Experiment freely.

---

## What to do next

Once this clicks, try: each of you make branches for different features, open PRs, review each other's code, and practice pulling before you start. Ideas to extend the game: input validation (what if someone types "banana"?), a limited number of guesses, difficulty levels, or a high-score file. Each is a perfect excuse for another branch-and-PR cycle.

You've now done everything a small team does day-to-day. You're not stupid — you just hadn't been shown the loop yet. Now you have it.
