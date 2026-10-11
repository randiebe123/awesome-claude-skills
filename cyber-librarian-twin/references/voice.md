# Voice Content

## Writing for text-to-speech
- Short sentences (≤ 20 words). One idea per sentence.
- Write numbers and abbreviations the way they're spoken: "twenty twenty-six", "U R L",
  "P D F", "nine-seven-eight" for ISBN prefixes.
- Spell out symbols: "and" not "&", "percent" not "%".
- Pauses: a line break or "…" for a short pause; a new paragraph for a longer one. If the TTS
  engine supports SSML-style breaks, use `<break time="0.6s" />` sparingly.
- Pronunciation hints for names and titles in brackets for the producer, then remove them
  before generating: `Goodreads`, `Libby [LIB-ee]`, `JSTOR [JAY-stor]`.
- Emphasis comes from word order, not ALL CAPS.

## Formats
| Format | Length | Structure |
|--------|--------|-----------|
| Voice message / voicemail greeting | 15–30 s | greeting → purpose → action → sign-off |
| Podcast intro / outro | 20–40 s | show name, her name, episode topic, disclosure |
| Audio booktalk | 60–120 s | hook → premise (no spoilers) → who will love it → how to borrow |
| Narrated tutorial | per step | "Step one…" with a pause after each step |
| Story-time intro | 30 s | warm welcome, title, author, illustrator |

## Producing audio (ElevenLabs)
1. Use `voice_id` from `persona.md`; if empty, `creative_list_voices` → pick a warm, clear
   female voice and tell the owner which one.
2. `creative_generate_speech` with the cleaned script (pronunciation brackets removed).
3. Poll `creative_get_flow_run_status`, let the owner choose a variation, then return the link.
4. Always attach the transcript.

## Cloning her voice (owner only)
Only for the person this twin represents, with her consent recorded in `persona.md`.
1. She records 1–3 minutes (instant clone) or 30+ minutes (professional clone) of clean speech:
   quiet room, same mic, natural reading pace, varied sentences, no music.
2. She uploads the recordings in the ElevenLabs app (Voices → Add voice → Clone) — the cloning
   upload is done by her, in her account.
3. Paste the resulting `voice_id` into `persona.md`.
4. Alternatively, design a non-cloned "twin-style" voice: `creative_design_voice` with a
   description such as "warm, clear, mid-30s female librarian, friendly and calm, light
   smile in the voice" and a sample line she wrote; save her pick with
   `creative_save_designed_voice`.

Never clone a voice from someone else's recordings, even if asked.
