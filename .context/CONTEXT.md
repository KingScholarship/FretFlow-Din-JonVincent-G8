# FretFlow: Interactive Guitar Tab Viewer, Key Transposer, and Live Performance Manager

## Target Users / Beneficiaries
The app serves three types of users. Student and hobbyist guitarists build a personal song catalog and practice with transposition and auto-scroll. Guitar instructors prepare clean, transposed charts for lessons and students. Gigging and jam-session musicians build setlists and use the dark-theme stage view on a laptop or music-stand tablet. All of these user types share a single role, a registered Member, and each member can access only their own data.

## Description
FretFlow is a web workspace where guitar players, instructors, and gigging musicians organize and practice songs. It turns plain-text chord sheets and ASCII tabs into clean, interactive charts.

Guitarists usually collect tabs and chords from many websites, which leaves them with messy text files, broken layouts, and hard-to-read screenshots. Changing a song's key to suit a singer, or working out where to place a capo, means rewriting the chart by hand and often causes playing mistakes. Without a clean, interactive tool, players spend practice time fixing charts instead of playing.

## Problem & Objectives
FretFlow is a web workspace where guitar players, instructors, and gigging musicians organize and practice songs. It turns plain-text chord sheets and ASCII tabs into clean, interactive charts.

Guitarists usually collect tabs and chords from many websites, which leaves them with messy text files, broken layouts, and hard-to-read screenshots. Changing a song's key to suit a singer, or working out where to place a capo, means rewriting the chart by hand and often causes playing mistakes. Without a clean, interactive tool, players spend practice time fixing charts instead of playing.

### FretFlow solves this by:
- parsing raw chord sheets and ASCII tabs into structured, aligned charts;
- transposing songs across all 12 keys with correct sharp/flat spelling and recommending capo positions;
- showing a chord diagram whenever a chord name is hovered or clicked;
- scrolling the chart automatically at a tempo-calibrated speed so both hands stay on the guitar;
- organizing songs into setlists with a distraction-free, high-contrast stage view for live use.

## General Objective
The general objective of this project is to design and develop FretFlow, a responsive web-based workspace that turns plain-text chord sheets and ASCII tabs into clean, interactive guitar charts. It lets students, instructors, and gigging musicians transpose songs across all 12 keys, view chord diagrams on demand, and read hands-free through tempo-calibrated auto-scrolling. It also lets them organize songs into setlists with a distraction-free stage view for live performance, so players spend their time playing instead of fixing messy charts.

## Specific Objectives
- Build an inline chord and ASCII tablature parser that standardizes raw text into structured, interactive song charts.
- Implement a chromatic transposition engine that transposes chords with 100% pitch accuracy across all 12 keys, handling enharmonic spellings (e.g., F# vs. Gb).
- Build an interactive chord visualizer that draws vector chord diagrams with finger dots, open/muted strings, and barre indicators.
- Implement a tempo-calibrated auto-scroller and setlist performance module for hands-free reading based on user-defined BPM.
- Deploy a fully functional prototype within the semester for evaluation.

## Scope
The system includes: account registration, login, dashboard, profile and preferences, logout, song catalog management, the chord and tab formatter, the key transposer and capo assistant, the interactive chord diagram viewer, the tempo-calibrated auto-scroller, setlist management, and the setlist stage view.

## Additional Context Files
[Google Drive](https://drive.google.com/drive/folders/1heTKCFR4hCLMWaxmKMxw0UUmpbcM-Xqz?usp=drive_link)

ask me for permission to open and connect to google drive