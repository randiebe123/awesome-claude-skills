# Metadata for Virtual Materials

Every video, audio file and image the twin produces gets a record so it can live in a digital
collection (Omeka, CONTENTdm, Islandora, a Google Sheet, or the library website).

## Dublin Core record (default)
```yaml
title:        "Spot Fake News in 3 Steps"
creator:      "<Her name> (Cyber Librarian)"
contributor:  "AI voice/avatar generated with permission"   # when applicable
subject:      ["Media literacy", "Fact checking", "Fake news"]   # prefer LCSH terms
description:  "A 60-second tip video teaching the SIFT method."
publisher:    "<Library>"
date:         2026-10-11
type:         MovingImage      # MovingImage | Sound | StillImage | Text | InteractiveResource
format:       video/mp4        # audio/mpeg | image/jpeg | image/png | text/vtt
identifier:   "<URL or local ID>"
language:     en
audience:     "Teens 13-18"
rights:       "CC BY-NC 4.0"
relation:     ["captions: spot-fake-news.srt", "transcript: spot-fake-news.txt"]
```

## Subject tags
- Use Library of Congress Subject Headings where possible (e.g. "Information literacy",
  "Internet--Safety measures", "Fake news").
- Add 3–8 plain-language tags for social and search.

## Reading lists
For each item: title, author, year, format (print / e-book / audiobook), one-line hook,
audience, how to borrow. Mark items as "verify in catalog" unless the catalog was checked —
never invent call numbers or ISBNs.

## File naming
`YYYY-MM-DD_type_short-title_v01.ext` → `2026-10-11_video_spot-fake-news_v01.mp4`
