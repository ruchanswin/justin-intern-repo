# What is the purpose of CI/CD?
- CI/CD aim to streamline software development by automating the build, test, and deployment processes. They can detect bugs early since CI runs tests and checks on every commit or pull request to catch bugs and errors before they reach production, provide faster feedback on code quality and integration issues, reduced manual work by automating deployment, which minimises human error and saving time. They also encourage team collaboration, small and frequent commits.
## How does automating style checks improve project quality?
- They ensure the code follows standard formatting and naming conventions.
- Clean, well-formatted code is easier to review, debug, and maintain.
- They reduces typos and sloppy documentation, especially content in the user interface.
- They ensure the code structure remains clean and works smoothly even if more contributors join.
### What are some challenges with enforcing checks in CI/CD?
- Overly strict linting rules may flag harmless code, which frustrates developers.
- Setting up CI tools like GitHub Actions and Husky requires careful tuning to avoid performance bottlenecks.
- Enforcing checks could be regarded as unnecessary and tedious.
- Keeping linters and CI workflows updated with the project needs considerable time and effort.
#### How do CI/CD pipelines differ between small projects and large teams?
- Pipeline complexity and scalability: Small projects work with simple workflows and fewer checks, and the setup is easy with fast iteration cycles. However, large teams create multi-stage pipelines with parallel jobs and conditional logic, and these pipelines requires robust infrastructure, monitoring, and scaling strategies.
- Tooling: Small projects mostly use lightweight tools like Husky, ESLint or Prettier, while large teams use heavier and more complex tools like Jenkins, CircleCI, GitHub Actions with custom runners.
- Enforcement: Enforcing CI/CD pipelines in small projects is often optional or lightweight, while large teams take CI/CD pipelines seriously with code ownership, required checks, and protected branches.
- Collaboration: Small projects only require an individual or a small group to work on, while large teams has multiple sections with branching strategies, code reviews, and integration testing.

<<<<<<< Updated upstream
## How does automating style checks improve project quality?

### What are some challenges with enforcing checks in CI/CD?

#### How do CI/CD pipelines differ between small projects and large teams?
=======
##### How to set up CI/CD workflow
1. Create a new Github branch (you can use Github commands or Github Desktop interface) and create package.json file with npm init -y
2. Install packages that will be use for Markdown linting and automated spell checks: markdownlint-cli (check .md formatting), cspell (find typos across files), husky (run scripts on git hooks like pre‑commit), lint-staged (run linters only on staged files)
npm i -D markdownlint-cli cspell husky lint-staged
3. Add scripts to run the tools:
- lint:md: run markdownlint on every .md files and ignore large folders
- lint:spell: run cspell across the repo (uses .gitignore to avoid committing large folders like node_modules/)
- lint: command that runs both the above commands
- prepare: run after install to set up Husky
- lint-staged: tell Husky to only check staged files at commit time
4. Configure the linters by creating .markdownlint.json and cspell.json
5. Add a local pre-commit hook (Husky). In the pre-commit file, replace the content inside with npx lint-staged
6. Create the Github CI workflow file ci.yml
7. Commit the branch, push the branch and then create the pull request.
>>>>>>> Stashed changes
