# AquaSC Paper Skills

Three Codex skills for writing research papers, preparing reviewer responses, and formatting publication figures. The conventions come from the AquaSC manuscript revision and advisor feedback. They can be adapted to other engineering and machine-learning papers.

## Included skills

- **[aquasc-paper-writing](skills/aquasc-paper-writing/SKILL.md)**: coherent paragraphs, selective abstracts, full terms before abbreviations, mechanism-focused results discussion, compact conclusions, and preservation of advisor edits and approved revision scope.
- **[aquasc-response-letter](skills/aquasc-response-letter/SKILL.md)**: direct, self-contained reviewer replies; gratitude in opening acknowledgments; black response prose; exact blue manuscript excerpts; and verified section/page/figure/table locators.
- **[aquasc-publication-figures](skills/aquasc-publication-figures/SKILL.md)**: subcaptions below panels, regular caption weight, matching x/y-axis fonts, thinner curves, readable single-column layouts, and tables without vertical rules. Includes a portable Matplotlib helper and synthetic layout examples.

The skills provide editorial conventions. Scientific facts, numerical results, and claims must come from the paper being edited.

## Install online in Codex

Ask Codex:

```text
Use $skill-installer to install the three skills from
https://github.com/phucngvinuni/aquasc-paper-skills
with these paths:
skills/aquasc-paper-writing
skills/aquasc-response-letter
skills/aquasc-publication-figures
```

To install one skill, give its GitHub folder URL:

- [Paper writing](https://github.com/phucngvinuni/aquasc-paper-skills/tree/main/skills/aquasc-paper-writing)
- [Response letter](https://github.com/phucngvinuni/aquasc-paper-skills/tree/main/skills/aquasc-response-letter)
- [Publication figures](https://github.com/phucngvinuni/aquasc-paper-skills/tree/main/skills/aquasc-publication-figures)

The installer downloads into `$CODEX_HOME/skills`, or `~/.codex/skills` when `CODEX_HOME` is unset. Installed skills become available on the next turn. Existing skill directories are not overwritten by the standard installer; see the update instructions below.

### Direct installer command

On macOS/Linux, using the default Codex home:

```bash
python "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo phucngvinuni/aquasc-paper-skills \
  --path skills/aquasc-paper-writing skills/aquasc-response-letter skills/aquasc-publication-figures
```

On Windows PowerShell:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" --repo phucngvinuni/aquasc-paper-skills --path skills/aquasc-paper-writing skills/aquasc-response-letter skills/aquasc-publication-figures
```

If Codex is installed under a custom `CODEX_HOME`, use the installer at that location. The helper supports `--dest` for another installation directory and `--ref` for a specific branch or commit.

## Usage

Invoke a skill by name and supply the files and edit scope:

```text
Use $aquasc-paper-writing to proofread this manuscript.
Edit only the blue text and preserve advisor comments.
```

```text
Use $aquasc-response-letter to sync the letter with the latest manuscript.
Verify every action excerpt and its final page/section locator.
```

```text
Use $aquasc-publication-figures to restyle the figures used in this manuscript.
Move subcaptions below panels, match axis fonts, and reduce curve thickness.
Keep the numerical data and manuscript prose unchanged.
```

The skills allow automatic discovery as well as explicit invocation. Current user instructions and the venue template take precedence over their defaults.

## Figure helper

The writing and response skills require no Python packages. To run the optional plotting helper/examples, use Python 3.10 or later and install the figure dependencies:

```bash
python -m pip install -r requirements-figures.txt
python skills/aquasc-publication-figures/scripts/demo_export.py --output-dir output/style-preview
```

The examples contain synthetic data and must not be cited as experimental results. They demonstrate a vertical single-column pair, a horizontal full-width pair, and a six-panel grid. The helper preserves existing data, axis limits, and canvas size while formatting artists.

Times New Roman is preferred when available. A consistent serif fallback is selected otherwise. Fonts are not distributed with this repository.

## Update installed copies

Ask Codex to compare the desired GitHub version with the installed skill folders, preserve local modifications, and update the selected skills. The standard installer intentionally stops when a destination already exists. A fresh download into a temporary directory can be used for comparison before replacing an installed copy.

## Repository layout

```text
skills/
  aquasc-paper-writing/
    SKILL.md
    agents/openai.yaml
    references/
  aquasc-response-letter/
    SKILL.md
    agents/openai.yaml
    references/
  aquasc-publication-figures/
    SKILL.md
    agents/openai.yaml
    references/
    scripts/aquasc_figure_style.py
    scripts/demo_export.py
```
