/* lista */
const kue = require('kue'),
      queue = kue.createQueue();

const aLotOfJob = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ];

for (const oneJob of aLotOfJob) {
  let jobs = queue.create('push_notification_code_2', oneJob)
    .save(err => {
      if (!err) console.log(`Notification job created: ${jobs.id}`);
    })
    .on('complete', () => console.log(`Notification job ${jobs.id} completed`))
    .on('failed', (err) => console.log(`Notification job ${jobs.id} failed: ${err}`))
    .on('progress', (percentage) => console.log(`Notification job ${jobs.id} ${percentage}% complete`));
}