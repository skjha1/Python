To create and initialize a Node.js application using Express and MongoDB, follow these steps:

### 1. **Set Up a New Node.js Project**
   - First, create a new directory for your project and navigate into it:
     ```bash
     mkdir heart-app
     cd heart-app
     ```
   - Initialize a new Node.js project:
     ```bash
     npm init -y
     ```
   - This command generates a `package.json` file with default settings.

### 2. **Install Required Dependencies**
   - Install Express, Mongoose, and CORS:
     ```bash
     npm install express mongoose cors
     ```
   - Optionally, install `nodemon` for automatic server restarting during development:
     ```bash
     npm install --save-dev nodemon
     ```
   - Update your `package.json` to include a start script with `nodemon`:
     ```json
     "scripts": {
       "start": "nodemon index.js"
     }
     ```

### 3. **Create the Main Application File**
   - Create a file named `index.js` and set up the basic structure:
     ```javascript
     const express = require('express');
     const mongoose = require('mongoose');
     const cors = require('cors');

     const app = express();
     const port = 5000;

     app.use(cors());
     app.use(express.json());

     // MongoDB connection
     mongoose.connect('mongodb://localhost:27017/heartDB', {
         useNewUrlParser: true,
         useUnifiedTopology: true,
     });

     // Log MongoDB connection events
     mongoose.connection.on('connected', () => {
         console.log('Mongoose connected to heartDB');
     });

     mongoose.connection.on('error', (err) => {
         console.log('Mongoose connection error: ' + err);
     });

     // Define the schema and model
     const heartSchema = new mongoose.Schema({
         name: String,
         age: Number,
         heartRate: Number,
     });

     const Heart = mongoose.model('Heart', heartSchema);

     // API endpoint to fetch heart data
     app.get('/api/heartData', async (req, res) => {
         try {
             const heartData = await Heart.find();
             console.log('Heart Data:', heartData); // Log fetched data
             res.json(heartData);
         } catch (error) {
             console.error('Error fetching heart data:', error); // Log error
             res.status(500).send(error);
         }
     });

     // API endpoint to create a new heart data entry
     app.post('/api/heartData', async (req, res) => {
         const { name, age, heartRate } = req.body;

         try {
             const newHeartData = new Heart({ name, age, heartRate });
             await newHeartData.save();
             console.log('New Heart Data created:', newHeartData); // Log created data
             res.status(201).json(newHeartData); // Return the created data
         } catch (error) {
             console.error('Error creating heart data:', error); // Log error
             res.status(500).send(error);
         }
     });

     // API endpoint to delete a heart data entry by ID
     app.delete('/api/heartData/:id', async (req, res) => {
         const { id } = req.params;

         try {
             const deletedHeartData = await Heart.findByIdAndDelete(id);
             if (!deletedHeartData) {
                 return res.status(404).send('Heart Data not found');
             }
             console.log('Heart Data deleted:', deletedHeartData); // Log deleted data
             res.status(200).json(deletedHeartData); // Return the deleted data
         } catch (error) {
             console.error('Error deleting heart data:', error); // Log error
             res.status(500).send(error);
         }
     });

     app.listen(port, () => {
         console.log(`Server is running on http://localhost:${port}`);
     });
     ```

### 4. **Run the Application**
   - Start the server:
     ```bash
     npm start
     ```
   - Your server will be running at `http://localhost:5000`.

### 5. **Test the Endpoints**
   - Use Postman or any other API testing tool to test the following endpoints:
     - **GET** `/api/heartData` - Fetch all heart data entries.
     - **POST** `/api/heartData` - Create a new heart data entry.
     - **DELETE** `/api/heartData/:id` - Delete a heart data entry by ID.

This setup provides a basic structure for a Node.js application using Express and MongoDB, with API endpoints for managing heart data.
