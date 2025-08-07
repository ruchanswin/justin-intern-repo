export default function Button({ children, onClick }) {
  return (
    <button
      onClick={onClick}
      className="px-4 py-2 bg-blue-500 text-white rounded shadow hover:bg-blue-600 active:bg-blue-700 transition-colors duration-150"
    >
      {children}
    </button>
  );
}
