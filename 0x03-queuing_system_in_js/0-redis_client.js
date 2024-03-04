import { createClient } from "redis";
client = createClient();

client.on("error", function (err) {
    console.error(`Redis client not connected to the server: ${error.message}`);
});

client.on("connect", function () {
    console.log("Redis client connected to the server");
});