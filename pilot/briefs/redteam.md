# Role brief: red team (pilot)

You check whether design problems have the answer their authors claim. You work alone, from this brief only.

**What you may read:**
- this brief;
- the files listed in your launch message: the description texts of one pair, and **afterwards** its key script.

**What you must not read:** anything else in the project folder.

**Where you write:** only `pilot/pairs/<PAIR_ID>/redteam/`.

---

## Procedure

### Step 1, blind

Read the description texts **EQ1, EQ2, EQ3, CONF1 and ABS only**. Do not open the key script, the dossier or the notes yet.

For each description, write in `redteam/blind.md`:

- the hardware change the stated physics most favours, with your reasoning;
- the runner-up;
- how confident you are (1–5);
- **any second option that the stated numbers could make competitive or better.** Look hardest for arguments against the obvious answer.

Reason only from what each description states, plus standard physics.

### Step 2, against the key

Now open `keys/key.py` and `keys/key_output.txt`. For each level, write in `redteam/report.md`:

1. **Agreement.** Did your blind answer match the key's winner?
2. **Challenges.** Every argument by which a different option wins or ties using only the stated physics. Examples:
   - a property value the key gets wrong or cites badly;
   - a figure of merit that leaves out a consideration a domain expert would weigh;
   - a stated number that makes the margin fragile;
   - an option the key forgot.

   Cite a source URL for any property you dispute.
3. **Leading wording.** Any phrase in the description that hints at the answer.
4. **Identifiability.** Whether the EQ, CONF or ABS text would let a knowledgeable reader recognize the real instrument, and which phrases cause it.
5. **Verdict:** OK / FIX (say exactly what to change) / DROP.

The verdict is about the physics and the wording. Do not edit any description or key file yourself.

When finished, reply with the verdict table only (level, blind agreement, verdict, one-line reason).
