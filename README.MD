<div align="center">

<br/>

```
██████╗  █████╗ ██╗██╗  ██╗   ██╗███████╗ █████╗ ████████╗██╗██████╗ ███████╗   █████╗ ██╗
██╔══██╗██╔══██╗██║██║  ╚██╗ ██╔╝██╔════╝██╔══██╗╚══██╔══╝██║██╔══██╗██╔════╝  ██╔══██╗██║
██║  ██║███████║██║██║   ╚████╔╝ ███████╗███████║   ██║   ██║██████╔╝█████╗    ███████║██║
██║  ██║██╔══██║██║██║    ╚██╔╝  ╚════██║██╔══██║   ██║   ██║██╔══██╗██╔══╝    ██╔══██║██║
██████╔╝██║  ██║██║███████╗██║   ███████║██║  ██║   ██║   ██║██║  ██║███████╗  ██║  ██║██║
╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝╚══════╝  ╚═╝  ╚═╝
```

### 🗞️ Live Indian Political News &nbsp;→&nbsp; ✍️ Hinglish Satire &nbsp;→&nbsp; 🎨 AI Comic &nbsp;— **Fully Autonomous**

<br/>

[![Live Demo](https://img.shields.io/badge/🔴%20Live%20Demo-Click%20Here-FF4500?style=for-the-badge&labelColor=1a1a1a)](YOUR_LIVE_LINK_HERE)
&nbsp;
[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️%20in%20India-FF6B6B?style=for-the-badge&labelColor=1a1a1a)](https://github.com/YOUR_GITHUB_USERNAME)

<br/>

</div>

---

## 🧠 What Makes This Different From "Just Another AI Project"

Most AI projects = one API call + display result. **DailySatire.ai is not that.**

This is a **true multi-agent orchestration system** — four specialized AI agents collaborate in a pipeline, each with a distinct role, passing structured outputs down the chain to produce something no single model call could achieve alone.

> **The insight:** Real-world AI engineering isn't about prompting — it's about *orchestrating* models, managing state, handling failures, and delivering results reliably at scale. This project demonstrates exactly that.

<br/>

## 🏗️ System Architecture

```
                        ┌─────────────────────────────────────────────────────┐
                        │                 USER REQUEST                        │
                        │            (Clerk Auth Token)                       │
                        └──────────────────────┬──────────────────────────────┘
                                               │
                                               ▼
                        ┌─────────────────────────────────────────────────────┐
                        │              FASTAPI ORCHESTRATOR                   │
                        │         Rate Limit Check → MongoDB                  │
                        │           (5 comics / user / day)                   │
                        └──────────┬───────────────────────────────────────────┘
                                   │
               ┌───────────────────┼───────────────────────────┐
               │                   │                           │
               ▼                   ▼                           ▼
     ┌──────────────┐    ┌──────────────────┐      ┌─────────────────┐
     │  🕵️ SCOUT    │ →  │  ✍️ EDITOR        │ →   │ 🎨 ILLUSTRATOR  │
     │              │    │                  │      │                 │
     │  Fetches     │    │  Converts news   │      │  Generates a    │
     │  trending    │    │  → punchy        │      │  comic-style    │
     │  Indian      │    │  Hinglish        │      │  image via      │
     │  political   │    │  satire via      │      │  Hugging Face   │
     │  news        │    │  Gemini LLM      │      │  Diffusion      │
     └──────────────┘    └──────────────────┘      └─────────────────┘
                                                            │
                                                            ▼
                                              ┌─────────────────────────┐
                                              │    🖨️ PUBLISHER          │
                                              │                         │
                                              │  Overlays satire text   │
                                              │  onto image → final     │
                                              │  comic panel returned   │
                                              └─────────────────────────┘
```

<br/>

## ⚙️ Tech Stack

<div align="center">

| Layer | Technology | Why |
|---|---|---|
| **Frontend** | ![Next.js](https://img.shields.io/badge/Next.js_16-000000?style=flat-square&logo=next.js) + Turbopack | Blazing-fast dev builds, App Router |
| **Auth** | ![Clerk](https://img.shields.io/badge/Clerk-6C47FF?style=flat-square&logo=clerk&logoColor=white) | Production-grade auth (Google + Email) in minutes |
| **Animations** | ![Framer Motion](https://img.shields.io/badge/Framer_Motion-0055FF?style=flat-square&logo=framer&logoColor=white) | Fluid, physics-based UI transitions |
| **Backend** | ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) | Async Python API, auto-generated Swagger docs |
| **LLM (Satire)** | ![Gemini](https://img.shields.io/badge/Google_Gemini-4285F4?style=flat-square&logo=google&logoColor=white) | State-of-the-art language model for Hinglish generation |
| **Image Gen** | ![Hugging Face](https://img.shields.io/badge/Hugging_Face_Diffusion-FFD21E?style=flat-square&logo=huggingface&logoColor=black) | Open-source diffusion models for comic-style art |
| **Database** | ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white) | Flexible document store for usage tracking + history |


</div>

<br/>

## 🤖 The Four Agents — Deep Dive

### 🕵️ Agent 1: Scout
Monitors live news sources and surfaces the most trending Indian political stories. Implements deduplication so the same story never gets satirized twice.

### ✍️ Agent 2: Editor  
Takes raw news headlines and context → feeds them to **Google Gemini** with a carefully engineered prompt → produces punchy, culturally authentic Hinglish satire. This isn't just "translate to Hindi" — it writes *jokes*, with setup, punchline, and political bite.

### 🎨 Agent 3: Illustrator  
Takes the satirical narrative and generates a comic-style illustration using **Hugging Face diffusion models**. Prompt engineering here is critical — the agent constructs image prompts that match the comic aesthetic, not just the news topic.

### 🖨️ Agent 4: Publisher  
Composites the satire text onto the generated image, handles typography, panel layout, and returns a finished comic — ready to share.

<br/>

## 📊 Key Engineering Decisions

```python
# Why MongoDB for rate limiting instead of Redis?
# → Zero additional infra. MongoDB TTL indexes auto-expire daily counts.
# → Same DB used for comic history = fewer moving parts in production.

usage_doc = {
    "user_id": clerk_user_id,
    "date": today,           # TTL index on this field
    "comics_generated": 3,   # Checked before every pipeline run
}
```

```javascript
// Why Clerk over NextAuth / custom JWT?
// → Clerk handles edge cases: session rotation, device management,
//   OAuth token refresh — things that take weeks to get right manually.
// → Middleware protection on all /api routes with 3 lines of config.
```

<br/>

## 🔐 Security & Abuse Prevention

- **Rate Limiting**: 5 comics/day/user enforced at the FastAPI layer — before any model is called. Prevents API cost blowouts.
- **Auth on Every Route**: Clerk middleware validates JWT on all backend endpoints. No anonymous access to the pipeline.
- **Input Sanitization**: User-provided parameters are validated before being passed to any LLM prompt.

<br/>

## 🚀 Local Setup

### Backend

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/DailySatire
cd DailySatire/Backend

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`:
```env
GEMINI_API_KEY=your_gemini_key
HUGGINGFACE_API_KEY=your_hf_key
MONGODB_URI=your_mongodb_uri
```

```bash
uvicorn api:app --reload
# → http://127.0.0.1:8000
# → http://127.0.0.1:8000/docs  (Swagger UI)
```

### Frontend

```bash
cd Frontend/comic-frontend
npm install
```

Create `.env.local`:
```env
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_...
CLERK_SECRET_KEY=sk_...
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

```bash
npm run dev
# → http://localhost:3000
```

<br/>

## 🗂️ Project Structure

```
DailySatire/
│
├── Backend/
│   ├── api.py                  # FastAPI app + route definitions
│   ├── agents/
│   │   ├── scout.py            # News fetching agent
│   │   ├── editor.py           # Gemini satire generation agent
│   │   ├── illustrator.py      # Hugging Face image generation agent
│   │   └── publisher.py        # Comic compositing agent
│   ├── utils/
│   │   ├── image_utils.py      # PIL processing, text overlay
│   │   └── rate_limiter.py     # MongoDB usage tracking
│   ├── output/                 # Generated comic cache
│   └── requirements.txt
│
└── Frontend/
    └── comic-frontend/
        ├── app/
        │   ├── page.tsx         # Landing + generator UI
        │   └── api/             # Next.js API routes
        ├── components/
        │   ├── Antigravity.tsx  # Custom particle background
        │   └── ComicCard.tsx    # Comic display component
        ├── middleware.ts        # Clerk auth protection
        └── package.json
```

<br/>

## 🔭 Roadmap

| Feature | Status |
|---|---|
| 🖼️ User comic gallery & history dashboard | Planned |
| 🎨 Upgraded models (FLUX / Animagine XL) | Planned |
| 🔊 Voice narration via ElevenLabs | Planned |
| 📱 Full mobile responsiveness | In Progress |
| ⚡ Streaming responses for faster perceived UX | Planned |
| 🌐 Multi-language satire (Tamil, Bengali, Marathi) | Exploring |

<br/>

## 💡 What I Learned

Building this taught me things that no tutorial covers:

- **Agentic pipelines fail differently** than single-model calls — you need error boundaries at every handoff, not just at the API layer
- **Prompt engineering for style consistency** across agents (the Editor's tone must inform the Illustrator's visual prompt)
- **Cost management** is a real engineering constraint — rate limiting isn't just a feature, it's what keeps a project alive
- **Diffusion model prompt craft** is its own discipline — comic-style image generation needs very different prompts than photorealism

<br/>

---

<div align="center">

**Built by [Saksham Sharma](https://github.com/YOUR_GITHUB_USERNAME)**

*Building at the intersection of AI + Creativity*

<br/>

If this project sparked something — ⭐ star it, 🍴 fork it, or just say hi.

</div>
