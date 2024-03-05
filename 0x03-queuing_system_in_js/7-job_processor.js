const kue = require('kue');

const queue = kue.createQueue();

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    done(error);
  } else {
    job.progress(50, 100);

    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    setTimeout(() => {
      job.progress(100, 100);

      done();
    }, 1000);
  }
}

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message, job, done);
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
 
