const express = require('express');
const createClient = require('redis').createClient;
const promisify = require('util').promisify;
const kue = require('kue');
const queue = kue.createQueue();

// Create Redis client
const client = createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

let reservationEnabled = true;

client.set('available_seats', 50);

// Function to reserve a seat
async function reserveSeat(number) {
    await setAsync('available_seats', number);
}

// Function to get current available seats
async function getCurrentAvailableSeats() {
    const seats = await getAsync('available_seats');
    return parseInt(seats, 10);
}

// Express server setup
const app = express();
const port = 1245;

app.get('/available_seats', async (req, res) => {
    const seats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats: seats.toString() });
});

app.get('/reserve_seat', (req, res) => {
    if (!reservationEnabled) {
        return res.json({ status: 'Reservation are blocked' });
    }

    const job = queue.create('reserve_seat', {}).save((err) => {
        if (err) {
            return res.json({ status: 'Reservation failed' });
        }

        res.json({ status: 'Reservation in process' });
    });

    job.on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
    }).on('failed', (errorMessage) => {
        console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
    });
});

app.get('/process', (req, res) => {
    queue.process('reserve_seat', async (job, done) => {
        let seats = await getCurrentAvailableSeats();
        if (seats > 0) {
            seats -= 1;
            await reserveSeat(seats);
            if (seats === 0) {
                reservationEnabled = false;
            }
            done();
        } else {
            done(new Error('Not enough seats available'));
        }
    });
    res.json({ status: 'Queue processing' });
});

// Starting the server
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
