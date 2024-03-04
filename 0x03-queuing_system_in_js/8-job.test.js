#!/usr/bin/node
/**
 * Writing the test for job creation
 */
import { createQueue } from 'kue';
import chai from 'chai';
import createPushNotificationsJobs from './8-job';

const expect = chai.expect;

const queue = createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
];

describe('createPushNotificationsJobs', () => {
  it('display a error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs(1, queue)).to.throw();
    expect(() => createPushNotificationsJobs(1, queue)).to.throw(/Jobs is not an array/);
  });

  it('throws if queue is not a valid kue', function() {
    expect(() => createPushNotificationsJobs(jobs, "")).to.throw();
  });
});