# Navigation with React Router

* What are the advantages of client-side routing?
* It supports fast navigation because it doesn't need to load the full page, it just loads the necessary components, which makes the trasitions smoother and improves user experience. Also, app state like form inputs or scroll position can persist across route changes, and you can integrate the client-side routing with server-side rendering using Next.js framework.

## Working with Lists & User Input

* What are some common issues when working with lists in React?
* You can forget to add key props, which can lead to performance issues and errors since React needs unique keys to re-render list items.
* Large lists can slow down rendering—consider virtualization like react-window, which can cause performance bottlenecks.
* The incorrectly updated states can create bugs, for example, mutating list items directly instead of using immutable updates.
* Changing list order or filtering without proper keys can lead to re-rendering issues and unexpected UI behavior.

### Styling with Tailwind CSS

* What are the advantages of using Tailwind CSS?
* It encourages rapid development with predefined classes.
* It supports responsive design built-in for desktop and mobile environments
* It reduces custom CSS, enforces design consistency, and removes unused styles in production.

* What are some potential pitfalls?
* The HTML files can become cluttered with long class strings, which can create messy files and reduce readability.
* It requires developers to understand utility-first design and Tailwind’s naming conventions, which can discourage use of semantic CSS or component-based styling.
* Applying complex customization like themes can be tricky if developers cannot understand the config system.

#### Handling State & User Input

* What happens if we modify state directly instead of using setState?
* React won’t detect the change, so the UI won’t update.
* Direct mutation can lead to unpredictable behavior and bugs.
* The direct modification violates the principle of immutability, which can break React’s data flow and make debugging harder.

##### Understanding Components & Props

* Why are components important in React?
* Components are modular because each component handles its own logic and presentation, and reusable so it avoids repetitive code for similar functions, which makes the architecture cleaner for large applications. It is also easier to update and debug isolated components.

###### Setting up a React project

* What challenges did you face during setup?
* When I download npm packages, it create conflicts because each package requires different versions of Javascript and Typescript, and this can lead to some functions not behaving properly. For example, when I download i18next package, the package requires typescript with version 5 or more, but my current typescript version is 4, and after that I have to update the version before installing the package, so it's important to manage Node versions, package managers, and dependencies to avoid future conflicts. Also, at first I'm struggled with file navigation since there are too many files and folders contained inside the big folder "react-code", so I have to put these files into small, manageable folders to store them properly and navigate files more quickly and easily.
