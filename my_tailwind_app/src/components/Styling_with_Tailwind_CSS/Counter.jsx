import { useState } from 'react';
import Button from './Button';

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50">
      <h1 className="text-2xl font-bold mb-4">Counter: {count}</h1>
      <div className="flex gap-4">
        <Button onClick={() => setCount(count - 1)}>
          -
        </Button>
        <Button onClick={() => setCount(count + 1)}>
          +
        </Button>
      </div>
    </div>
  );
}
