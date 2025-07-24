# ⚠️ Important Notes
## ✅ **1. GitHub ****************`workflow_dispatch`**************** (Manual Trigger via API)**

| Feature                       | GitHub Free Tier                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Trigger Method**            | Manual via UI or API                                                                                                     |
| **Limitations on Triggering** | ❌ No hard limit (but... see below)                                                                                       |
| **Rate Limit (API)**          | ✅ [5,000 requests/hour per user/token](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting) |
| **Action Minutes Consumed**   | ✅ Yes (counts toward monthly limit)                                                                                      |
| **Delays in Trigger**         | ❌ **No delay** (runs immediately)                                                                                        |

✅ Best for **on-demand** execution, scripting, or controlled scheduling.

---

## ✅ **2. ****************`cron-job.org`**************** (External Cron Trigger)**

| Feature                   | Value                                                            |
| ------------------------- | ---------------------------------------------------------------- |
| **Trigger Method**        | Scheduled HTTP requests to GitHub API                            |
| **Execution Delay**       | ⏳ Depends on their internal queue, usually minor (∼30 sec–2 min) |
| **Free Tier Schedule**    | Every 15 minutes minimum (not per minute)                        |
| **Limitations**           | ✔️ **50 jobs per account** (Free Tier)                           |
| **GitHub API Rate Limit** | 🔁 Still applies (uses your GitHub token)                        |
| **Execution Reliability** | ✅ Good for lightweight, periodic triggers                        |
| **Action Minutes Used?**  | ✅ Yes (GitHub workflow still runs)                               |

---

## 🔍 [`Limitations`](#) *(Why\_It\_Is\_Important)* →

While both methods offer great flexibility, you should be aware of the following limitations:

### 📌 GitHub Action Free Tier Limits

* ✅ **2,000 minutes/month** per account (public repos are unlimited)
* 📉 **Storage limits**: 500MB for artifacts + 1GB for logs
* 🧪 **Concurrent jobs**: Only 20 max jobs can run simultaneously
* ⏱️ **Job Timeout**: 6 hours max per job
* 💵 Additional minutes cost \$0.008/min after the free tier

### 📌 API Usage Limits

* 🔁 5,000 API requests/hour per user/token (shared across all jobs)
* ❌ Rate limit resets every hour — ensure your scheduler doesn't flood requests

### 📌 External Scheduler (`cron-job.org`) Constraints

* ⏳ Minimum frequency: Every 15 minutes
* 🔢 Max 50 jobs/account
* 🔐 Still consumes GitHub action minutes and API quota
* 🕒 Possible slight execution delays due to queue

✅ These are **not blockers** but key **constraints** to plan around.

---
