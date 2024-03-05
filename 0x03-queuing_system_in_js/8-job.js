const kue = require('kue');

const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData)
      .save((err) => {
        if (!err) {
          console.log(`Notification job created: ${job.id}`);
        } else {
          console.error(`Error creating notification job: ${err}`);
        }
      });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
      process.exit(0);
    });

    job.on('failed', (err) => {
      console.error(`Notification job ${job.id} failed: ${err}`);
      process.exit(1);
    });

    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}


const jobsArray = [
  { phoneNumber: '1234567890', message: 'Notification 1' },
  { phoneNumber: '9876543210', message: 'Notification 2' },
];

export default createPushNotificationsJobs;
