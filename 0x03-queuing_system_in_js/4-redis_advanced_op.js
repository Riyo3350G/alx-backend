import { createClient, print } from "redis";
const client = createClient();

client.on("error", function (err) {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

client.on("connect", function () {
    console.log("Redis client connected to the server");
});

client.hset('HolbertonSchools', 'Portland', '50', print);
client.hset('HolbertonSchools', 'Seattle', '80', print);
client.hset('HolbertonSchools', 'New York', '20', print);
client.hset('HolbertonSchools', 'Bogota', '20', print);
client.hset('HolbertonSchools', 'Cali', '40', print);
client.hset('HolbertonSchools', 'Paris', '2', print);

client.hgetall('HolbertonSchools', function (err, obj) {
    if (err) throw err;
    console.log(obj);
});
