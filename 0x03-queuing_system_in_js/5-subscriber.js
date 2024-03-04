import { createClient } from "redis";
const client = createClient();

client.on("error", function (err) {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

client.on("connect", function () {
    console.log("Redis client connected to the server");
});

client.subscribe('holberton school channel');
client.on('message', function (channel, message) {
    if (channel === 'holberton school channel') {
        if (message === 'KILL_SERVER') {
            client.unsubscribe(channel);
            client.quit();
        } else {
            console.log(message);
        }
    }
});
