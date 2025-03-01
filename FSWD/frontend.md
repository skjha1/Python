1. **Install Node.js and npm** if you haven't already. You can download and install them from [Node.js official website](https://nodejs.org/).

2. **Create a new React application**:
    ```bash
    npx create-react-app heart-data-ui
    cd heart-data-ui
    ```

3. **Install Axios** to make HTTP requests:
    ```bash
    npm install axios
    ```

4. **Start the React application**:
    ```bash
    npm start
    ```

#### Step 2: Create Components for Fetching and Displaying Heart Data

1. **Modify `src/App.js`** to include the basic structure and import necessary components:
    ```javascript
    import React, { useEffect, useState } from 'react';
    import axios from 'axios';
    import './App.css';

    function App() {
        const [heartData, setHeartData] = useState([]);
        const [formData, setFormData] = useState({
            name: '',
            age: '',
            heartRate: ''
        });

        useEffect(() => {
            fetchHeartData();
        }, []);

        const fetchHeartData = async () => {
            try {
                const response = await axios.get('http://localhost:5000/api/heartData');
                setHeartData(response.data);
            } catch (error) {
                console.error('Error fetching heart data:', error);
            }
        };

        const handleInputChange = (e) => {
            const { name, value } = e.target;
            setFormData({
                ...formData,
                [name]: value
            });
        };

        const handleSubmit = async (e) => {
            e.preventDefault();
            try {
                const response = await axios.post('http://localhost:5000/api/heartData', formData);
                setHeartData([...heartData, response.data]);
                setFormData({ name: '', age: '', heartRate: '' });
            } catch (error) {
                console.error('Error creating heart data:', error);
            }
        };

        return (
            <div className="App">
                <h1>Heart Data</h1>
                <form onSubmit={handleSubmit}>
                    <input
                        type="text"
                        name="name"
                        value={formData.name}
                        onChange={handleInputChange}
                        placeholder="Name"
                        required
                    />
                    <input
                        type="number"
                        name="age"
                        value={formData.age}
                        onChange={handleInputChange}
                        placeholder="Age"
                        required
                    />
                    <input
                        type="number"
                        name="heartRate"
                        value={formData.heartRate}
                        onChange={handleInputChange}
                        placeholder="Heart Rate"
                        required
                    />
                    <button type="submit">Add Heart Data</button>
                </form>
                <ul>
                    {heartData.map((data) => (
                        <li key={data._id}>
                            {data.name} - {data.age} years - {data.heartRate} bpm
                        </li>
                    ))}
                </ul>
            </div>
        );
    }

    export default App;
    ```

2. **Create CSS for styling** in `src/App.css`:
    ```css
    .App {
        text-align: center;
    }

    form {
        margin-bottom: 20px;
    }

    input {
        margin: 0 5px;
        padding: 5px;
    }

    button {
        padding: 5px 10px;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        background: #f9f9f9;
        margin: 5px 0;
        padding: 10px;
        border: 1px solid #ddd;
    }
    ```

3. **Run the React application** by starting the development server:
    ```bash
    npm start
    ```

Your React application will now fetch the heart data from your Node.js API and display it on the UI. You can add new heart data entries through the form, which will be sent to the backend and displayed on the UI.

This setup provides a basic yet interactive way to manage heart data using React and Node.js.





### Enhancing the React Application with Additional Components and UI Improvements

We'll create more detailed components for better separation of concerns and add some interesting UI elements like loading spinners and conditional rendering to improve the user experience.

#### Step 1: Create Components

1. **Create `HeartDataList.js`** to display the list of heart data:
    ```javascript
    // src/components/HeartDataList.js
    import React from 'react';

    function HeartDataList({ heartData, onDelete }) {
        return (
            <div>
                <h2>Heart Data</h2>
                {heartData.length > 0 ? (
                    <ul>
                        {heartData.map((data) => (
                            <li key={data._id}>
                                {data.name} - {data.age} years - {data.heartRate} bpm
                                <button onClick={() => onDelete(data._id)}>Delete</button>
                            </li>
                        ))}
                    </ul>
                ) : (
                    <p>No heart data available.</p>
                )}
            </div>
        );
    }

    export default HeartDataList;
    ```

