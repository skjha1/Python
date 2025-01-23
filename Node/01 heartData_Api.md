
```js
// mkdir heart-app 
// cd heart-app

// npm init -y 
// npm install express mongoose cors

// Create a file with index.js
// node inde.js


const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');


const app = express();
const port = 5000;


app.use(cors());
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/heartDB', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});


mongoose.connection.on('connected', () => {
    console.log('Mongoose connected to heartDB')
});

mongoose.connection.on('error', (err) => {
    console.log('Mongoose connection error: ' + err);
});

const heartSchema = new mongoose.Schema ({
    name: String,
    age: Number,
    heartRate: Number,
});

const Heart = mongoose.model('Heart', heartSchema);


app.get('/api/heartData', async (req, res) => {
    try {
        const heartData = await Heart.find();
        console.log('Heart Data: ', heartData);
        res.json(heartData);
    } catch (error) {
        console.error('Error fetching the details from feart data:' , error);
        res.status(500).send(error);
    }
});

app.post('/api/heartData', async (req, res) => {
    const {name, age, heartRate} = req.body

    try{
        const newHeartData = new Heart({name, age, heartRate}); 
        await newHeartData.save();
        console.log('New Heart Data created: ', newHeartData); // Log created data
        res.status(201).json(newHeartData); // return the created data
    } catch (error) {
        console.error('Error creating heart data: ', error); // log error
        res.status(500).send(error);
    }
}); 

// API endpoint to delete heart data by id

app.delete('/api/heartData/:id', async(req, res) => {
    const {id} = req.params;

    try {
        const deletedHeartData = await Heart.findByIdAndDelete(id)
        if(!deletedHeartData){
            return res.status(404).send('Heart Data not found');
        }
        console.log('Heart Data deleted: ', deletedHeartData);
        res.status(200).json(deletedHeartData);
    } catch (error) {
        console.error('Error deleting heart data: ', error);
        res.status(500).send(error);
    }
})


app.listen(port, () => {
    console.log(`Server is running on port http://localhost:${port}`);
})
```
