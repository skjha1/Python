#### components/Counter.js

```js
// Importing React and the useState hook from the 'react' package
import React, { useState } from 'react';

// Defining the Counter functional component
const Counter = () => {
  // Declaring a state variable 'count' and a function 'setCount' to update it, initializing 'count' to 0
  const [count, setCount] = useState(0);

  // Function to increment the count state by 1
  const increment = () => setCount(count + 1);

  // Function to decrement the count state by 1
  const decrement = () => setCount(count - 1);

  // Returning JSX to render the component
  return (
    <div>
      {/* Displaying the current count */}
      <h1>Counter: {count}</h1>
      {/* Button to increment the count, triggers increment function on click */}
      <button onClick={increment}>Increment</button>
      {/* Button to decrement the count, triggers decrement function on click */}
      <button onClick={decrement}>Decrement</button>
    </div>
  );
};

// Exporting the Counter component as the default export of this module
export default Counter;
```


#### App.js

```js
import logo from './logo.svg';
import './App.css';
import Counter from './components/Counter';

function App() {
  return (
    <div >
     <h1> MyReact Counter App </h1>
     <Counter />
    </div>
  );
}

export default App;
```




```
