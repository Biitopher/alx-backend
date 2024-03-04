const kue = require('kue');

const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message);

  done();
});

queue.on('job enqueue', (id, type) => {
  console.log(`Job ${id} of type ${type} is now in progress`);
});

queue.on('job complete', (id) => {
  console.log(`Job ${id} is completed`);
  process.exit(0);
});

queue.on('error', (err) => {
  console.error('Queue error:', err);
  process.exit(1);
});
