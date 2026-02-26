# Nick's Tech Career Transformation Plan
## (Updated Feb 2026 — Full Roadmap Integration)

## Who This Plan Is For
**Nicholas (Nick)** — 21, Software Engineering student at Zetech University (3rd year, 1st sem).
Diploma in Business Information Technology. Currently on a break until May.
Goal: Stop being a "prompter", actually learn to code, build a portfolio, find a niche, and enter the job market confidently.

---

## The Core Problem (Be Honest With Yourself)
You are not bad at coding. You have never actually *learned* coding — you've been *generating* it.
There is a difference between understanding a system and being able to prompt one into existence.
The fix is not to stop using AI. The fix is to **change your relationship with AI**:
- Old way: "AI, write this for me" → copy → submit
- New way: "I'll write this myself" → AI reviews it → you understand the feedback

---

## Niche Recommendation: Full-Stack Web Developer (Python-first)

### Why this niche for YOU specifically:
1. **You already know Python, HTML, CSS, MySQL** — you're not starting from zero
2. **Your Business IT diploma** gives you real-world context most devs lack (you can build things that actually solve business problems)
3. **Your vibecoded school automation app** shows you naturally think in automation — that's a developer's instinct
4. **Full-stack web dev** is the highest-demand, highest-freelance-opportunity niche in the Kenyan and remote job market
5. **Python is the gateway** to AI/ML, data, automation, and backend — keeping all your other interests open

This does NOT close the door on ML, security, or mobile. It gives you a **landing pad** to build real projects, get paid, and then specialize further.

---

## The Non-Negotiable Rules (Anti-AI-Crutch Protocol)

Before anything else, internalize these rules. Break them consciously and you sabotage your own plan:

1. **Write code first, ask AI second.** Always attempt the problem yourself for at least 20-30 minutes before touching Copilot/ChatGPT.
2. **Never paste code you can't explain line by line.** If you can't explain it, delete it and rewrite it until you can.
3. **Use AI like a senior dev, not a vending machine.** Ask "Why does this work?" not "Give me the code."
4. **Read the error message yourself first.** Before asking AI, spend 5 minutes with the error. Google it. Try to fix it. Then ask.
5. **Comment your own code before AI reviews it.** Writing comments forces you to understand what you wrote.
6. **Rebuild before you refactor.** Take your vibecoded school app and rebuild it from scratch — understanding every line. This is your first real project.

---

---

## Roadmap Overview — Priority Order for Your Niche

You have 9 roadmaps. Here's exactly when and how each one feeds into your journey:

| Roadmap | Phase | What to Extract From It |
|---------|-------|--------------------------|
| `python.pdf` | Phase 1 | Basics → OOP → DSA → Flask/Django → Testing |
| `computer-science.pdf` | Phase 1-2 | DS&A, Big O, Algorithms, Design Patterns |
| `datastructures-and-algorithms.pdf` | Phase 1-2 | Concrete sorting/searching/tree/graph implementations |
| `full-stack.pdf` | Phase 2 | HTML → CSS → JS → Django → REST APIs → Deployment |
| `backend.pdf` | Phase 2-3 | Databases, Auth, Caching, Testing, Architecture |
| `linux.pdf` | Phase 3 | Commands, File system, Processes, Shell scripting |
| `devops.pdf` | Phase 3-4 | Docker, GitHub Actions, Basic cloud deployment |
| `system-design.pdf` | Phase 4 | Scalability, CAP theorem, Design patterns |
| `aws.pdf` | Phase 5+ | Cloud infra (after everything else is solid) |

---

## Phase 0: Environment + Mindset Reset ✅ (DONE)

