#!/usr/bin/yarn dev
import { createQueue } from "kue";

const queue = createQueue({ name: "push_notification_code" });

const job = queue.create("push_notification_code", {
  phoneNumber: "1234554321",
  message: "Account registered with success",
});

job
  .on("enqueue", () => {
    console.log("Notification job created:", job.id);
  })
  .on("complete", () => {
    console.log("Notification job completed");
  })
  .on("failed attempt", () => {
    console.log("Notification job failed");
  });
job.save();
