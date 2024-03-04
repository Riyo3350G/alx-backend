import { createClient, print } from "redis";
const client = createClient();

client.on("error", function (err) {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

client.on("connect", function () {
    console.log("Redis client connected to the server");
});

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, print);
}

const displaySchoolValue = (schoolName) => {
    client.get(schoolName, function (err, value) {
        console.log(value);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
