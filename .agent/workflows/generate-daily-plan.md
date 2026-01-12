---
description: Generate a detailed daily study and revision plan based on lecture analysis and user constraints.
---

# Workflow: Generate Daily Revision & Study Plan

This workflow generates a daily action plan for the user, balancing new learning with spaced repetition (1 week and 1 month intervals), strictly adhering to a 2-hour daily limit.

## 1. Context Loading & State Verification
1.  **Check `.plans` Directory**: Verify if the `.plans/` directory exists in the root. If not, create it.
2.  **Analyze History**: Read existing files in `.plans/` (sorted by date) to determine:
    *   What topics/lectures have already been covered (Last Covered State).
    *   What items were completed exactly 7 days ago (for 1-week revision).
    *   What items were completed exactly 30 days ago (for 1-month revision).
3.  **Load Resources**: List and read the available analysis files in `resources/claude_analysis/`.
    *   Target specific files like `lec-42.md`, `lec-43.md`, etc.
    *   Extract the list of "Topics" and "Practice Questions" from these files.

## 2. Plan Generation Strategy
1.  **Set Date**: detailed plan for "Today" or specific input date.
2.  **Allocate Time (Max 2 Hours)**:
    *   **Revision Slot (Fixed ~30-60 mins)**: High priority.
        *   Include items from **1 week ago** and **1 month ago**.
        *   If no specific items fall on these exact dates (e.g., first run), skip or add general review.
    *   **New Learning Slot (Remaining ~60-90 mins)**:
        *   Pick the next sequential topic(s) from the `resources/claude_analysis` that haven't been covered yet.
        *   **Constraint**: Do not overload. Pick 1-2 substantial topics or 1 lecture analysis.
3.  **Draft Content**:
    *   **Session Time**: Prefer **5:00 AM - 7:00 AM** (User's morning slot) or **7:00 PM - 9:00 PM** (Evening slot).
    *   **Mandatory Question & Code Coverage**:
        *   **CRITICAL**: You MUST extract **EVERY** single practice problem/link mentioned in the lecture analysis.
        *   **Code Links**: You MUST link to **every** local code file mentioned in the analysis:
            *   Instructor Code (`../../instructor_code/...`)
            *   User Practice Code (`../../user_practice_code/...`)
        *   Do not leave any resource unlinked.
    *   **Actionable Items**:
        *   "Read Section X in lec-Y.md" (Link to local file).
        *   "Review Instructor Code: [Filename](../instructor_code/...)"
        *   "Write/Refine User Code: [Filename](../user_practice_code/...)"
        *   "Solve Question Q1, Q2" (Link to questions in the md).

## 3. File Creation
1.  **Check for Revisions**:
    *   Identify any topics completed exactly 7 days or 30 days ago.
    *   **If Revision Due**:
        *   Create file: `.plans/revision/YYYY-MM-DD-Rev-Lxx.md` (e.g., `2026-01-19-Rev-L42.md`).
        *   **Content**:
            *   `# Revision: Lecture XX (YYYY-MM-DD)`
            *   `## 🎯 Goal: Spaced Repetition (1 Week/1 Month)`
            *   `## ⏱️ Time: 1 Hour`
            *   `## 📖 Quick Review`: Link to specific section in Analysis.
            *   `## 💻 Re-Solve`: Pick 1 Hard/Medium problem from that lecture.
2.  **Create Daily Plan File**: Generate `/.plans/YYYY-MM-DD-Lxx.md`.
    *   **Filename**: Include Lecture ID.
    *   **Structure**:
        *   `# Daily Plan: YYYY-MM-DD (Lecture XX)`
        *   `## ...` (Standard sections)
        *   `## 🔄 Revision Task`:
            *   If revision exists: "See separate plan: [Revision Lxx](../plans/revision/YYYY-MM-DD-Rev-Lxx.md)"
            *   Else: "No scheduled revision today."
3.  **Validation**: Ensure all paths are valid relative links (`../`).

## 4. Dashboard Update
1.  **Update Root README**: Modify `readme.md` (or `README.md`) to include a dynamic "📅 Current Task" section.
    *   Link to today's `.plans/YYYY-MM-DD-Lxx.md`.
    *   **Link Revisions**: Add entries to "Upcoming Revisions" section if a revision file was created.
    *   Show a brief summary check-list.

## 5. Progress Tracking
1.  **Analyze Completed Plans**:
    *   Iterate through all files in `.plans/`.
    *   Parse each file to count:
        *   Total Checkboxes (`- [ ]`, `- [x]`).
        *   Completed Checkboxes (`- [x]`).
    *   Group data by Lecture/Topic if possible, or simple daily aggregates.
2.  **Update `progress.md`**:
    *   Create or Overwrite `progress.md` in the root.
    *   **Header**: `# 📊 Revision Progress Tracker`.
    *   **Summary Stats**: Total Days Planned, Completion Rate %.
    *   **Detailed Table**: Date | Focus | Status | % Done.
    *   **Lecture Coverage**: Simple list of Lectures fully covered vs in-progress.
3.  **Link in README**: Ensure `progress.md` is linked in the main `README.md`.

## 6. User Notification
1.  Notify the user that the plan is created and progress updated.
