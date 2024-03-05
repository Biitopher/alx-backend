const chai = require('chai');
const expect = chai.expect;
const kue = require('kue');
const createPushNotificationsJobs = require('./8-job');

const queue = kue.createQueue();

queue.testMode.enter();

describe('createPushNotificationsJobs', () => {
  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should create jobs in the queue', () => {
    const jobsArray = [
      { phoneNumber: '1234567890', message: 'Notification 1' },
      { phoneNumber: '9876543210', message: 'Notification 2' },
    ];

    createPushNotificationsJobs(jobsArray, queue);

    expect(queue.testMode.jobs.length).to.equal(jobsArray.length);
  });

});

export default createPushNotificationsJobs;