2. **Create `HeartDataForm.js`** to add new heart data:
    ```javascript
    // src/components/HeartDataForm.js
    import React, { useState } from 'react';
    import axios from 'axios';

    function HeartDataForm({ onAdd }) {
        const [formData, setFormData] = useState({
            name: '',
            age: '',
            heartRate: ''
        });

        const handleInputChange = (e) => {
            const { name, value } = e.target;
            setFormData({
                ...formData,
                [name]: value
            });
        };

        const handleSubmit = async (e) => {
            e.preventDefault();
            try {
                const response = await axios.post('http://localhost:5000/api/heartData', formData);
                onAdd(response.data);
                setFormData({ name: '', age: '', heartRate: '' });
            } catch (error) {
                console.error('Error creating heart data:', error);
            }
        };

        return (
            <form onSubmit={handleSubmit}>
                <h2>Add Heart Data</h2>
                <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleInputChange}
                    placeholder="Name"
                    required
                />
                <input
                    type="number"
                    name="age"
                    value={formData.age}
                    onChange={handleInputChange}
                    placeholder="Age"
                    required
                />
                <input
                    type="number"
                    name="heartRate"
                    value={formData.heartRate}
                    onChange={handleInputChange}
                    placeholder="Heart Rate"
                    required
                />
                <button type="submit">Add Heart Data</button>
            </form>
        );
    }

    export default HeartDataForm;
    ```

3. **Create `LoadingSpinner.js`** for a loading state:
    ```javascript
    // src/components/LoadingSpinner.js
    import React from 'react';
    import './LoadingSpinner.css';

    function LoadingSpinner() {
        return (
            <div className="spinner-container">
                <div className="loading-spinner"></div>
            </div>
        );
    }

    export default LoadingSpinner;
    ```

4. **Add CSS for loading spinner** in `src/components/LoadingSpinner.css`:
    ```css
    /* src/components/LoadingSpinner.css */
    .spinner-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .loading-spinner {
        border: 8px solid rgba(0, 0, 0, 0.1);
        border-left-color: #222;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        animation: spin 1s linear infinite;
    }

    @keyframes spin {
        to {
            transform: rotate(360deg);
        }
    }
    ```

#### Step 2: Update the Main Component

1. **Update `FetchHeartData.js`** to handle loading state and use `HeartDataList` component:
    ```javascript
    // src/components/FetchHeartData.js
    import React, { useEffect, useState } from 'react';
    import axios from 'axios';
    import LoadingSpinner from './LoadingSpinner';
    import HeartDataList from './HeartDataList';

    function FetchHeartData() {
        const [heartData, setHeartData] = useState([]);
        const [loading, setLoading] = useState(true);

        useEffect(() => {
            fetchHeartData();
        }, []);

        const fetchHeartData = async () => {
            try {
                const response = await axios.get('http://localhost:5000/api/heartData');
                setHeartData(response.data);
            } catch (error) {
                console.error('Error fetching heart data:', error);
            } finally {
                setLoading(false);
            }
        };

        const handleDelete = async (id) => {
            try {
                await axios.delete(`http://localhost:5000/api/heartData/${id}`);
                setHeartData(heartData.filter((data) => data._id !== id));
            } catch (error) {
                console.error('Error deleting heart data:', error);
            }
        };

        return (
            <div>
                {loading ? (
                    <LoadingSpinner />
                ) : (
                    <HeartDataList heartData={heartData} onDelete={handleDelete} />
                )}
            </div>
        );
    }

    export default FetchHeartData;
    ```

2. **Update `App.js`** to include the form and fetch components:
    ```javascript
    // src/App.js
    import React, { useState } from 'react';
    import FetchHeartData from './components/FetchHeartData';
    import HeartDataForm from './components/HeartDataForm';
    import './App.css';

    function App() {
        const [heartData, setHeartData] = useState([]);

        const handleAddHeartData = (newData) => {
            setHeartData([...heartData, newData]);
        };

        return (
            <div className="App">
                <h1>Heart Data Management</h1>
                <HeartDataForm onAdd={handleAddHeartData} />
                <FetchHeartData heartData={heartData} setHeartData={setHeartData} />
            </div>
        );
    }

    export default App;
    ```

#### Step 3: Run the Application

1. **Start the React application**:
    ```bash
    npm start

```
