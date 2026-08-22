# CATIA V5 Knowledge Test

A desktop quiz application for practising CATIA V5 knowledge, built with Tkinter. It shuffles a bank of 187 questions, grades each answer immediately with an explanation, tracks your score, and lets you review every question at the end.

I built this while preparing for CATIA V5 certification. Flashcards were too shallow for multiple-answer questions, so I wanted something that could grade "select all that apply" properly and explain *why* an answer was wrong.

## Features

- **187 questions** — 145 single-choice, 42 multiple-choice ("select all that apply").
- **Immediate feedback** with an explanation for every question, right or wrong.
- **Randomised order** each run, so you learn the material and not the sequence.
- **Running score** displayed as you go.
- **Review mode** at the end — every question with your answer, the correct answer, and the explanation, in one scrollable window.
- Window auto-sizes to your screen, with large fonts for comfortable reading.

## Running it

Requires Python 3.9+ with Tkinter, which ships with the standard python.org installer on Windows and macOS. No third-party packages needed.

```bash
python main.py
```

On Debian/Ubuntu, Tkinter is a separate package:

```bash
sudo apt install python3-tk
```

## Question format

Questions live in `data.json` next to the script, as a list of objects:

```json
{
  "question": "What does CATIA stand for?",
  "options": [
    "Computer Aided Three-Dimensional Interactive Application",
    "Computer Aided Technical Intelligent Analysis"
  ],
  "correct_answer": ["Computer Aided Three-Dimensional Interactive Application"],
  "type": "single",
  "explanation": "CATIA is an acronym for Computer Aided Three-Dimensional Interactive Application."
}
```

| Field | Meaning |
|---|---|
| `question` | The question text. |
| `options` | All choices shown to the user. |
| `correct_answer` | List of the options that are correct. A single string is also accepted for backwards compatibility. |
| `type` | `"single"` for one answer, `"multiple"` for select-all-that-apply. |
| `explanation` | Shown after answering. Optional, but present on every question here. |

The app validates this structure on startup and reports a clear error if a question is malformed, rather than failing halfway through a quiz.

To add your own questions, append objects to `data.json` — no code changes needed.
