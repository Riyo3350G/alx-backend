import res from "express/lib/response";
import { createQueue } from "kue";
const queue = createQueue();

const jobInfo = {
    phoneNumber: "1234567890",
    message: "This is the code to verify your account",
};

const job = queue.create('push_notification_code', jobInfo).save((err) => {
    if (!err) {
        console.log(`Notification job created: ${job.id}`);
    }
});

job.on('complete', (result) => {
    console.log('Notification job completed');
});

job.on('failed', (err) => {
    console.log('Notification job failed');
});