Everything in this phase is already complete:
- ✅ VS Code + Python + Git + extensions installed
- ✅ Git config set (name, email, VS Code as editor)
- ✅ `dev-journal` repo live on GitHub
- ✅ `academic_automator` cloned to `C:\Nick\projects\`
- ✅ GitHub profile exists (Nicklamdigas)

**One remaining task:** Set up your GitHub Profile README (pinned to your profile page)
- Go to GitHub → New repo → name it exactly your username: `Nicklamdigas`
- Add a `README.md` that introduces you — keep it short: who you are, what you're learning, what you're building

---

## Phase 1: Python + CS Fundamentals (Weeks 1–5)

**Goal:** Own Python completely. Understand DS&A. Write code you can explain line by line.

**Roadmaps active this phase:** `python.pdf`, `computer-science.pdf`, `datastructures-and-algorithms.pdf`

### Primary Learning Path — freecodecamp the python certification (in this exact order)
> freecodecamp the python certification gives you interactive exercises you write yourself. No watching videos and pretending you learned.

| # | Course | What it covers | Roadmap link |
|---|--------|----------------|--------------|
| 1 | **Learn Python** | Variables, functions, lists, dicts, loops, errors | python.pdf basics |
| 2 | **Learn Linux** | Terminal, filesystem, permissions, programs | linux.pdf intro |
| 3 | **Build a Bookbot** (project) | File I/O, text processing, real Python | python.pdf File I/O |
| 4 | **Learn Git** | Repos, branching, merging, rebase, remotes | All roadmaps |
| 5 | **Learn OOP** | Classes, encapsulation, inheritance, polymorphism | python.pdf OOP |
| 6 | **Build Asteroids** (project) | Event loops, state, game logic | python.pdf OOP |
| 7 | **Learn Functional Programming** | Pure functions, closures, decorators, recursion | python.pdf paradigms |
| 8 | **Learn DSA** | Big O, sorting, stacks, queues, trees, graphs, BFS/DFS | computer-science.pdf + DSA.pdf |
| 9 | **Build Static Site Generator** (project) | File parsing, templates, real output | python.pdf + full-stack.pdf |

🔗 Link: https://www.freecodecamp.org/learn/scientific-computing-with-python/

### Supplementary: CS50P (Harvard, free)
Do the problem sets **yourself, no AI, before looking at hints.**
- 🔗 https://cs50.harvard.edu/python/2022/
- Complete all 10 weeks — each problem set reinforces a freecodecamp the python certification concept

### LeetCode Practice
- Week 1-2: 3 Easy/day (arrays, strings) — https://leetcode.com/problemset/?difficulty=EASY
- Week 3-5: 5 Easy/day + 2 Medium/week
- **Rule:** Write your solution on paper first. Then type it. Then ask AI to review it.
- **Language:** Python only. No pasting AI solutions.

### build-your-own-x Project (End of Phase 1)
**Build your own Shell in Python** — teaches you how a terminal actually works
- 🔗 Search "build your own shell python" at: https://github.com/codecrafters-io/build-your-own-x
- Commit every step. Write a comment on every line before you move on.

### Phase 1 Projects (build all three — no AI writing the logic)
1. **CLI Task Manager** — `add`, `done`, `list`, `delete` commands, saved to `tasks.json`
   - Must handle: empty list, duplicate tasks, invalid input
   - Folder: `C:\Nick\projects\phase1-python\task-manager\`
2. **Student Grade Calculator** — reads a CSV of student names + marks, outputs averages, pass/fail
   - Must use: functions, file I/O, dictionaries, error handling
   - Folder: `C:\Nick\projects\phase1-python\grade-calculator\`
3. **Web Scraper** — scrapes headlines from a real news site (e.g., Nation.Africa) using `requests` + `BeautifulSoup`
   - Saves output to a JSON file, runs from CLI with a `--url` argument
   - Folder: `C:\Nick\projects\phase1-python\web-scraper\`

### Key Concepts Checklist (from `python.pdf` + `computer-science.pdf`)
Before moving to Phase 2, you must be able to do these WITHOUT looking them up:
- [ ] Write a class with `__init__`, methods, and `__str__`
- [ ] Implement a linked list from scratch
- [ ] Explain Big O of a loop vs nested loop vs binary search
- [ ] Write a recursive function and trace its call stack on paper
- [ ] Sort a list of dicts by a key using a lambda
- [ ] Handle a file that might not exist without crashing

---

## Phase 2: Full-Stack Web Development (Weeks 5–8)

**Goal:** Build real, visible things that work in a browser and can be shown to anyone.

**Roadmaps active this phase:** `full-stack.pdf`, `backend.pdf` (first half)

### Topics in Order (from `full-stack.pdf`)
1. **HTML deeper** — semantic HTML5, forms, accessibility basics
2. **CSS deeper** — Flexbox, CSS Grid, responsive design (media queries), custom properties
3. **JavaScript fundamentals** — DOM manipulation, events, fetch API, async/await, promises
   - No frameworks yet. Understand the language before the abstraction.
4. **Django** — URL routing, templates, models (ORM), forms, admin panel, user auth
5. **REST APIs** — what HTTP verbs mean, status codes, how to design endpoints
6. **Django REST Framework (DRF)** — build and consume a JSON API

### Free Resources by Topic
| Topic | Resource | Link |
|-------|----------|------|
| HTML/CSS | freeCodeCamp Responsive Web Design | https://www.freecodecamp.org/learn/2022/responsive-web-design/ |
| JavaScript | The Odin Project (JavaScript Path) | https://www.theodinproject.com/paths/full-stack-javascript |
| JavaScript | javascript.info (read it cover to cover) | https://javascript.info |
| Django | Official Django Tutorial (do all 7 parts) | https://docs.djangoproject.com/en/stable/intro/tutorial01/ |
| Django | Mozilla MDN Django tutorial | https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django |
| REST APIs | RESTful API Design — freeCodeCamp article | https://www.freecodecamp.org/news/rest-api-design-best-practices-build-a-rest-api/ |
| DRF | Official DRF Tutorial | https://www.django-rest-framework.org/tutorial/quickstart/ |

### build-your-own-x Project (End of Phase 2)
**Build your own Web Server in Python** — teaches you exactly how HTTP and servers work
- 🔗 https://github.com/codecrafters-io/build-your-own-x#build-your-own-web-server
- This is what Flask and Django are doing under the hood. Build it first.

### Phase 2 Projects
1. **Personal Portfolio Website** — HTML/CSS/JS only. No frameworks.
   - Fully responsive (works on mobile)
   - Sections: About, Skills, Projects (link to GitHub), Contact
   - Deploy on GitHub Pages (free): https://pages.github.com/
   - Folder: `C:\Nick\projects\phase2-web\portfolio\`
2. **Django Blog App** — full CRUD (create/read/update/delete posts), user registration + login, MySQL database
   - Must have: login required to create/edit, public can read, pagination
   - Folder: `C:\Nick\projects\phase2-web\django-blog\`

---

## Phase 3: Backend Depth + Linux + Deployment (Weeks 8–11)

**Goal:** Design and build systems you understand end-to-end. Deploy them live.

**Roadmaps active this phase:** `backend.pdf` (second half), `linux.pdf`, `devops.pdf` (Docker + CI/CD), `system-design.pdf` (intro chapters)

### Topics from `backend.pdf`
1. **Databases deeper** (from `backend.pdf` + `full-stack.pdf`)
   - MySQL: JOINs, subqueries, transactions, indexes, normalization (1NF, 2NF, 3NF)
   - SQLite for lightweight apps
   - ORMs vs raw SQL — know both
2. **Authentication** — JWT tokens, OAuth basics, session vs token auth
3. **Testing** — unit tests (`pytest`), integration tests, what to test and what not to
4. **Caching** — what Redis is, when to use it, simple in-memory caching
5. **Web security basics** (from `backend.pdf`) — HTTPS, CORS, OWASP Top 10 (read, don't memorize)

### Topics from `linux.pdf`
| Topic | Why It Matters |
|-------|----------------|
| File permissions (`chmod`, `chown`) | You will need this when deploying |
| Process management (`ps`, `kill`, `systemd`) | Your academic_automator uses this |
| Shell scripting (bash) | Automate your dev workflow |
| SSH & file transfer | Connect to remote servers |
| Package management (`apt`) | Install things on a server |
| Networking basics (`curl`, `netstat`, `ping`) | Debug API and deployment issues |

**Resource:** freecodecamp the python certification Learn Linux course (already in Phase 1 path) + `linux.pdf`

### Topics from `devops.pdf` (just the essentials now)
1. **Docker** — containerize a Python app, write a `Dockerfile`, use `docker-compose`
   - Resource: Docker Getting Started: https://docs.docker.com/get-started/
   - Resource: freecodecamp the python certification has a Docker course in their path
2. **GitHub Actions** — set up a CI pipeline that runs your tests automatically on every push
   - Resource: GitHub Actions docs: https://docs.github.com/en/actions/quickstart
3. **Deployment** — deploy a Django app live on Render (free tier)
   - Resource: https://render.com/docs/deploy-django

### Introduction to System Design (`system-design.pdf`)
Read only these sections now (no need to master — just build awareness):
- What is System Design? How to approach it?
- Performance vs Scalability, Latency vs Throughput
- Availability vs Consistency, CAP Theorem
- Load Balancers (concept only)
- Databases: SQL vs NoSQL — when to use which

**Resource:** System Design Primer (free): https://github.com/donnemartin/system-design-primer

### build-your-own-x Project (End of Phase 3)
**Build your own Database in Python** — teaches you B-trees, indexes, storage
- 🔗 https://github.com/codecrafters-io/build-your-own-x#build-your-own-database
- This directly reinforces your SQL knowledge.

### Phase 3 Flagship Project: Full-Stack School Management System
This is your **main portfolio project** — the one that gets you interviews.

**What it must include:**
- Student records (CRUD)
- Grade tracking + GPA calculation
- Timetable/schedule management
- User roles: Admin, Teacher, Student (different permissions)
- REST API (Django REST Framework)
- Frontend (simple HTML/CSS/JS dashboard — no framework needed)
- MySQL database with at least 5 normalized tables
- JWT authentication
- Deployed live on Render

**How to build it (the right order):**
1. Draw the ER diagram on paper first — every table, every relationship
2. Draw the wireframes (screens) before any code
3. Create the Django project, set up models
4. Build and test each API endpoint individually
5. Build the frontend last — consuming your own API
6. Write at least basic tests for the API
7. Deploy

**Folder:** `C:\Nick\projects\phase3-backend\school-management\`

---

## Phase 4: Portfolio Polish + Job Prep (Weeks 11–12 and ongoing)

**Goal:** Present yourself as a hireable junior developer. Apply for internships.

### System Design Depth (`system-design.pdf`)
Now go deeper on the rest of `system-design.pdf`:
- Caching strategies (Redis, CDN, application cache)
- Message queues (concept — Kafka, RabbitMQ)
- Microservices vs Monolith (when each makes sense)
- Cloud Design Patterns (read `aws.pdf` Step 1 only: IAM, VPC, EC2)
- Practice: For every project you've built, ask "how would this handle 100,000 users?"

**Resource:** Grokking System Design (free read): https://www.educative.io/courses/grokking-modern-system-design-interview-for-engineers-managers

### build-your-own-x (Advanced, Optional)
**Build your own Git in Python** — teaches you how version control actually works at the object level
- 🔗 https://github.com/codecrafters-io/build-your-own-x#build-your-own-git
- Only do this if you're curious. It's an excellent portfolio piece.

### GitHub Portfolio Must-Haves
- **Pinned repos:** Minimum 3 (portfolio site, school management system, one Phase 1 project)
- Every pinned repo must have:
  - Clear README: what it does, tech stack, how to run it, screenshots
  - Meaningful commit history (at least 20 commits that tell a story)
  - Live demo link
- **Profile README** (`Nicklamdigas/README.md`): who you are, what you're learning, what you're building

### CV (1 page only)
Structure:
```
NICHOLAS [SURNAME]
[City, Kenya] | GitHub: github.com/Nicklamdigas | LinkedIn | Email

