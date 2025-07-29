# Pull Requests
* Review an existing PR in a public open-source repo (React PRs), read through comments and discussions and observe how changes are requested and approved.\
- Each messages have clear title to demonstrate which function the developers have worked on or fixed.
- For each message, they contain detailed description to show what was the problem, how they fix the problem and if the problem has been fixed or more help is needed.
- Before merging, each messages go through automated tests to make sure the code meets the requirements. If passed, the feature branch could be merged into the main branch. Otherwise, the feature branch cannot be merged and needs to be fixed. When merged, the code maintainer has to make sure the merge doesn't cause conflicts.
- The titles of the messages use committing convention, like "Fix:" or "docs:".
* Why are PRs important in a team workflow?
- They let the team discuss changes and provide feedback to each other's work before merging to the main branch, which encourages constructive reviews and decision-making.
- They are essential for reviewing code to make sure all the bugs are found and fixed and the code meets business and user requirements.
- They allow team members to trace all the code modifications, so that if there are any incidents, the team can go back to previous states and fix it.
- For new members such as interns, PRs act as documentation for them to review the codebase to understand coding practices, tools and convention that the company uses.
## Specific Example
https://github.com/facebook/react/pull/34026
- The title is clear to show what was changed (Allow assigning ref-accessing functions to objects if not mutated) and where was changed (complier)
- The description restated the change and demonstrated how it should be changed (rewrite the ref validation to use the new mutation/aliasing effects, which would provide a more consistent behavior across instruction types and require fewer special cases like this.)
- The PR then went through testing cases by a code maintainer to make sure the code meets the requirements and no conflicts appear between the feature branch and the main branch.
- I learn from reviewing an open-source PR how professional developers writing titles, descriptions and providing feedback of the PRs by using technical norms and respectful languages. All the commit messages are in English, which allows for better understanding and communication since English is the most popular language in the world.
- I can see the flow of requests for changes, approvals, and merges.
- I can see how developers collaborate with each other even though they have different schedules and working styles. Due to their meaningful commit messages, they can keep track with the current progress and enable later reviews.
- I can see the way a professional pull request is made.
# Writing Meaningful Commit Messages
* Explore commit histories in an open-source GitHub project (React) and analyze good vs. bad commit messages.
- Good commit messages in React: They use convention like "Bug:", "Compile Bug" or "Feature Request" to indicate the types of changes. The tiles are clear, which state the current problems and where they happen. The description are informative, which demonstrate the types of issue, the link to the repo, the frequency of the errors, the versions of React and React Complier that the developer is using.
- Bad commit messages: I cannot find any bad messages in this open-source project, but common signs of bad commit messages are short, vague messages like "fixed" or "changed" (no contexts, no issues stated, no code locationa and no detailed purposes) or messages unrelated to the codebase like "final final".
* What makes a good commit message?
- The message is clear and specific (it should demonstrate what was changes and why/how it was changed).
- The message is concise and informative (it should provide enough contexts and details to understand the changes made, don't use generic messages like "fix stuff") to help other people understand the purpose behind these changes
- The message should follow committing convention ("feat:", "fix:", etc.) for readability.
* How does a clear commit message help in team collaboration?
- It helps other team members review the code easily and fast to improve team workflow and productivity.
- It allows for later feedback in retrospectives and acts as documentation for new members like interns.
- It shows you actually put effort and proper care to the shared work.
* How can poor commit messages cause issues later?
- It makes other members confused to understand which piece of code was changed and the reasons of changes, so they have to waste time asking for clarification.
- It makes it harder for later review if there are any incidents. Due to vague messages, the team has to read every single line of code to find the bugs, which affects the workflow and productivity.
- For new members, they cannot understand how the code works because of poor documentation, so when they start working on the codebase, they will lose track and be unsure of what to do.
# Understanding git bisect
* What does git bisect do?
- git bisect is a binary search tool built into Git to find the exact commit where a bug was introduced. You tell Git whether a commit is good (before the bug) or bad (after the bug), and Git will narrow down the range until it finds the commit that contains the bug.
* When would you use it in a real-world debugging situation?
- When you identify a bug but not sure which commit introduced it.
- The commit history is too large and you will waste too much time to manually review every single commit.
- The bug cannot be detected using automated tests but you can write a simple test to catch it.
* How does it compare to manually reviewing commits?
- git bisect allows developers to find bugs much faster with higher precision, while traditional approach requires developers to spend a huge amount of time to identify bugs and it is prone to errors. While git bisect requires initial setup, the time and effort saved from the search can make up for the setup; manual search requires developers to read the commit changes one-by-one which wastes a lot of time and effort and the bug is not guaranteed to be found. However, manual search allows you to understand the code structure and functions clearly, while git bisect is suitable for fixing bugs in small, specific functions. 
# Advanced Git Commands & When to Use Them
* What does each command do?
- git checkout main -- <file>: Restore a specific file from main without affecting other changes.
- git cherry-pick <commit>: Apply a specific commit from another branch without merging the whole branch.
- git log: View commit history and understand how changes evolved.
- git blame <file>: See who last modified each line in a file and when.
* When would you use it in a real project (hint: these are all really important in long running projects with multiple developers)?
- git checkout main -- <file>: Restore a specific file after a bad changes without removing any other work, which is great for undoing changes to config files or docs without resetting the entire branch.
- git cherry-pick <commit>: Integrate a specific fix or feature from another branch, which is useful when you want to apply only one change without merging unrelated work.
- git log: Discover the development process of a feature, trace bugs, or write changelogs.
- git blame <file>: Debugging code by showing a line-by-line history of who last modified it, which is valuable for audits, refactors, and tracking causes. This command can work well with git bisect for debugging.
* What surprised you while testing these commands?
- git checkout main -- <file> doesn’t create a commit in the commit history, which can be risky if you forget to stash other changes.
- git cherry-pick can fail if the commit misses necessary contexts or documentation in your branch (missing imports or files).
- git log has formatting options (--oneline, --graph, etc.) to turn it into a timeline powerhouse.
# Merge Conflicts and Conflict Resolution
* What caused the conflict?
- It happened due to overlapping changes in the same file from different branches. When conflicts happen, Git will stop the merge and mark the file with conflict markers (<<<<, ====, >>>>). The code between <<<< and ==== is the code appeared in the main branch, while the code between >>>> and ==== is the new one after pulling the code from other branches.
* How did you resolve it?
- I have to open the conflict file in the feature branch and look for conflict marker, then I will keep relevant changes and remove unnecessary ones. Once resolved you can merge the feature branch with the main branch.
* What did you learn?
- Merge conflicts are pretty common and you have to deal with them very often.
- Using git client like GitHub Desktop can help identify the conflicts easily since it highlights the conflicts and provides clickable options.
- It shows team communication is important. Good communication helps resolve the conflicts better since the team can discuss which features to keep and which to discard.
# Branching & Team Collaboration
* Why is pushing directly to main problematic?
- The changes are pushed directly without reviewing stages, which can lead to bugs, unfinished features, file conflicts and security vulnerabilities.
- When multiple people push files to the main branch, it can be harder to trace changes, understand what was changed, who changed and if the changes meet satisfaction and standards.
- If there are any major errors, reverting back to the state before could be challenging and messy, especially when there are many developers working on that project.
* How do branches help with reviewing code?
- Branches create isolated, safe sandboxes for each developer to work on features, fixes and try out new functions without touching the working, stable main code.
- By submitting changes via PRs, it allows other developers to review the changes, provide feedback, identify any problems and avoid conflicts before merging into the main branch. The review process ensures the code works properly and meets the requirements, which promotes team collaboration and constructive feedback.
* What happens if two people edit the same file on different branches?
- This will create a merge conflict if the changes are overlapping each other. If the changes are on different parts of the file, Git can merge these branches into the main branch. Decisions must be made to keep which version/features and discard the unnecessary changes. The resolution of the conflicts require great team collaboration, decision-making and sympathy.
# Git concept: staging vs committing
* What is the difference between staging and committing?
- Staging (git add) is like preparing a snapshot of your changes. For example, you want a file, or a part of a file to be included in the next commit.
- Committing (git commit) is when you actually record the staged changes into Git repos with a message explaining why you made these changes.
* Why does Git separate these two steps?
- You want to stage some changes but not others, which is suitable for curating commits.
- You want to build small commits that each represents a focused change to improve history readability and debugging.
- You can review staged files before permanently adding them to reduce accidental commits.
* When would you want to stage changes without committing?
- When you’re working steadily and want to save your progress, but haven't finalized the whole feature.
- When you want to combine multiple changes into a separate commit. For example, you want to stage your typo fixes first, then your logic updates later.
- When collaborating with other team members, you want them to review staged changes before committing.