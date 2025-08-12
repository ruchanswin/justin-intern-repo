## How to Set Up a React Project

### 1. Normal React Project (using Create React App)

1. Install Node.js (<https://nodejs.org/>)
2. Open your terminal and run:

   ```sh
   npx create-react-app my-app
   cd my-app
   npm start
   ```

#### Install Tailwind CSS in Create React App

1. Install Tailwind and dependencies:

   ```sh
   npm install -D tailwindcss postcss autoprefixer
   npx tailwindcss init -p
   ```

2. Configure `tailwind.config.js`:

   ```js
   module.exports = {
     content: ["./src/**/*.{js,jsx,ts,tsx}"],
     theme: { extend: {} },
     plugins: [],
   };
   ```

3. Add Tailwind to `src/index.css`:

   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```

4. Restart your dev server.

### 2. React + Vite Project

1. Install Node.js (<https://nodejs.org/>)
2. Open your terminal and run:

   ```sh
   npm create vite@latest my-vite-app -- --template react
   cd my-vite-app
   npm install
   npm run dev
   ```

#### Install Tailwind CSS in Vite React Project

1. Install Tailwind and dependencies:

   ```sh
   npm install -D tailwindcss postcss autoprefixer
   npx tailwindcss init -p
   ```

2. Configure `tailwind.config.js`:

   ```js
   module.exports = {
     content: ["./src/**/*.{js,jsx,ts,tsx}"],
     theme: { extend: {} },
     plugins: [],
   };
   ```

3. Add Tailwind to `src/index.css` (or `src/main.css`):

   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```

4. Restart your dev server.