SKILLS
Python, Django, Django REST Framework, Flask, SQL (MySQL/SQLite),
HTML, CSS, JavaScript, Git, Docker, Linux, REST APIs

PROJECTS
School Management System | Django, DRF, MySQL, JWT Auth, React | [Live link] [GitHub]
Academic Link Automator | Python, Flask, SQLite, Telegram Bot, systemd | [GitHub]
Portfolio Website | HTML, CSS, JavaScript | [Live link]

EDUCATION
B.Sc. Software Engineering — Zetech University (Expected [year])
Diploma in Business Information Technology — [College]

ACTIVITIES
[Any hackathon, open source contribution, community event]
```

### LinkedIn
- Headline: "Software Engineering Student | Python & Django Developer | Building real-world web systems"
- About: 3 sentences — who you are, what you're building, what you're looking for
- Post once a week about your learning — even small wins

### Networking (Kenya + Remote)
| Channel | Action |
|---------|--------|
| Twitter/X | Follow #KeTech, #DevKe, #NairobiDev — engage, don't just scroll |
| iHub Nairobi | Attend events (free): https://ihub.co.ke |
| Nairobi Dev Meetups | Search Meetup.com for "Nairobi tech" or "Python Kenya" |
| Discord | The Odin Project, CS50, freecodecamp the python certification — ask and answer questions |
| Safaricom Hackathon | Watch for annual call — excellent for CV + network |
| Zindi (Africa AI) | ML competitions — good exposure: https://zindi.africa |
| Open Source | Make 1-2 contributions to any Python/Django project on GitHub |

### Internship/Job Application Timeline
- **3 months before semester ends:** Start sending applications
- **Target roles:** Junior Developer, Software Engineer Intern, Backend Developer (Nairobi + Remote)
- **Target companies:** Safaricom, Andela (remote), Twiga Foods, Africa's Talking, any Kenyan startup
- **Freelance:** List on Upwork with your School Management System as portfolio — target small Kenyan businesses (inventory, POS, HR systems — your Business IT diploma is the pitch)

---

## Phase 5: Specialization (After Graduation / Year 4)

After Phase 4 you have a foundation. Choose one of these branches:

### Option A: AI/ML Engineer
- 🔗 Roadmap: `computer-science.pdf` + AI/Data Science roadmap (roadmap.sh)
- Tools: NumPy, Pandas, scikit-learn, TensorFlow/PyTorch
- Entry point: Zindi competitions, Kaggle

### Option B: Backend/API Engineer (Deepening Python)
- Go deep on `backend.pdf` — message queues, microservices, distributed systems
- Learn FastAPI as an alternative to Django
- `system-design.pdf` in full
- freecodecamp the python certification Go path (Golang for high-performance services)

### Option C: DevOps/Cloud Engineer
- Complete `devops.pdf` fully
- Complete `aws.pdf` (all 4 steps)
- Certifications: AWS Cloud Practitioner (free study materials exist)
- Tools: Terraform, Kubernetes, Ansible

### Option D: Freelance Full-Stack (Most immediate income)
- Build 2-3 client-ready templates (school system, inventory system, appointment booking)
- List on Upwork, Fiverr, LinkedIn
- Your Business IT diploma = you speak the client's language. Use it.

---

## Answering the Big Question: What's Your Niche?

**For Nick now (2026) → Full-Stack Python Web Developer + Automation**

This is your landing pad. It is NOT a permanent label. It is the niche that:
- Uses your existing skills (Python, HTML, CSS, MySQL)
- Has the most job/freelance opportunities in Kenya and remotely
- Keeps all future specializations open (AI/ML, backend, DevOps)
- Lets you monetize your Business IT diploma immediately

---

## Weekly Schedule Template (Break Period — 8 hrs/day)

| Time | Activity |
|------|----------|
| 8:00–9:00 | freecodecamp the python certification course (1 chapter minimum) |
| 9:00–11:00 | CS50P problem set or LeetCode (write on paper first) |
| 11:00–13:00 | Project work (Phase project — no AI for core logic) |
| 13:00–14:00 | Break + lunch |
| 14:00–16:00 | Continue project OR start build-your-own-x exercise |
| 16:00–17:00 | Review today's code, write dev-journal entry, commit to GitHub |
| 17:00–18:00 | Read tech articles, engage on LinkedIn/Twitter/Discord |
| 18:00+ | Rest. Seriously. Don't code past exhaustion. |

---

## Weekly Progress Check (Every Friday)

Answer these 6 questions in your dev-journal:
1. What can I build today that I couldn't build last week?
2. Can I explain every line of code I wrote this week?
3. Did I solve at least one problem myself before asking AI?
4. Did I commit code to GitHub at least 4 days this week?
5. Did I complete at least one freecodecamp the python certification chapter?
6. Did I write a dev-journal entry every day?

If yes to all 6 — you are on track.

---

## A Word on Mental Health & the Break

You mentioned this break was due to medical issues. This plan is intense but **sustainable is more important than fast**. If on a given day you can only do 4 hours — do 4 focused hours. Burnout will set you back more than a slow day will.

You are not behind. You are 21 with a diploma, a degree in progress, stable internet, full-time availability, and the self-awareness to know you need to change. That is already ahead of most.
