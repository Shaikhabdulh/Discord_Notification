# 🤖 Discord Reminder Bot Setup with GitHub Actions

A GitHub Actions-powered Discord bot that reminds your team to join the daily standup meeting at **5:50 PM IST (Mon–Fri)**. It also includes an inspiring quote fetched from the ZenQuotes API.
This document walks you through everything you need to set up a Discord bot that sends daily reminder messages via GitHub Actions. It includes setup, file structure, deployment, and how to get the necessary Discord IDs.

---

## ✅ Features

* ⏰ **Scheduled reminder at 5:50 PM IST**
* 📆 **Skips Saturday and Sunday**
* 🧘 **Includes motivational quote**
* 🔐 **Uses GitHub secrets for security**

---

## 📁 Project Structure

```
/my-repo
├── bot.py
├── README.md         # Main guide
├── ROLE_ID.md        # Linked from main README
└── .github/
    └── workflows/
        └── standup-reminder.yml
```

---

## 🚀 Setup Instructions

### 1. **Create a Discord Bot**

* Visit: [Discord Developer Portal](https://discord.com/developers/applications)
* Create an application → Go to **Bot** tab → Click **"Reset Token"** and copy it
* Under OAuth2 → URL Generator, select `bot` + `Send Messages`, generate the invite URL, and add it to your server

### 2. **Enable Developer Mode in Discord**

* Go to **User Settings → Advanced → Enable Developer Mode**
* Right-click your desired channel and role → Copy IDs for `THREAD_ID` and `ROLE_ID`
# For More Detailed Explanation, Follow Below Steps
---
## 🔧 Get Your Discord IDs (Enable Developer Mode)

### Step 2.1: Enable Developer Mode

1. Open the **Discord app**
2. Click **⚙️ User Settings** (bottom left)
3. Go to **Advanced** under "App Settings"
4. Turn **Developer Mode** → ON

### Step 2.2: Get `THREAD_ID`

1. Go to the **channel or thread** where your bot will post
2. Right-click the channel/thread name in the sidebar
3. Click **"Copy Channel ID"**
4. Save it as `THREAD_ID`

### Step 2.3: Get `ROLE_ID`

1. Click your **Server Name → Server Settings → Roles**
2. Right-click the desired role or click (⋯)
3. Select **"Copy Role ID"**
4. Save it as `ROLE_ID`
   
---

### 3. **Add GitHub Secrets**

Go to your repo → **Settings → Secrets → Actions → New repository secret**:

* `DISCORD_TOKEN` = Bot token from Discord Developer Portal
* `THREAD_ID` = Channel ID where bot should post
* `ROLE_ID` = Role ID to mention (optional)
## 📘 More Information 'ROLE_ID'

See [`ROLE_ID` = Role ID to mention (Why_it_is_optional)→](./ROLE_ID.md)

### 4. **Push the Code to GitHub**

Make sure both `bot.py` and `.github/workflows/standup-reminder.yml` are pushed.

### 5. **Run the Bot**

* Go to **Actions** tab in GitHub
* Manually trigger the workflow or wait for automatic daily trigger

---

## 🧪 Test Your Bot

* Trigger the workflow manually to confirm successful message delivery
* Check the thread in Discord for your bot's reminder message

---
## ⚠️ GitHub Free Tier Limitation:
- GitHub’s **`schedule:`** using `cron` in workflows (via `on: schedule`) can have **delays of 5–30+ minutes**, especially on the free tier.
- These delays are not reliable for time-sensitive tasks like **sending Discord reminders at an exact time**.

---

### ✅ Why cron-job.org?
- **External trigger** with precise control (no delay)
- Uses `workflow_dispatch` to manually trigger the workflow via **GitHub API**
- **Free, simple UI** with advanced controls (headers, body, method)
- Can send HTTP POST to GitHub’s workflow dispatch endpoint at exact scheduled time

---

### 🎯 Final Benefit:
This ensures **accurate, reliable reminders** at exactly **5:50 PM IST** without depending on GitHub's unpredictable schedule execution delays.
Here's a **comparison** between:

---

## 🔁 **1. GitHub Actions using `workflow_dispatch` + external trigger (`cron-job.org`)**
```yaml
name: Daily Standup Reminder

on:
  workflow_dispatch:
```

- **Trigger Type:** Manual (API or UI)
- **Scheduled via:** External service (e.g., [cron-job.org](https://cron-job.org))
- **Accuracy:** ✅ High (down to the minute)
- **Delay:** ❌ None (triggered exactly as scheduled)
- **Use Case:** When GitHub's `schedule:` is too unreliable

---

## ⏱️ **2. GitHub Actions using built-in `schedule` (cron expression)**
```yaml
name: Daily Standup Reminder

on:
  schedule:
    - cron: '20 12 * * 1-5'  # Runs Mon–Fri at 5:50 PM IST (12:20 UTC)
```

- **Trigger Type:** GitHub internal scheduler
- **Scheduled via:** GitHub Action cron
- **Accuracy:** ⚠️ Unreliable on free tier (5–30 min delays possible)
- **Delay:** ❗ May or may not run on time
- **Use Case:** Non-critical jobs, or if you’re on a paid GitHub tier

---

## ✅ Summary:
| Feature                     | `workflow_dispatch` + cron-job.org | `schedule:` in GitHub Actions |
|----------------------------|--------------------------------------|-------------------------------|
| Control over time          | ✅ Precise                           | ⚠️ Less control                |
| Delay in trigger           | ❌ None                              | ✅ Possible                    |
| Setup complexity           | ⚠️ Medium (external config needed)   | ✅ Simple                      |
| Best for reminders/alerts  | ✅ Yes                               | ❌ Not recommended             |

---

# 🔔 Discord Reminder Bot — Trigger with Cron-Job.org

Set up an external cron trigger for a GitHub Actions workflow using [cron-job.org](https://cron-job.org), with minimal GitHub token permissions.

---

## 🎯 Objective

Send a Discord reminder every weekday at **5:50 PM IST** (12:20 PM UTC).

> 💡 This setup helps avoid delays in GitHub Actions' built-in `schedule` trigger, especially on free-tier accounts.

---

## ⚙️ Prerequisites

* GitHub repository with a workflow file supporting `workflow_dispatch`
* Discord bot configured and working
* GitHub Personal Access Token (PAT)

---

## 🔐 GitHub Token Setup

1. Go to: [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. Click **"Generate new token (classic)"**
3. Name it: `CronJob Trigger Token`
4. Select expiration (e.g., 30 days)
5. ✅ Select **Only the following scopes**:

   * `repo` → `public_repo` *(if public repo)* or `repo` *(if private)*
   * `workflow`
6. Click **Generate token**
7. Copy and save the token securely.

> ⚠️ **Keep the GitHub token secret**. If exposed, immediately revoke and regenerate.

---

## 🌐 Create Trigger on cron-job.org

### 1. **Create Account**

* Visit [https://cron-job.org](https://cron-job.org)
* Click **Sign Up**, enter email and password, and verify your email
* Login to your account

### 2. **Add New Cron Job**

* From the left menu, click **Cronjobs**
* Click the blue **"Create Cronjob"** button

### 3. **Fill General Settings**

* **Title:** `Discord Reminder Trigger`
* **URL:**

  ```
  https://api.github.com/repos/YOUR_USERNAME/YOUR_REPO/actions/workflows/standup-reminder.yml/dispatches
  ```

  *Example:*

  ```
  https://api.github.com/repos/Shaikhabdulh/Discord_Notification/actions/workflows/standup-reminder.yml/dispatches
  ```

### 4. **Go to Advanced Settings**

Click **"Advanced Settings"** to configure headers, method, and body.

### 5. **Set Request Headers**

* In the **Request Headers** section:

  * Click **"Add Header"** 3 times
  * Add the following:

    * `Accept: application/vnd.github.v3+json`
    * `Authorization: Bearer YOUR_GITHUB_TOKEN`
    * `Content-Type: application/json`

### 6. **Set HTTP Method**

* In the **Method** section, select `POST` from the dropdown

### 7. **Set Request Body**

* In the **Request Body** section:

  * Choose **"Raw Data"**
  * Paste this JSON:

    ```json
    {
      "ref": "main"
    }
    ```

### 8. **Schedule the Cron Job**

* Scroll to **Schedule Settings**
* Select **Custom** option:

  * **Minutes:** `50`
  * **Hours:** `12`
  * **Days of week:** `Mon, Tue, Wed, Thu, Fri`
  * **Time Zone:** `UTC`

> ⏲️ 12:50 UTC = 5:50 PM IST

* ✅ Check **"Enable job"**
* Click **"Create Cronjob"** to save

---

## ✅ Verify

* Go to your GitHub repository → **Actions** tab
* Wait until scheduled time (e.g., 12:50 UTC)
* Confirm the workflow ran with trigger type `API`
* Verify that the Discord bot sent a message

---

## 🔒 Security Tips

* Use **minimal token permissions** (`workflow`, `repo`/`public_repo` only)
* **Regenerate token** immediately if leaked
* Never expose your token in code or logs
* Use GitHub secrets when integrating in code

---

⚠️ Important Limitations to Consider

While both methods offer great flexibility, you should be aware of the following limitations:

GitHub API Limits: Even with 5,000 requests/hour, excessive or misconfigured jobs may cause rate-limiting issues.

Action Minutes: Every run consumes minutes; the free tier offers 2,000 minutes/month across all workflows.

Cron-job.org Schedule Granularity: The free tier only allows jobs every 15 minutes minimum — not suitable for high-frequency tasks.

Execution Delays: External schedulers like cron-job.org may introduce minor delays (not real-time).
---
## 📘 More Information 'Limitations'

See [`Limitations`](./Limitations.md)

## 📌 Customization

* Change reminder time: edit the `cron` line in `standup-reminder.yml`
* Use your own quotes: replace `get_quote()` function in `bot.py`
* Post to multiple channels: duplicate the `fetch_channel()` and `send()` logic

---

## 📞 Support

Need help or want more features? Ping your DevOps/Automation engineer or drop your queries in this project's issue tab.

---

Made with 💻 + ☁️ by your AI assistant ✨
